import pytest

@pytest.fixture
def sample_fixture():
    """
    Confirm availability of plugin fixtures.
    """
    return "This is sample_fixture's string"
