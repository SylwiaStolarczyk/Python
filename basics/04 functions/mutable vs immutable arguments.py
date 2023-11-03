#immutable int, float, bool, str, frozenset
#dodawanie do typów niemutowalnych tworzy całkowicie nowe miejsc w pamięci

def modifyStr(strData):
    print(id(strData))
    strData+= "!"
    print(id(strData))
    print(strData)

string = "Hello"

modifyStr(string)

#mutable types: list, set, dict
#w wyniku modyfikowania nie zostanie utworzona nowa wartość

def modifyList(listData):
    print(id(listData))
    listData.append(10)
    print(id(listData))
    return listData

listValue = [0,1,2]

print(id(listValue))
modifyList(listValue)