from flask import Flask, render_template, redirect, session, request, url_for, flash
from spy_quest.game_map import game_engine

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
    scene = game_engine.get_scene('the pit')
    return render_template("home.html", scene=scene)


@app.route('/play', methods=['GET', 'POST'])
def play():
    if session['scene.name'] and request.method == 'POST':
        previous_scene = game_engine.get_scene(session['scene.name'])
        if request.form['action'] in previous_scene.legal_paths:
            session['scene.name'] = request.form['action']
            return redirect(url_for('play'))
        else:
           flash("you cant go there from this scene, try again.......")
           return redirect(url_for('play'))
    scene = game_engine.get_scene(session['scene.name'])
    return render_template('play.html', scene=scene)


if __name__ == "__main__":
    app.run()
