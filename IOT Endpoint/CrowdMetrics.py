# Parses Azure response + counts people
def countPeople(objects):
    personCount = 0
    for object in objects:
        if object.object_property == "person":
            personCount += 1
    return personCount