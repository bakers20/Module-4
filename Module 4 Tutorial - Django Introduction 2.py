# 1. Create a directory for the project and navigate to it
$ mkdir djangogirls
$ cd djangogirls

# 2. Set up a virtual environment (Windows)
$ python -m venv myvenv

# Set up a virtual environment (Linux/MacOS)
$ python3 -m venv myvenv

# 3. Activate the virtual environment
# On Windows:
$ myvenv\Scripts\activate

# On Linux/MacOS:
$ source myvenv/bin/activate

# 4. Upgrade pip (in the virtual environment)
(myvenv) $ python -m pip install --upgrade pip

# 5. Create a `requirements.txt` file to specify dependencies
# File content for `requirements.txt`:
Django~=4.2.11

# 6. Install the dependencies listed in `requirements.txt`
(myvenv) $ pip install -r requirements.txt

# 7. Create a new Django project in the current directory
# On Windows:
(myvenv) C:\Users\Name\djangogirls> django-admin.exe startproject mysite .

# On Linux/MacOS:
(myvenv) ~/djangogirls$ django-admin startproject mysite .

# Your project directory structure should now look like this:
# djangogirls/
# ├── manage.py
# ├── mysite/
# │   ├── asgi.py
# │   ├── __init__.py
# │   ├── settings.py
# │   ├── urls.py
# │   └── wsgi.py
# ├── myvenv/
# └── requirements.txt

# 8. Update project settings in `mysite/settings.py`:
# Set the correct timezone
TIME_ZONE = 'Europe/Berlin'  # Update with your timezone

# Set the language code
LANGUAGE_CODE = 'de-ch'  # Update based on your language

# Add static files path
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Add allowed hosts for deployment (e.g., PythonAnywhere, Glitch)
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.pythonanywhere.com']

# 9. Set up the SQLite3 database
# The default setup in `settings.py` is fine:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 10. Run database migrations
(myvenv) $ python manage.py migrate

# 11. Start the web server (on Linux/MacOS):
(myvenv) ~/djangogirls$ python manage.py runserver

# Start the web server (on Windows):
(myvenv) C:\Users\Name\djangogirls> python manage.py runserver 0:8000

# 12. Open the web server in a browser at:
# http://127.0.0.1:8000/
