import os
import json
import random


class FileManager:
    """Handle the local file system IO """

    @staticmethod
    def get_extension(path):
        """Get file extension from file path """
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode='r', *args, **kwargs):
        """Reads json data"""
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)


class Vocabulary:
    """ Standardized vocabulary representation from multiple sources. """

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        """Finds and runs appropriate handle to run depending on file type"""
        extension = cls.files.get_extension(path)
        representation = cls._strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def _from_json(cls, path, fields=True, *args, **kwargs):
        """Returns info from json file provided"""
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            representation = (data, data.keys())
        else:
            representation = data
        return representation

    @classmethod
    def _strategies(cls, file_extension, intent='read'):
        """Returns function based on given extension """
        input_strategies = {'json': cls._from_json}
        if intent is 'read':
            return input_strategies[file_extension]


class EpithetGenerator:
    """Returns desired epithet info"""
    vocab = Vocabulary()

    @classmethod
    def single_rand_epithet(cls, path):
        """Creates and returns single random insult """
        column_dict = cls.vocab.from_file(path)[0]
        epithet = []
        for column in column_dict:
            epithet.append(random.choice(column_dict[column]))
        return epithet

    @classmethod
    def multiple_epithets(cls, path, quantity):
        """Returns defined number of insults"""
        epithets = {}
        for i in range(quantity):
            epithets[i+1] = cls.single_rand_epithet(path)
        return epithets
