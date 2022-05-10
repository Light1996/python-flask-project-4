"""This allows Gunicorn to serve the app in production"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
