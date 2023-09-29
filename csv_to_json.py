# This script reads csv file and convert it into json

import csv
import json


csv_filepath = '/home/file.csv'



def csv_to_dict(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data


csv_data = csv_to_dict(csv_filepath)



with open("/home/file.json", "w") as f:
    json_object = json.dumps(csv_data, indent=4)
    f.write(json_object)
    
