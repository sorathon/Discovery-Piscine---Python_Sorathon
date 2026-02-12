def find_the_redheads(family):
    return list(filter(lambda name: family[name] == "red", family.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virgile": "brunette",
    "david": "red",
    "franck": "red",
}

print(find_the_redheads(dupont_family))
