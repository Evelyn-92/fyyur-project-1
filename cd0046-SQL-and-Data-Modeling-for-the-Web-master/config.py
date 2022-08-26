import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'https://www.google.com/search?q=postgresql%3A%2F%2Fbanda%3AMARIAWILLNEVER%40localhost%3A5432%2Ffyyur&oq=postgresql%3A%2F%2Fbanda%3AMARIAWILLNEVER%40localhost%3A5432%2Ffyyur&aqs=chrome..69i57j69i58.112533j0j7&sourceid=chrome&ie=UTF-8'
