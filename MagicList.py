class MagicList:

    def __init__(self, cls_type=None):
        if not cls_type:
            self.vals = [0]  # assuming a list is created with length >= 1
        else:
            self.vals = [cls_type()]

    def __getitem__(self, key):
        return self.vals[key]

    def __setitem__(self, key, value):
        self.vals[key] = value

    def __str__(self):
        return str(self.vals)

    def append(self, val):
        self.vals.append(val) # todo - test

    def __len__(self):
        return len(self.vals) # todo - test
