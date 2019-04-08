def city_country(city, country):
    message = '"' + city + ', ' + country + '"'
    return message


message = city_country('Santiago', 'Chile')
print(message)

message = city_country('Osaka', 'Japan')
print(message)

message = city_country('Eindhoven', 'The Netherlands')
print(message)
