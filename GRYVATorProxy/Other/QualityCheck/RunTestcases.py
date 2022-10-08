import os
import sys
from datetime import datetime
from pathlib import Path
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def standardized_tasks_run_testcases_for_docker_project_in_common_project_structure(self: TasksForCommonProjectStructure, run_testcases_script_file: str, verbosity: int, commandline_arguments: list[str]):
    codeunit_folder = GeneralUtilities.resolve_relative_path(f"../..", str(os.path.dirname(run_testcases_script_file)))
    repository_folder: str = str(Path(os.path.dirname(run_testcases_script_file)).parent.parent.parent.absolute())
    codeunitname: str = Path(os.path.dirname(run_testcases_script_file)).parent.parent.name
    date = int(round(datetime.now().timestamp()))
    # TODO generate real coverage report
    dummy_test_coverage_file = f"""<?xml version="1.0" ?>
<coverage version="6.3.2" timestamp="{date}" lines-valid="0" lines-covered="0" line-rate="0" branches-covered="0" branches-valid="0" branch-rate="0" complexity="0">
	<sources>
		<source>{codeunitname}</source>
	</sources>
	<packages>
		<package name="{codeunitname}" line-rate="0" branch-rate="0" complexity="0">
		</package>
	</packages>
</coverage>"""
    artifacts_folder = GeneralUtilities.resolve_relative_path("Other/Artifacts", codeunit_folder)
    testcoverage_artifacts_folder = os.path.join(artifacts_folder, "TestCoverage")
    testcoverage_file = os.path.join(testcoverage_artifacts_folder, "TestCoverage.xml")
    GeneralUtilities.ensure_file_exists(testcoverage_file)
    GeneralUtilities.write_text_to_file(testcoverage_file, dummy_test_coverage_file)
    self.standardized_tasks_generate_coverage_report(repository_folder, codeunitname, verbosity, True, commandline_arguments)


def run_testcases():
    standardized_tasks_run_testcases_for_docker_project_in_common_project_structure(TasksForCommonProjectStructure(), str(Path(__file__).absolute()),  1, sys.argv)


if __name__ == "__main__":
    run_testcases()
