class MagicList:

    def __init__(self, cls_type=None, vals=None):
        # supporting initial assingment operation
        # vals must be iterable
        if not cls_type:
            self.vals = []  # assuming a list is created with length >= 1
        else:
            self.vals = [cls_type()]
        if vals:
            for val in vals:
                self.append(val)

    def __getitem__(self, key):
        return self.vals[key]

    def __setitem__(self, key, value):
        if not self.vals and key == 0:
            self.vals.append(value)
        else:
            self.vals[key] = value

    def clear(self):
        self.vals.clear()

    def __str__(self):
        return str(self.vals)

    def append(self, val):
        self.vals.append(val)

    # def count(self):
    #     todo

    def extend(self, other):
        self.vals.extend(other)

    def index(self, element, start=None, end=None):
        if start and end:
            return self.vals.index(element, start, end)
        if start:
            return self.vals.index(element, start)
        if end:
            return self.vals.index(element, end=end)
        return self.vals.index(element)

    def pop(self):
        self.vals.pop()

    def insert(self, index, element):
        self.vals.insert(index, element)

    def __len__(self):
        return len(self.vals)  # todo - test

# current list of unsupported actions
# (mainly due to time and I didn't feel like they were the main point of the assingmnet)

# Python List copy()
# Python List reverse()
# Python List sort()
#
# Python List insert()
# insert an element to the list
#
# Python List remove()
# Removes item from the list
