class PrintList(object):

    def __init__(self, my_list):
        self.mylist = my_list

    def __repr__(self):
        return str(self.mylist)


printlist = PrintList(["a", "b", "c"])
print(printlist.__repr__())  # Output: ["a", "b", "c"]
# just 'print(printlist)' works the same because __repr__() defines how to represent object
print(printlist)
