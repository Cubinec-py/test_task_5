# This repo just for test task
### First, need to create and asset .env file in the root directory.
```dotenv
SECRET_KEY=
```
Activate virtual environment and install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 pip install -r requirements.txt
```
Before start project need to init migrations:
```bash
python3 manage.py migrate --settings=core.settings.local
```
To create superuser(optional):
```bash
python3 manage.py createsuperuser --settings=core.settings.local
```
To start project:
```bash
python3 manage.py runserver --settings=core.settings.local
```