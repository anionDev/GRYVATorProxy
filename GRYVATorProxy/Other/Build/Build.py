from ast import arg
import os
import sys
from pathlib import Path
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def standardized_tasks_build_for_docker_library_project_in_common_project_structure(self: TasksForCommonProjectStructure, build_script_file: str, build_configuration: str, verbosity: int, commandline_arguments: list[str]):
    # TODO use verbosity-value
    # TODO use sys_argv-value
    use_cache: bool = False  # TODO make configurable
    sc: ScriptCollectionCore = ScriptCollectionCore()
    codeunitname: str = Path(os.path.dirname(build_script_file)).parent.parent.name
    codeunit_folder = GeneralUtilities.resolve_relative_path(f"../..", str(os.path.dirname(build_script_file)))

    codeunitname_lower = codeunitname.lower()
    version = self.get_version_of_codeunit(os.path.join(codeunit_folder, f"{codeunitname}.codeunit"))
    args = ["image", "build", "--pull", "--force-rm", "--progress=plain", "--build-arg", f"EnvironmentStage={build_configuration}",
            "--tag", f"{codeunitname_lower}:latest", "--tag", f"{codeunitname_lower}:{version}", "--file", "Dockerfile"]
    if not use_cache:
        args.append("--no-cache")
    args.append(".")
    codeunit_content_folder = os.path.join(codeunit_folder, codeunitname)
    sc.run_program_argsasarray("docker", args, codeunit_content_folder)
    artifacts_folder = GeneralUtilities.resolve_relative_path("Other/Artifacts", codeunit_folder)
    app_artifacts_folder = os.path.join(artifacts_folder, "ApplicationImage")
    GeneralUtilities.ensure_directory_does_not_exist(app_artifacts_folder)
    GeneralUtilities.ensure_directory_exists(app_artifacts_folder)
    sc.run_program_argsasarray("docker", ["save", "--output", f"{codeunitname}_v{version}.tar", f"{codeunitname_lower}:{version}"], app_artifacts_folder)


def build():
    standardized_tasks_build_for_docker_library_project_in_common_project_structure(TasksForCommonProjectStructure(), str(Path(__file__).absolute()), "QualityCheck", 1, sys.argv)


if __name__ == "__main__":
    build()
