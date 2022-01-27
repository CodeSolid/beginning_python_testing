# Use this to clear the python cache files if tests won't refresh
find . | grep -E "(.pytest_cache|__pycache__|\.pyc|\.pyo$)" | xargs rm -rf