import json


def CheckInDicts(dictionary):
    global MaxDepth
    global TestDepth
    #print("CheckInDicts called")
    tstdict={}
    tstlst=[]
    for key in dictionary:
        if type(dictionary.get(key)) is type(tstdict):                             #if dictionary in dictionary: ...
            #print(dictionary.get(key))
            TestDepth=TestDepth+1
            CheckInDicts(dictionary.get(key))
        if type(dictionary.get(key)) is type(tstlst):
            #print(dictionary.get(key))
            TestDepth=TestDepth+1
            CheckInList(dictionary.get(key))
    if TestDepth>MaxDepth:
        MaxDepth=TestDepth
    TestDepth=0


def CheckInList(List):
    global MaxDepth
    global TestDepth
    tstdict={}
    tstlst=[]
    #print("CheckInList called")
    for element in List:
        if type(element) is type(tstdict):
            #print(element)
            TestDepth=TestDepth+1
            CheckInDicts(element)
        if type(element) is type(tstlst):
            #print(element)
            TestDepth=TestDepth+1
            CheckInList(element)
    if TestDepth>MaxDepth:
        MaxDepth=TestDepth
    TestDepth=0


NameOfFile=input('Give the file name: ')
with open(NameOfFile) as f:
    data=f.read()
dict = json.loads(data)
MaxDepth=0
TestDepth=0
CheckInDicts(dict)
print('The Maximum depth is: ',MaxDepth)
