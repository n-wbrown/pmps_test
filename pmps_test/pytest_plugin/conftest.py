import pytest
from .pcds_fixtures import *




AMS_NET_ID_OPTION = "--ams_net_id"
BASE_PV_OPTION = "--pv"

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

    parser.addini(
        BASE_PV_OPTION.strip("-"), default=None,
        help="Provide PVs to be tested."
    )
    parser.addoption(
        BASE_PV_OPTION, action="store", default=None,
        help="Provide PVs to be tested. Supersedes the .ini file."
    )

def pytest_load_initial_conftests(early_config, parser, args):
    print(args)


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

@pytest.fixture
def base_pv(request):
    """
    set BASE_PV dictionary for tests
    """
    if request.config.getini(BASE_PV_OPTION.strip("-")) is not None:
        return request.config.getini(BASE_PV_OPTION.strip("-"))
    else:
        return request.config.getoption(BASE_PV_OPTION)
