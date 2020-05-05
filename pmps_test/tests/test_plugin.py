import pytest

def test_import_testdir(testdir):
    testdir.makeconftest(
        """
        import pytest
        """
    )
    testdir.copy_example("test_plugin_meta.py")
    result = testdir.runpytest("-k","test_fake")
    result.assert_outcomes(passed=1)


def test_fake():
    assert False