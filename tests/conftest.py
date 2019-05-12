import pytest

from hgvs.parser import Parser


@pytest.fixture(scope="session")
def parser():
    return Parser()
