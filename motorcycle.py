import shelve
with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "253 Dream"
    bike["color"] = "Red"
    bike["engine_size"] = 250

    print(bike["engine_size"])
    print(bike["color"])

