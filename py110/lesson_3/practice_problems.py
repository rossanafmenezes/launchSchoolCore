import pdb


def test():
    print("Inside the function!")
pdb.set_trace()
print("Before function call")
test()
print("After function call")