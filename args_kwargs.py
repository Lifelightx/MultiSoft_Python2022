# def add(*args):
#     for item in args:
#         print(item)
#
#     print(args)
#
# add(1,2,['a','b'])

def calculate(**kwargs):
    for item in kwargs.values():
        print(item)

    print(kwargs)

calculate(num1=1, num2=3)