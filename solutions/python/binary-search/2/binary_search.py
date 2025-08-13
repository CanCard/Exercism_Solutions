def find(search_list, value):
    found = False
    first = 0
    last = len(search_list) - 1
    while found == False and first <= last:
        mid = (first + last) // 2
        if search_list[mid] == value:
            found = True
            return mid
        else:
            if value < search_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found == False:
        raise ValueError("value not in array")