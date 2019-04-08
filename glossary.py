from collections import OrderedDict

glossary = OrderedDict()
glossary = {
    'print': "Print something on screen.",
    'for': "Start a loop.",
    'del': "Delete something.",
    'if': "Conditional statement",
    'in': "Check if value is in something.",
    'elif': "Else if.",
    }

for word, definition in glossary.items():
    print(word + ": " + definition)
