from flask import Flask, render_template, redirect, session, request, url_for, flash
from game_map import game_engine

# CONFIGURATION
DEBUG = True
SECRET_KEY = '\xbd\x01\xe4\xcf\xa1\x0f\x8d\xcd'

app = Flask(__name__)
app.config.from_object(__name__)


class GameError(Exception):
    pass


@app.route('/')
def home_page():
    session['scene.name'] = 'the pit'
    scene = session['scene.name']
    return render_template("home.html", scene=scene)

@app.route('/play/<name>', methods=['GET', 'POST'])
def play_game(name):
    if session['scene.name'] and request.method == 'POST':
        previous_scene = game_engine.get_scene(session['scene.name'])
        session_name = game_engine.handle_scene(request.form['action'])
        if session_name not in previous_scene.legal_paths:
            flash("you cant go there from this scene, try again.......")
            session['scene.name'] = session['scene.name']
            print("cow")
            print(session['scene.name'])
            print("cow")
            return redirect(url_for('play_game', name=session['scene.name']))
        else:
            session['scene.name'] = session_name
            print("cow")
            print(session['scene.name'])
            print("cow")
            return redirect(url_for('play_game', name=session['scene.name']))
    print(session['scene.name'])
    current_scene = game_engine.get_scene(session['scene.name'])
    return render_template('play.html', scene=current_scene)

if __name__ == "__main__":
    app.run()
