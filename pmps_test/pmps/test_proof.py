import logging

import pytest


logger = logging.getLogger(__name__)


def test_True():
    assert True


def test_False():
    assert False


def test_fixture(sample_fixture):
    print(sample_fixture())
    assert False


def test_passed_args(cmdopt):
    """
    Example test using an argument passed programatically
    """
    print(cmdopt)
    assert cmdopt == 100


def test_commandline_args(ams_net_id):
    """
    Example test using an argument passed at runtime
    """
    print(ams_net_id)
    assert ams_net_id == "127.0.0.1.1.1"


@pytest.mark.incremental
class TestClassTests:
    @classmethod
    def setup_class(cls):
        print("print_setup")
        cls.setting = 19
        return cls

    @classmethod
    def teardown_class(cls):
        print("print_teardown")

    def test_this(self):
        print(f"this {self.setting}")
        assert False

    def test_that(self):
        print(f"that {self.setting}")
        assert False
