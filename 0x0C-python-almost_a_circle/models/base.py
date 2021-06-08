#!/usr/bin/python3
'''
Almost a circle project
Holberton program
'''
import json
import csv

class Base:
    '''
    Base class of the project
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Instantiatior
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        returns the JSON string representation
        of list_dictionaries
        '''
        if list_dictionaries and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        '''
        returns the list of the JSON
        string representation json_string
        '''
        if json_string and json_string != '':
            return json.loads(json_string)
        else:
            return list()

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation
        of list_objs to a file
        '''
        new_list = []
        if list_objs and len(list_objs) > 0:
            str = ''
            for item in list_objs:
                new_list.append(item.to_dictionary())
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(Base.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        '''
        Returns an instance with all attributes
        already set according to dictionary
        '''
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
        Return a list of instances
        '''
        new_list = list()
        try:
            with open(cls.__name__ + '.json', 'r') as f:
                file_string = f.read()
                ins_list = Base.from_json_string(file_string)
                for item in ins_list:
                    new_list.append(cls.create(**item))
                return new_list
        except Exception:
            return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        serializes in CSV
        '''
        new_list = []
        with open(cls.__name__ + '.csv', 'w') as f:
            if list_objs and len(list_objs) > 0:
                if cls.__name__ == 'Rectangle':
                    header = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    header = ['id', 'size', 'x', 'y']

                writer = csv.DictWriter(f, header)
                writer.writeheader()
                for item in list_objs:
                    writer.writerow(item.to_dictionary())
            else:
                file.write('[]')

    @classmethod
    def load_from_file_csv(cls):
        '''
        deserializes from CSV
        '''
        new_list = list()
        try:
            with open(cls.__name__ + '.csv', 'r', newline='') as csvf:
                freader = csv.reader(csvf)
                for row in freader:
                    new_list.append(cls.create(**row))
                return new_list
        except Exception:
            return new_list
