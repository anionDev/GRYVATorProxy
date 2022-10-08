import sys
from pathlib import Path
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def build():
    TasksForCommonProjectStructure().standardized_tasks_build_for_docker_codeunit(str(Path(__file__).absolute()), "QualityCheck", sys.argv)


if __name__ == "__main__":
    build()
