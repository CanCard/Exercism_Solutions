def append(list1, list2):
    list1 = list1 + list2
    return list1


def concat(lists):
    list1 = []
    for i in lists:
        if isinstance(i, list):
            for k in i:
                list1 += [k]
        else:
            list1 += [k]
    return list1
                


def filter(function, list):
    list1= []
    for i in list:
        if function(i) == True:
            list1 = list1 +[i]
    return list1


def length(list):
    sayac = 0
    for i in list:
        sayac = sayac + 1
    return sayac


def map(function, list):
    result = []
    for i in list:
        result += [function(i)]
    return result


def foldl(function, list, initial):
    for i in list:
        initial = function(initial, i)
    return initial


def foldr(function, list, initial):
    for i in list[::-1]:
        initial = function(initial, i)
    return initial


def reverse(list):
    l = []
    for i in list:
        l.insert(0,i)
    return l
