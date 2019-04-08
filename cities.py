cities = {
    'osaka': {'country': 'japan', 'population': 2700000,
              'fact': 'my friend lives there', },
    'edinburgh': {'country': 'scotland', 'population': 507000,
                  'fact': 'Edinburgh Castle is built on an inactive volcano',
                  },
    'brighton': {'country': 'england', 'population': 156000,
                 'fact': "this city is home to England's oldest cinema", },
    }

for city, info in cities.items():
    print(city.title() + " is a city in " + info['country'].title() +
          ". It's population is approximately " + str(info['population']) +
          " people. Fun fact: " + info['fact'] + ".")
