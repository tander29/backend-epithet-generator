from sprint_c import app
from sprint_c.helpers import EpithetGenerator as Epgen
from sprint_c.helpers import Vocabulary as Vocab
from random import randint
import flask
import os

try:
    ROOT_PATH = os.environ["EPITHET_ROOT"]
except KeyError:
    ROOT_PATH = '../../'
resourse_path = os.path.join(ROOT_PATH, 'resources/')
json_path = resourse_path + 'data.json'


@app.route('/')
@app.route('/random')
@app.route('/<int:quantity>')
def generate_epithet(quantity=1, random=None):
    if flask.request.path == '/random':
        quantity = randint(1, 10)
    return flask.jsonify(Epgen.multiple_epithets(json_path, quantity))


@app.route('/vocabulary')
def vocabulary():
    # return str(Epgen.multiple_epithets(json_path))
    all_vocab = Vocab.from_file(json_path)[0]
    return flask.jsonify(all_vocab)
