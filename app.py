from flask import Flask

website_wide_message = None

def create_app():
    app = Flask(__name__, template_folder="pages")
    app.secret_key = "test123$1"
    app.app_context()

    # app.jinja_env.globals.update(len=len)

    from pages.login.login import Login
    from pages.dashboard.dashboard import Dashboard
    from pages.leaderboard.leaderboard import Leaderboard

    app.register_blueprint(Login, url_prefix="/")
    app.register_blueprint(Dashboard, url_prefix="/")
    app.register_blueprint(Leaderboard, url_prefix="/")

    return app

if __name__ == "__main__":
    create_app().run()