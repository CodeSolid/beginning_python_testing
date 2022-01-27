"""greeter module contains one testable function"""

def greet(name: str = None) -> str:
    """greet is a hello world style function to have something to test."""
    if name is None:
        return "Hello, World!"
    else:
        return f"Hello, {name}!"
