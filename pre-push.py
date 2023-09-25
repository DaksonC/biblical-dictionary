import subprocess
import sys

tests = ["pipenv run python manage.py test words.tests.test_integration"]

for test in tests:
    subprocess.check_call(test.split())

sys.exit(0)
