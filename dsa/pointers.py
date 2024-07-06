a = {"aa":10}
b = a
print(f"a before change {a}")
print(f"b before change {b}")
print(f"a id before change {id(a)}")
print(f"b id before change {id(b)}")

b={"bb":22}

print(f"a after change {a}")
print(f"b after change {b}")
print(f"a id after change {id(a)}")
print(f"b id after change {id(b)}")