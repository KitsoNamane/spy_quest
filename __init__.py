import flask
import map

# CONFIGURATION
DEBUG = True
SECRET_KEY = "flaky"

app = flask.Flask(__name__)
app.config.from_object(__name__)


class GameError(Exception):
    pass


@app.route('/')
def home_page():
    flask.session['scene.name'] = 'the pit'
    scene = map.game_engine.get_scene('the pit')
    return flask.render_template("home.html", scene=scene)


@app.route('/play', methods=['GET', 'POST'])
def play():
    if flask.session['scene.name'] and flask.request.method == 'POST':
        flask.session['scene.name'] = flask.request.form['action']
        return flask.redirect(flask.url_for('play'))
    scene = map.game_engine.get_scene(flask.session['scene.name'])
    return flask.render_template('play.html', scene=scene)


if __name__ == "__main__":
    app.run()
