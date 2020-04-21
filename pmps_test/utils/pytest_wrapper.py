import pytest
import types

def targeted_pytest(target_direrctory=None: str, 
            pytest_args=None: List) -> xml:
    pytest.main(
        args=[target_directory] + pytest_extra_args,
        plugins=pytest_plugins,
    )