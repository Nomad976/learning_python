def make_sandwich(*ingredients):
    print("\nMaking a sandwich with:")
    for ingredient in ingredients:
        print("- " + ingredient)


make_sandwich('pepperoni')
make_sandwich('cheese', 'sausage')
make_sandwich('lettuce', 'bbq sauce', 'cheese', 'beef')
