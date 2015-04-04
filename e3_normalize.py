#!/usr/bin/env python3

def normalize(numbers):
    total = sum(x for _, x in numbers)
    for city, count in numbers:
        percent = 100 * count / total
        yield city, percent


if __name__ == '__main__':
    from e1_list import *
    result = normalize(load_cities_list('population.tsv'))
    print('List:')
    print(list(result))

    from e2_generator import *
    result = normalize(load_cities_generator('population.tsv'))
    print('Generator:')
    print(next(result))
