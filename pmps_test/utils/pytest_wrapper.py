import pytest
import typing


def targeted_pytest(target_direrctory: str = None,
                    pytest_args: typing.List = None,
                    pytest_plugins: typing.List = None) -> None:
    pytest.main(
        args=[target_direrctory]+pytest_args,
        plugins=pytest_plugins,
    )
