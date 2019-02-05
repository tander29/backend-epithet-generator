from sprint_b.helpers import FileManager as Fm
from sprint_b.helpers import Vocabulary as Vocab
from sprint_b.helpers import EpithetGenerator as Epgen
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
    assert Fm.get_extension(path) == 'txt'
    assert Fm.get_extension(path2) == 'json'
    assert Fm.get_extension(path3) == 'csv'


def test_fm_read_json():
    returned_json = Fm.read_json(json_path)
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
    words = Epgen.single_rand_epithet(json_path)
    assert type(words) == list
    assert len(words) == 3


def test_epithet_multiple():
    quantity = 2
    assert type(Epgen.multiple_epithets(json_path, quantity)) == dict
    assert len(Epgen.multiple_epithets(
        json_path, quantity)) == quantity
