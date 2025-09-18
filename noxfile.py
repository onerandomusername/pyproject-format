"""Configure nox."""

import nox

NOX_SESSION = nox.session(python=False)


@NOX_SESSION
def fix(session: nox.Session):
    """Fix files inplace."""
    session.run("ruff", "format", "-s", ".")
    session.run("ruff", "check", "-se", "--fix", ".")


@NOX_SESSION
def lint(session: nox.Session):
    """Check file formatting that only have to do with formatting."""
    session.run("ruff", "format", "--check", ".")
    session.run("ruff", "check", ".")


@NOX_SESSION
def typecheck(session: nox.Session):
    session.run("mypy", "-p", "pyproject_format")


@NOX_SESSION
def tests(session: nox.Session):
    session.run("pytest", "tests", *session.posargs)


@NOX_SESSION
def coverage(session: nox.Session):
    session.run(
        "pytest",
        "--cov",
        "pyproject_format",
        "--cov-report",
        "term-missing",
        "tests",
    )
