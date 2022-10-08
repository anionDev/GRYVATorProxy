import sys
from pathlib import Path
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def generate_reference():
    TasksForCommonProjectStructure().standardized_tasks_generate_refefrence_for_codeunit_in_common_project_structure(str(Path(__file__).absolute()), sys.argv)

generate_reference()
