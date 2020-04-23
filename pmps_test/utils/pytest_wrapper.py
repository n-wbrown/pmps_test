import pytest
import typing


def targeted_pytest(target_directory: str = None,
                    pytest_args: typing.List = None,
                    pytest_plugins: typing.List = None) -> None:

    pytest.main(
        args=[f"{target_directory}"]+pytest_args,
        # plugins=pytest_plugins,
    )
