import pytest
from libs.datastore import DataStore


@pytest.fixture()
def datastore_init():
    DataStore.init()


def test_datastore_list(datastore_init):
    expected = []
    assert DataStore.list_all() == expected


def test_datastore_insert(datastore_init):
    expected = [1, 2, 3]
    for num in expected:
        DataStore.insert(num)

    assert DataStore.list_all() == expected
