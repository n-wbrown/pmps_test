from pmps_test.bin.system_tests import main as system_tests_main

from pytest import ExitCode


def test_system_tests_main():
    # Confirm functionality of the main.system_tests_main commandline utility
    assert system_tests_main(
            ["pmps_test/pmps", "-k", "test_True"]
        ) == ExitCode(0), \
        "system_tests_main fails with path argument"
    assert system_tests_main(
            ["pmps_test/pmps", "-k", "test_False"]
        ) == ExitCode(1), \
        "system_tests_main fails to catch a bad test"
    assert system_tests_main(["--ignore=pmps_test/tests"]) == ExitCode(1), \
        "system_tests_main fails with path argument"

def test_plugin_fixture():
    assert system_tests_main(
            ["pmps_test/pmps", "-k", "test_fixture"]
        ) == ExitCode(0), \
        "system_tests_main is not accessing the plugin"
