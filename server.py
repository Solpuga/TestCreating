from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask import Flask, render_template, redirect, make_response, request, session, abort, jsonify, make_response
from data import db_session
from data.users.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    app.run()


main()
