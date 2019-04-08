favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")

people = ['erin', 'sarah', 'tommy', 'phil']

for name in people:
    if name in favourite_languages.keys():
        print(name.title() + ", thank you for taking the poll.")
    else:
        print(name.title() + ", you should take our poll!")
