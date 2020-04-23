import argparse
import importlib.resources
import logging
from os import getcwd
from textwrap import dedent, fill

import pmps_test
from ..pmps.conftest import CMDOPT_OPTION
from ..utils.pytest_wrapper import targeted_pytest
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

    top_parser.add_argument(
        "test_path", type=str, help="Directory containing tests", 
        default=getcwd()
    )

    # unknown_args are not recognized by argparse and will be sent to pytest
    args, unknown_args = top_parser.parse_known_args(args)

    # stash static tests directory
    with importlib.resources.path(pmps_test.pmps, ".") as p:
        pmps_test_root_dir = p # noqa

    result = targeted_pytest(
        target_directory=args.test_path,
        pytest_args=unknown_args,
        pytest_plugins=None
    )

    return result


if __name__ == "__main__":
    main()
