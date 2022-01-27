"""tests the myapp.greeter module"""

from myapp.greeter import greet

def test_greeter_returns_hello_world_if_no_name_provided():
    assert greet() == "Hello, World!"

def test_greeter_returns_hello_name_if_name_provided():
    assert greet("John") == "Hello, John!"
