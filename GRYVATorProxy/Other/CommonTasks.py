import sys
import os
from pathlib import Path
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def common_tasks():
    file = str(Path(__file__).absolute())
    sc = ScriptCollectionCore()
    version = sc.getversion_from_arguments_or_gitversion(file, sys.argv)
    TasksForCommonProjectStructure().update_version_of_codeunit_to_project_version(file, version)


if __name__ == "__main__":
    common_tasks()
