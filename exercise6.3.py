
glossary = {"variable": "A name that stores a value in a program.", "string": "A series of characters, written inside quotes.", "list": "An ordered collection of items that can be changed.",
    "loop": "A structure that repeats a block of code.",
    "dictionary": "A collection of key-value pairs.",}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")