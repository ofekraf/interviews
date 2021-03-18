class MagicList:

    def __init__(self, cls_type=None):
        if not cls_type:
            self.vals = []  # assuming a list is created with length >= 1
        else:
            self.vals = [cls_type()]

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
        self.vals.append(val) # todo - test

    def __len__(self):
        return len(self.vals) # todo - test



# for now not overriding the assignment operator as this was not
# explicitly requested,