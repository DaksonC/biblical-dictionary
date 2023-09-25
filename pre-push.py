import subprocess
import sys

tests = ["pipenv run python manage.py test words.tests.test_models",
         "pipenv run python manage.py test words.tests.test_seralizers", "pipenv run python manage.py test words.tests.test_viewsets"]

for test in tests:
    subprocess.check_call(test.split())

sys.exit(0)
