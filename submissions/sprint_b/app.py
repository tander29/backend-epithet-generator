from sprint_b import app
from sprint_b.helpers import EpithetGenerator as epgen
from pathlib import PurePath as Path
import os

p = Path(os.getcwd())
project_root = str(p.parent.parent)
json_path = os.path.join(project_root+'/resources', 'data.json')
file_path = os.path.join(project_root+'/resources', 'data.csv')


@app.route('/')
def generate_epithets():
    return str(epgen.single_rand_epithet(json_path))


@app.route('/vocabulary')
def vocabulary():
    # return str(epgen.multiple_epithets(json_path))
    all_vocab = str(epgen.multiple_epithets(json_path))
    return all_vocab
