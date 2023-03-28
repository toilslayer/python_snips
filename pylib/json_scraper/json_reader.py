import json

def get_json_keys(json_data,depth):
    keys=[]
    for jd in json_data:
        keys.append(jd)
        for sjd in json_data[jd]:
            keys.append(sjd)
            if isinstance(json_data[jd][sjd], dict) and depth > 0:
                get_json_keys(data[jd][sjd],depth - 1)
                    
    print(keys)

json_list = json.loads('{"sa1":{"name": "John", "age": 30}, "sa2":{"name": "Jane", "age": 25}}')
# get_json_keys(json_list)

def get_all_keys(data, depth):
    keys=[]
    for jd in data:
        keys.append(jd)
        for sjd in data[jd]:
            keys.append(sjd)
            if isinstance(data[jd][sjd], dict) and depth > 0:
                get_all_keys(data[jd][sjd], depth - 1)
    print(keys)

# json_list = json.loads('{"sa1":{"name": "John", "container": "Main","files": {"filename": "blah.txt"}}}')
# json_list = json.loads('{"sa1": "FirstSA","Container": "cont1","file1": {"name": "John", "age": 30}}')
# , "file2":{"name": "Jane", "age": 25}
# json_list = json.loads('{"sa1":{"name": "John", "age": 30}, "sa2":{"name": "Jane", "age": {"test": "value"}}}')
get_all_keys(json_list, 3)
