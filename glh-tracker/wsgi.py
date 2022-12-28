from flaskwebgui import FlaskUI

from app import create_app

app = create_app()

if __name__ == "__main__":
    FlaskUI(app=app, width=800, height=600, fullscreen=True,
            server="flask").run()
