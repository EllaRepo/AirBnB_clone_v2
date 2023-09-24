#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown
    """
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Function called with '/states/<id>' route
    """
    states = storage.all(State)
    if not id:
        dict_to_html = {value.id: value.name for value in states.values()}
        return render_template('7-states_list.html',
                               Table="States",
                               items=dict_to_html)

    key = "State." + id
    if key in states:
        return render_template('9-states.html',
                               Table="State: {}".format(states[key].name),
                               items=states[key])

    return render_template('9-states.html',
                           items=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
