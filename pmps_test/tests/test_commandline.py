import pytest

from pmps_test.bin.system_tests import main as system_tests_main

def test_system_tests_main():
    system_tests_main("pmp_test/pmps")