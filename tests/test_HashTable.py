import pytest 
from data_structures.hashing import HashTable

@pytest.fixture
def table():
    return HashTable(size=10)

def test_insert_and_search_single_key(table):
    table.insert(3, "cat")
    assert table.search(3) == "cat"

def test_insert_different_types(table):
    table.insert(1, "bat")
    table.insert('a', "bee")
    table.insert(3.5, 4)
    table.insert("string", 5)

    assert table.search(1) == "bat"
    assert table.search('a') == "bee"
    assert table.search(3.5) == 4
    assert table.search("string") == 5

def test_update_existing_key_value(table):
    table.insert(5, "first")
    table.insert(5, "second")

    assert table.search(5) == "second"

def test_delete_existing_key(table):
    table.insert(6, 7)
    table.delete(6)

    assert table.search(6) == -1

def test_delete_nonexistant_key(table):
    table.delete(99)

    assert table.search(99) == -1

def test_collision(table):
    table.insert(7, 8)
    table.insert(17, 9)

    assert table.search(7) == 8
    assert table.search(17) == 9

def test_empty_search(table):
    assert table.search(0) == "Key not found"

def test_resize_trigger(table):
    for i in range(8): 
        table.insert(i, f"val{i}")
    assert table.size == 20


