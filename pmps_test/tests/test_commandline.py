from pmps_test.bin.system_tests import main as system_tests_main


def test_system_tests_main():
    k = system_tests_main("pmp_test/pmps")
    print(k)
    assert False
