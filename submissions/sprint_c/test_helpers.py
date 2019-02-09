from sprint_b.helpers import FileManager as Fm
from sprint_b.helpers import Vocabulary as Vocab
from sprint_b.helpers import EpithetGenerator as Epgen
import pytest
from pathlib import PurePath as Path
import os
p = Path(os.getcwd())
project_root = str(p.parent.parent)

json_path = os.path.join(project_root+'/resources', 'data.json')
csv_path = os.path.join(project_root+'/resources', 'data.csv')


def test_fm_get_extension():
    """Test FileManager extensions """
    path = 'thisstuff.txt'
    path2 = 'thisstuff.json'
    path3 = 'thisstuff.csv'
    assert Fm.get_extension(path) == 'txt'
    assert Fm.get_extension(path2) == 'json'
    assert Fm.get_extension(path3) == 'csv'


def test_fm_read_json():
    """Tests if reads json, if provided else raises error """
    returned_json = Fm.read_json(json_path)
    print(type(returned_json))
    assert type(returned_json) == dict
    assert len(returned_json.keys()) == 3
    with pytest.raises(Exception):
        Fm.read_json(csv_path)


def test_vocab_from_file():
    """Returns tuple if from file, curretly only works with json """
    representation = Vocab.from_file(json_path)
    vocab_data = representation[0]
    assert type(representation) == tuple
    assert type(vocab_data) == dict
    assert len(vocab_data.keys()) == 3
    with pytest.raises(Exception):
        # csv currently not in strategies
        Vocab.from_file(csv_path)


def test_vocab_from_json():
    """Specifically gets info from json """
    representation = Vocab._from_json(json_path)
    assert type(representation) == tuple
    assert type(representation[0]) == dict
    assert len(representation[0]) == 3
    with pytest.raises(Exception):
        Fm.read_json(csv_path)


def test_vocab_strategies():
    """Returns function of which data to grab based on extension """
    json_strategy = Vocab._strategies('json')
    assert json_strategy.__name__ == '_from_json'
    with pytest.raises(Exception):
        Fm.read_json(csv_path)


def test_epithet_random():
    """Returns a random epit if given proper path"""
    words = Epgen.single_rand_epithet(json_path)
    assert type(words) == list
    assert len(words) == 3


def test_epithet_multiple():
    """Returns given quantity of random epithets """
    quantity = 2
    assert type(Epgen.multiple_epithets(json_path, quantity)) == dict
    assert len(Epgen.multiple_epithets(
        json_path, quantity)) == quantity
