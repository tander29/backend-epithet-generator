from sprint_b.helpers import FileManager as fm
from sprint_b.helpers import Vocabulary as Vocab
from sprint_b.helpers import EpithetGenerator as epgen
from pathlib import PurePath as Path
import os
p = Path(os.getcwd())
project_root = str(p.parent.parent)

json_path = os.path.join(project_root+'/resources', 'data.json')
file_path = os.path.join(project_root+'/resources', 'data.csv')


def test_fm_get_extension():
    path = 'thisstuff.txt'
    path2 = 'thisstuff.json'
    path3 = 'thisstuff.csv'
    assert fm.get_extension(path) == 'txt'
    assert fm.get_extension(path2) == 'json'
    assert fm.get_extension(path3) == 'csv'


def test_fm_read_json():
    returned_json = fm.read_json(json_path)
    print(type(returned_json))
    assert type(returned_json) == dict
    assert len(returned_json.keys()) == 3


def test_vocab_from_file():
    representation = Vocab.from_file(json_path)
    vocab_data = representation[0]
    assert type(representation) == tuple
    assert type(vocab_data) == dict
    assert len(vocab_data.keys()) == 3


def test_vocab_from_json():
    representation = Vocab._from_json(json_path)
    assert type(representation) == tuple
    assert type(representation[0]) == dict
    assert len(representation[0]) == 3


def test_vocab_strategies():
    json_strategy = Vocab._strategies('json')
    assert json_strategy.__name__ == '_from_json'


def test_epithet_random():
    words = epgen.single_rand_epithet(json_path)
    assert type(words) == list
    assert len(words) == 3


def test_epithet_multiple():
    quantity = 2
    assert type(epgen.multiple_epithets(json_path, quantity)) == dict
    assert len(epgen.multiple_epithets(json_path, quantity)) == quantity
