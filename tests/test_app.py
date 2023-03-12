from src.app import home

def test_home():
    assert home() == "Hello, World!"
