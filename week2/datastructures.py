Data1 = (7, False, "Apple", True, 7, 98.6)
print(len(Data1))
print(Data1[3])
print(Data1.count(7))

Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}
Data2.pop()
Data2.add("Alpha")
print(Data2)

Data3 = ["A", 7, -1, 3.14, True, 7]
Data3.reverse()
Data3[2] = 'B'
Data3.pop()
print(Data3)

Data4 = {
    "name": "Joe",
    "age": 26,
    "active": True,
    "hourly_wage": 14.75
}

Data4.update({"active": False})
Data4.setdefault("address", "123 West Main Street")
Data4.setdefault("weekly_hours", 40)
if Data4.get("weekly_hours") >= 40:
    print(Data4.get("weekly_hours") * Data4.get("hourly_wage") )
print(Data4)