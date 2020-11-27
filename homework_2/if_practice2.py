def string_compare(string_1, string_2):
    if type(string_1) is not str or type(string_2) is not str:
        return 0
    elif string_1 == string_2:
        return 1
    elif string_1 != string_2 and len(string_1)>len(string_2):
        return 2
    elif string_1 != string_2 and string_2 == 'learn':
        return 3


print(string_compare(1,'dfd'))
print(string_compare('duble','duble'))
print(string_compare('dubleeeee','duble'))
print(string_compare('test','learn'))

