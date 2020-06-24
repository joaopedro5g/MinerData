import json
from datetime import date

with open('data.json') as json_file:
    data = json.load(json_file)
    i = 0
    today= date.today().strftime("%m/%d/%Y")
    today= today[:-4]+today[-2:]
    for p in data:
        i = i + 1
        if(str(p['date']) == str(today)):
            print('Name: ' + str(p['name']))
            print('Price: ' + str(p['money']))
    print('Register of {} length'.format(i))