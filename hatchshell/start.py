# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Start hatching a shell as required."""

import logging

from hatchshell.spidermonkey.hatch import SpiderMonkeyShell

RUN_LOG = logging.getLogger("run_log")
logging.basicConfig(
    format="%(asctime)s %(name)-8s %(levelname)-8s {%(module)s} [%(funcName)s] %(message)s",
    datefmt="%m-%d %H:%M:%S", level=logging.INFO,
)
logging.getLogger("flake8").setLevel(logging.ERROR)


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
    shell = SpiderMonkeyShell()

    # Should these be within SpiderMonkeyShell??
    # sm_shell.prereqs.check()  # Should call os.check() and repo.check()

    # # argparse to accept parameters for build_options, possibly randomizing. Not priority yet
    # sm_shell.compile("--enable-debug and other standard options")  # configuration and compilation here
    # sm_shell.verify()  # Consider using binaryornot
    # sm_shell.delete_objdir()
    # return the full path to the compiled binary
    # except (propagate error code up)

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

    shell.compile()
    # RUN_LOG.info("Path to: %s", shell.get_absolute_path())
    # Generate sphinx documentation
    # Consider putting it in github.io?


if __name__ == "__main__":
    # Ideally main() should return 1 or 0 depending on how the compilation turned out.
    # sys.exit(main())
    main()
