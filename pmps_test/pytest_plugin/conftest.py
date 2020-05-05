import pytest
from .pcds_fixtures import *




AMS_NET_ID_OPTION = "--ams_net_id"

def pytest_addoption(parser):
    """
    This is a built-in pytest hook.

    This function allows os to pass options directly to pytest when run.
    """
    parser.addoption(
        AMS_NET_ID_OPTION, action="store", default=None,
        help="AMS NET ID adress list passed via command"
        "line. Supersedes the .ini file"
    )
    parser.addini(
        AMS_NET_ID_OPTION.strip("-"), default=None,
        help="AMS NET ID address list passed via the .ini file."
    )


@pytest.fixture
def ams_net_id(request):
    """
    Set AMS_NET_ID of target PLC
    """
    if request.config.getini(AMS_NET_ID_OPTION) is not None:
        return request.config.getini(AMS_NET_ID_OPTION)
    else:
        return request.config.getoption(AMS_NET_ID_OPTION)
     

@pytest.fixture
def sample_fixture():
    return "sample_fixture"