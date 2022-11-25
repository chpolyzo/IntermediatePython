import csv
import json
neo_csv_path = "./data/neos.csv"
cad_json_path = "./data/cad.json"

from models import NearEarthObject, CloseApproach

def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos_values = []
    
    with open(neo_csv_path) as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            # print(row[3], row[4], row[15], row[7])
            neos_values.append(NearEarthObject(row[3], row[4], row[15], row[7]))
        return neos_values


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    cad_values = []
    with open(cad_json_path) as f:
        cad_data = json.load(f)
        cad_elements = cad_data['data']
        for row in cad_elements:
            # print(row[0], row[3], row[4], row[7])
            cad_values.append(CloseApproach(row[0], row[3], row[4], row[7]))
        
    return cad_values

def createNeosKeys(neo_csv_path):
    """Reads a csv file path and returns a list of feature names
    aka labels to be used as python dictionary keys"""
    try:
        f = open(neo_csv_path, 'r')
        neos_labels = next(f).split(',') # first line of the file

    finally:
        f.close()
        
        labels = neos_labels[3], neos_labels[4], neos_labels[15], neos_labels[7]
        return list(labels)


def createCadKeys(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    
    with open(cad_json_path) as f:
        
        cad_data = json.load(f)
        cad_keys = cad_data['fields']
        labels = cad_keys[0], cad_keys[3], cad_keys[4], cad_keys[8] 

        
    return list(labels)
