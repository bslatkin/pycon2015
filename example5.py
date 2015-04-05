#!/usr/bin/env python3

def normalize(population):
    total = sum(x for _, x in population)
    for city, count in population:
        percent = 100 * count / total
        yield city, percent

from example4 import load_cities_list, load_cities_generator

data = load_cities_list('population.tsv')
result = normalize(data)
print(next(result))
print(next(result))

#

import logging

data = load_cities_generator('population.tsv')
result = normalize(data)

try:
    print(next(result))
except StopIteration:
    logging.exception('Expected')

data = load_cities_generator('population.tsv')
result = normalize(data)
print(list(result))

#

class LoadCities(object):

    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path) as handle:
            for line in handle:
                city, count = line.split('\t')
                yield city, int(count)


data = LoadCities('population.tsv')
result = normalize(data)
print(next(result))
print(next(result))

#

def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must be a container')

    total = sum(x for _, x in numbers)
    for city, count in numbers:
        percent = 100 * count / total
        yield city, percent


data = load_cities_generator('population.tsv')
result = normalize_defensive(data)
try:
    print(next(result))
except TypeError:
    logging.exception('Expected')


data = LoadCities('population.tsv')
result = normalize_defensive(data)
print(next(result))
