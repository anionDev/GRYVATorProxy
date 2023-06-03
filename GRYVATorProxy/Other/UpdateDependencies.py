from pathlib import Path
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure
import requests


def get_debian_version(image_tag: str) -> str:
    result = ScriptCollectionCore().run_program_argsasarray(
        "docker", ['run', f'debian:{image_tag}', 'bash', '-c', 'apt-get -y update && apt-get -y install lsb-release && lsb_release -cs'])
    result_line = GeneralUtilities.string_to_lines(result[1])[-2]
    return result_line


def get_latest_tor_version_of_debian_repository(debian_version) -> str:
    package_url = f"https://deb.torproject.org/torproject.org/dists/{debian_version}/main/binary-amd64/Packages"
    r = requests.get(package_url)
    if r.status_code != 200:
        raise ValueError(f"Checking for latest tor package resulted in HTTP-response-code {r.status_code}.")
    lines = GeneralUtilities.string_to_lines(GeneralUtilities.bytes_to_string(r.content))
    version_line_prefix = "Version: "
    version_content_line = [line for line in lines if line.startswith(version_line_prefix)][1]
    version_with_overhead = version_content_line[len(version_line_prefix):]
    version = version_with_overhead.split("~")[0]
    return version


def update_dependency_in_resources_folder(update_dependencies_file, dependency_name: str, latest_version_function: str):
    version_file = GeneralUtilities.resolve_relative_path(f"../Resources/Dependencies/{dependency_name}/Version.txt", update_dependencies_file)
    current_version = GeneralUtilities.read_text_from_file(version_file)
    if current_version != latest_version_function:
        GeneralUtilities.write_text_to_file(version_file, latest_version_function)


def update_dependencies():
    script_file = str(Path(__file__).absolute())
    debian_version = get_debian_version("stable-slim")
    update_dependency_in_resources_folder(script_file, "Tor", get_latest_tor_version_of_debian_repository(debian_version))


if __name__ == "__main__":
    update_dependencies()
