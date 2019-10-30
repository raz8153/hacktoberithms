contacts = [
    {
        "firstName": "Akira",
        "lastName": "Laine",
        "number": "0543236543",
        "likes": ["Pizza", "Coding", "Brownie Points"]
    },
    {
        "firstName": "Harry",
        "lastName": "Potter",
        "number": "0994372684",
        "likes": ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "0487345643",
        "likes": ["Intriguing Cases", "Violin"]
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["JavaScript", "Gaming", "Foxes"]
    }
]


def look_up_profile(name, field):
    for i in contacts:
        if i["firstName"] == name and i.get(field) != None:
            return i[field]
        elif i.get(field) == None:
            return "NO SUCH PROPERTY"
    return "NO SUCH CONTACT"


# Change these values to test your function
print(look_up_profile("Akira", "likes"))