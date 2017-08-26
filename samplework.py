filename = "soumya1543sarath"


def getstring(filename):
    result = ""
    for f in filename:
        if (f.isdigit() == False):
            result = result + f
    return result

print(getstring(filename))
