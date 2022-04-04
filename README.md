# API DELIVERY FLASK                                                        

Description. API for delivery building with framework flask 
using an application factory pattern

Use the package manager pip to install 
run Make.sh
install:
	pip install -e .['dev']

init_db:
	FLASK_APP=delivery/app.py flask create-db
	FLASK_APP=delivery/app.py flask db upgrade

test:
	FLASK_ENV=test pytest tests/ -v --cov=delivery


Usage
run:
	FLASK_APP=delivery/app.py FLASK_ENV=development flask run

Author
Ali Rios

License
GNU Affero General Public License v3.0
