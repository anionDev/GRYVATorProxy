import sys
from pathlib import Path
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def standardized_tasks_linting_for_docker_project_in_common_project_structure(self: TasksForCommonProjectStructure, linting_script_file: str, verbosity: int, commandline_arguments):
    pass  # TODO


def linting():
    standardized_tasks_linting_for_docker_project_in_common_project_structure(TasksForCommonProjectStructure()(), str(Path(__file__).absolute()), 1, sys.argv)


if __name__ == "__main__":
    linting()
