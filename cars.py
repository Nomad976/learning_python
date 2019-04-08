def describe_car(manufacturer, model, **information):
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in information.items():
        car[key] = value
    return car


my_car = describe_car('Subaru', 'Outback', colour='blue', tow_package=True)
print(my_car)
