import re

def new_func():
    regex_pattern = r"\d+"
    data = {"orders":[{"id":1},
                  {"id":2},
                  {"id":3},
                  {"id":4},
                  {"id":5},
                  {"id":6},
                  {"id":7},
                  {"id":8},
                  {"id":9},
                  {"id":10},
                  {"id":11},
                  {"id":648},
                  {"id":649},
                  {"id":650},
                  {"id":651},
                  {"id":652},
                  {"id":653}],
                  "errors":[
                      {"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"
                       }
                       ]
                       }
    for key, values in data.items():
        if key=='orders':
            numbers = re.findall(regex_pattern, str(values))
            return numbers

data = new_func()
print(data)


# output => ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '648', '649', '650', '651', '652', '653']
