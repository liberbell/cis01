from collections import OrderedDict

d = {"apple": 5, "peers": 2, "orange": 8}
print(d)
print(d["peers"])
d["peer"] = 12
d["nabana"] = 4
print(d)

od = OrderedDict()
od["apple"] = 5
od["peer"] = 2
od["orange"] = 8
print(od["peer"])

od["banana"] = 12
print(od)