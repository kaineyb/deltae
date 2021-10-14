from deltae import __version__

current_version = "1.1.0"


def test_version():
    """Check Version in deltae/__init__.py"""
    assert __version__ == current_version


def test_toml_version():
    """Check Version in pyproject.toml"""
    import toml
    from pathlib import Path

    pyproject_toml = Path("pyproject.toml")

    with open(pyproject_toml, "r") as f:

        my_toml = toml.load(f)
        version = my_toml["tool"]["poetry"]["version"]
        print(version)

    assert version == current_version
