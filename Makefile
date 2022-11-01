flake8:
	cd backend && flake8 --max-line-length=120 --select BLK --exclude migrations --exclude venv ./

mypy:
	cd backend && mypy apps
	cd backend && mypy config

pylint:
	cd backend && export PYTHONPATH=. && pylint apps

test:
	cd backend && pytest

coverage:
	cd backend && coverage run --source='./apps' -m pytest
	cd backend && coverage html

safety:
	cd backend && safety check -r requirements/base.txt --ignore 39642

bandit:
	cd backend && bandit -c bandit.yaml -r config
	cd backend && bandit -c bandit.yaml -r apps

fix:
	isort backend/conftest.py
	isort backend/manage.py
	isort backend/apps
	isort backend/config
	black backend/conftest.py
	black backend/manage.py
	black backend/apps
	black backend/config

clean:
	rm -rf backend/.mypy_cache
	rm -rf backend/.pytest_cache
	rm -rf backend/htmlcov

# full: fix flake8 mypy pylint safety bandit coverage
full: fix flake8 mypy safety bandit coverage