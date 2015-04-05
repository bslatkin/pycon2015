#!/usr/bin/env python3

from pprint import pprint

def load_cities_list(path):
    result = []
    with open(path) as handle:
        for line in handle:
            city, count = line.split('\t')
            result.append((city, int(count)))
    return result


result = load_cities_list('population.tsv')
pprint(result)

#

def load_cities_generator(path):
    with open(path) as handle:
        for line in handle:
            city, count = line.split('\t')
            yield city, int(count)


result = load_cities_generator('population.tsv')
print(next(result))
print(next(result))
print(next(result))
