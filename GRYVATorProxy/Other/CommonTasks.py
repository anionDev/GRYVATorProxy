import sys
import os
from pathlib import Path
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def common_tasks():
    file = str(Path(__file__).absolute())
    folder_of_current_file = os.path.dirname(file)
    sc = ScriptCollectionCore()
    version = sc.getversion_from_arguments_or_gitversion(file, sys.argv)
    TasksForCommonProjectStructure().update_version_of_codeunit_to_project_version(file, version)
    sc.replace_version_in_csproj_file(GeneralUtilities.resolve_relative_path("../GRYVATorProxy/Dockerfile", folder_of_current_file), version)


if __name__ == "__main__":
    common_tasks()
