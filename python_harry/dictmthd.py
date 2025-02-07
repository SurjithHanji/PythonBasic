ep1={
    122:45,123:69,124:45,125:67
}
ep2={
    101:61,102:67,103:68
}
ep1.update(ep2)
print(ep1)

ep1.pop(122)
print(ep1)

del ep1[123]
print(ep1)

ep1.clear()
print(ep1)


