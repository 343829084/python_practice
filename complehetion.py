#coding=utf-8
#

def list_complehetion():
    multiples=[i for i in range(30) if i % 2 == 0]
    print(multiples)
    listTest=[i**2 for i in range(5)]
    print(listTest)
    list2={i**2 for i in [1,1,2]}
    print(list2)
    fruit = ['apple', 'banana', 'orange']
    dictresult = {key: value for key, value in enumerate(fruit) if len(value) > 5}
    print(dictresult)

def operator_file():
    try:
        with open('test.txt', 'rb') as file:
            data = file.read()
    except IOError as e:
        print("An error occurred.")
        raise e
    else:
        pass
    finally:
        pass

def lambda_test():
    add = lambda x, y : x+y
    print(add(4, 6))
    for i in range(2, 100):
        print(i)



if __name__ == '__main__':
    #list_complehetion()
    lambda_test()