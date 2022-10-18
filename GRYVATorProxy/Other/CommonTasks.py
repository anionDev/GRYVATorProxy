import sys
import os
import re
from pathlib import Path
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def replace_version_in_dockerfile_file(self: ScriptCollectionCore, dockerfile: str, version: str) -> None:
    GeneralUtilities.write_text_to_file(dockerfile, re.sub("ARG Version = \"\\d+\\.\\d+\\.\\d+\"", f"ARG Version = \"{version}\"",
                                                           GeneralUtilities.read_text_from_file(dockerfile)))


def common_tasks():
    file = str(Path(__file__).absolute())
    folder_of_current_file = os.path.dirname(file)
    sc = ScriptCollectionCore()
    version = sc.get_semver_version_from_gitversion(GeneralUtilities.resolve_relative_path("../..", os.path.dirname(file)))
    replace_version_in_dockerfile_file(sc, GeneralUtilities.resolve_relative_path("../GRYVATorProxy/Dockerfile", folder_of_current_file), version)
    tfcps = TasksForCommonProjectStructure()
    tfcps.standardized_tasks_do_common_tasks(file, 1, "QualityCheck", True, sys.argv)


if __name__ == "__main__":
    common_tasks()
