import pytest
import typing


def targeted_pytest(target_directory: str,
                    pytest_args: typing.List = None,
                    pytest_plugins: typing.List = None) -> None:

    args = [f"{target_directory}"]
    if pytest_args is not None:
        args.extend(pytest_args)

    plugins = ["pmps_test"]
    if pytest_plugins is not None:
        plugins.extend(pytest_plugins)

    result = pytest.main(
        args=args,
        plugins=plugins,
    )

    return result
