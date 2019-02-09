from sprint_b import app
from sprint_b.helpers import EpithetGenerator as Epgen
from sprint_b.helpers import Vocabulary as Vocab
import flask
import os

"""Root path changes for running debugger locally
and using flask"""
try:
    ROOT_PATH = os.environ["EPITHET_ROOT"]
except KeyError:
    ROOT_PATH = '../../'
resourse_path = os.path.join(ROOT_PATH, 'resources/')
json_path = resourse_path + 'data.json'


@app.route('/')
@app.route('/<int:quantity>')
def generate_epithet(quantity=1):
    return flask.jsonify(Epgen.multiple_epithets(json_path, quantity))


@app.route('/vocabulary')
def vocabulary():
    # return str(Epgen.multiple_epithets(json_path))
    all_vocab = Vocab.from_file(json_path)[0]
    return flask.jsonify(all_vocab)
