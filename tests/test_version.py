from importlib.metadata import version

import deltae


def test_version():
    """Check deltae.__version__ matches installed package metadata"""
    assert deltae.__version__ == version("deltae")
