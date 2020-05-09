import pytest

def test_import_testdir(testdir):
    testdir.copy_example("conftest.py")
    testdir.copy_example("test_plugin_meta.py")
    result = testdir.runpytest("-k","test_load_static_plugin_fixture")
    result.assert_outcomes(passed=1)

def test_base_pv_no_arg(testdir):
    testdir.copy_example("test_plugin_meta.py")
    result = testdir.runpytest("-k","test_base_pv_fixture_exists")
    result.assert_outcomes(passed=1)

def test_base_pv_multi_arg(testdir):
    testdir.copy_example("test_plugin_meta.py")
    result = testdir.runpytest("-k","test_base_pv_multiple_args")
    result.assert_outcomes(passed=1)
