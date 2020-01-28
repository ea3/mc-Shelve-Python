import shelve
with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "253 Dream"
    bike["color"] = "Red"
    bike["engine_size"] = 250

    for key in bike:
        print(key)

    print("++++++++++++++++++")

    print(bike["engine_size"])
    print(bike["color"])



