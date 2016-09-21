class student(object):
    def showMsg(self, myTeacher, name, age):
        myTeacher(name, age)


class teacher(object):
    def __init__(self):
        msg(conten)

    def conten(self, name, age):
        print("name=%s, age=%d"%(name, age))


    def msg(self, method):
        method()


a = student()
myteacher = teacher()
a.showMsg(myteacher.conten, "gary", 20)
