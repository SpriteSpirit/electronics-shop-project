import pytest

from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard


@pytest.fixture
def item():
    return Item('', 0, 0)


@pytest.fixture
def phone():
    return Phone('', 0, 0, 0)


@pytest.fixture
def keyboard():
    return Keyboard('', 0, 0)
