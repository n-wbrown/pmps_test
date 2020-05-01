import pytest

AMS_NET_ID_OPTION = "--ams_net_id_old"
CMDOPT_OPTION = "--cmdopt_old"


def pytest_load_initial_conftests(args, early_config, parser):
    pass


def pytest_addoption(parser):
    """
    This is a built-in pytest hook. Don't rename this function

    This function allows os to pass options directly to pytest when run.
    """
    parser.addoption(
        AMS_NET_ID_OPTION, action="store", default=False,
        help="Example argument passed via command line"
    )
    parser.addoption(
        CMDOPT_OPTION, action="store", default="type1",
        help="Example argument passed programmatically"
    )


def pytest_configure(config):
    pass


@pytest.fixture
def ams_net_id(request):
    return request.config.getoption(AMS_NET_ID_OPTION)


@pytest.fixture
def cmdopt(request):
    return request.config.getoption(CMDOPT_OPTION)
