import json
import os

request_parameter_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'\\data\Request_parameter.json'

def get_json(path,kw = ''):
    with open(path,'r',encoding = 'utf-8') as f:
        data_json = json.load(f)
        if kw:
            data = data_json.get(kw)
            return data
        else:
            return data_json









if __name__ == '__main__':
    get_json(request_parameter_path)
