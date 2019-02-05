from sprint_b import app
from sprint_b.helpers import EpithetGenerator as Epgen
from sprint_b.helpers import Vocabulary as Vocab
from pathlib import PurePath as Path
import json
import os

p = Path(os.getcwd())
project_root = str(p.parent.parent)
json_path = os.path.join(project_root+'/resources', 'data.json')
file_path = os.path.join(project_root+'/resources', 'data.csv')


@app.route('/')
@app.route('/<int:quantity>')
def generate_epithet(quantity=1):
    return Epgen.multiple_epithets(json_path, quantity)


@app.route('/vocabulary')
def vocabulary():
    # return str(Epgen.multiple_epithets(json_path))
    all_vocab = json.dumps(Vocab.from_file(json_path)[0])
    return all_vocab
