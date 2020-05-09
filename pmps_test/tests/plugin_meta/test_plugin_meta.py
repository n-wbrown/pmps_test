import pytest 

def test_load_static_plugin_fixture(xyz):
    pass

def test_base_pv_fixture_exists(base_pv):
    """
    Test that the fixture exists
    """
    pass

def test_base_pv_multiple_args(base_pv):
    """
    Test that a variable number of PVs can be passed 
    """
    result = base_pv
    print(result)
    assert type(result) is dict, "bad type returned"
    assert len(result) is 3, "Dictionary has incorrect length"
    assert result['pv1'] == "AB1C0:TEST"
    assert result['pv2'] == "DE1F1:DEBUG"
    assert result['spare_PV'] == "GH2I3:DEPLOY"