from collections import OrderedDict

class FILOOrderDict(OrderedDict):
    def __init__(self, capacity):
        super(FILOOrderDict, self).__init__()
        self.capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        OrderedDict.__setitem__(self, key, value)
        if (len(self) > self.capacity) :
            first = self.popitem(last=True)
            print("remove item ", first)



d = FILOOrderDict(3)
d['A'] = 100
d['B'] = 200
d['C'] = 300
d['D'] = 400
d['E'] = 500

print(d)