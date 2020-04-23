from pmps_test.bin.system_tests import main as system_tests_main


def test_system_tests_main():
    k = system_tests_main(["pmps_test/pmps", "--capture=sys", "-q"])
