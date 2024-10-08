# CONNECT Core API

## Dev guide

### App setup


pyenv install 3.12.0

python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate
or 
venv\Scripts\activate

# Install poetry
pip install poetry

# Install project dependencies
poetry install

# Update environment variables in `.env`
cp .env.default .env

# Create a superadmin
python core/manage.py createsuperuser

# Run the dev server
python core/manage.py runserver

# Go to admin & login with superuser creds
http://localhost:8000/admin

# Create a new OAuth application
  * Select client type: "Confidential"
  * Select authorization grant type: "Resource owner password-based"
  * Type name
  * Copy client key & client secret for future use
  * Save

 
# Fake the migrations for the defined apps
python3.12 core/manage.py makemigrations api api_auth
python3.12 core/manage.py migrate api --fake
python3.12 core/manage.py migrate api_auth --fake


# Run the migrations for the third-party apps in Django settings
python3.12 core/manage.py migrate

