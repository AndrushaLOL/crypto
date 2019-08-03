import os

DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///app.sqlite'