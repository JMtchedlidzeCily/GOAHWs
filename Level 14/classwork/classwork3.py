list1 = ["GOA", 2058, 205.8, True, "Is good"]
print(list1[-5])
print(list1[-4])
print(list1[-3])
print(list1[-2])
print(list1[-1])

list1 = ["GOA", 2058, 205.8, True, "Is good"]
a = list1[-4]
list1[-4] = list1[-1]
list1[-1] = a
print(list1)
