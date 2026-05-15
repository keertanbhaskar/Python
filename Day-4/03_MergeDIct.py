dict1 = {"keerti":23,"shama":22}
dict2 = {"shreya":22,"kavi":34}

merge = dict1 | dict2
print(merge)

dict3 = {"keerti":23,"shama":22}
merge2 = {**dict3,**dict2}
print(merge2)