import os

from flask_template.app import create_app

os.environ["PROJECT_DIRECTORY"] = os.path.dirname(__file__)

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
