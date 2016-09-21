import sys

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


if __name__ == '__main__':
    greet_me(sys.argv[1:])
