import argparse
import importlib.resources
import logging
from textwrap import dedent, fill

import pytest

import pmps_test
from ..pmps.conftest import CMDOPT_OPTION
import pmps_test.pmps

logger = logging.getLogger(__name__)


DESCRIPTION = fill(dedent("""
    Arbitrary test suite. Unrecognized arguments will be passed directly to
    pytest.
    """)).strip()


def main(args=None):

    top_parser = argparse.ArgumentParser(
        prog="system_tests",
        description=DESCRIPTION,
    )

    # unknown_args are not recognized by argparse and will be sent to pytest
    args, unknown_args = top_parser.parse_known_args(args)

    with importlib.resources.path(pmps_test.pmps, ".") as p:
        pmps_test_root_dir = p

    pytest_args = [
        f"{pmps_test_root_dir}",
        f"{CMDOPT_OPTION}=90",
    ] + unknown_args
    pytest_plugins = None

    pytest.main(
        args=pytest_args,
        plugins=pytest_plugins,
    )


if __name__ == "__main__":
    main()
