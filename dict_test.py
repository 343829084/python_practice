
class Dict(dict):

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

class MyStruct(object):
    """docstring for MyStruct"""
    def __init__(self):
        super(MyStruct, self).__init__()
        self.name = ''
        self.sex = 'male'


d = Dict()
for i in range(4):
    myKey = MyStruct()
    myKey.name = str(i)
    if (i % 2 == 0):
        myKey.sex = 'female'
    d[myKey] = i
    print(d[myKey])