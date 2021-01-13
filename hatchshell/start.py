# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Start hatching a shell as required."""

from __future__ import annotations

from logging import INFO as INFO_LOG_LEVEL

from hatchshell.spidermonkey.hatch import SpiderMonkeyShell
from hatchshell.util.logging import get_logger

RUN_LOG = get_logger(__name__)
RUN_LOG.setLevel(INFO_LOG_LEVEL)


def main() -> None:
    """Start hatching a shell."""
    # Support SpiderMonkey and JavaScriptCore
    # Check prerequisites, fail early.
    # dpkg for debian/ubuntu: https://askubuntu.com/questions/423355/how-do-i-check-if-a-package-is-installed-on-my-server
    # emerge -p firefox for gentoo: https://forums.gentoo.org/viewtopic-t-855048-start-0.html
    # Homebrew for macOS, ?? for Windows
    # Check hg/git trees present

    # if shell_type == "spidermonkey":
    # try
    # shell = SpiderMonkeyShell()
    SpiderMonkeyShell()

    # Should these be within SpiderMonkeyShell??
    # sm_shell.prereqs.check()  # Should call os.check() and repo.check()

    # # argparse to accept parameters for build_options, possibly randomizing. Not priority yet
    # sm_shell.compile("--enable-debug and other standard options")  # configuration and compilation here
    # sm_shell.verify()  # Consider using binaryornot
    # sm_shell.delete_objdir()
    # return the full path to the compiled binary
    # except: propagate error code up

    # elif shell_type == "javascriptcore":
    #     # try
    #     jsc_shell = javascriptcore.hatch.JavaScriptCoreShell()
    #     jsc_shell.prereqs.check()  # Should call os.check() and repo.check()

    #     # argparse to accept parameters for build_options, possibly randomizing. Not priority yet
    #     jsc_shell.compile("--enable-debug and other standard options")  # configuration and compilation here
    #     jsc_shell.verify()  # Consider using binaryornot
    #     jsc_shell.delete_objdir()
    #     # return the full path to the compiled binary
    #     # except (propagate error code up)

    # shell.compile()
    # RUN_LOG.info("Path to: %s", shell.get_absolute_path())
    # Consider generating sphinx documentation


if __name__ == "__main__":
    # Ideally main() should return 1 or 0 depending on how the compilation turned out.
    # sys.exit(main())
    main()
