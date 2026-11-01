glossary = { "variable": "A name that stores a value in a program.",
    "string": "A series of characters, written inside quotes.",
    "list": "An ordered collection of items that can be changed.",
    "loop": "A structure that repeats a block of code.",
    "dictionary": "A collection of key-value pairs.",
    "tuple": "An ordered collection of items that cannot be changed.",
    "function": "A named block of code that performs a specific task.",
    "boolean": "A value that is either True or False.",
    "integer": "A whole number without a decimal point.",
    "comment": "A note in the code that Python ignores when running.",}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")