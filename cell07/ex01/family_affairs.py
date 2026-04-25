def find_redheads(family):
    redheads = filter(lambda item: item[1] == "red", family.items())
    return list(map(lambda item: item[0], redheads))

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_redheads(dupont_family))