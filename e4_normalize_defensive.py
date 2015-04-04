#!/usr/bin/env python3


class LoadCities(object):
    def __init__(self, path):
        self.path = path
    def __iter__(self):
        with open(self.path) as handle:
            for line in handle:
                city, count = line.split('\t')
                yield city, int(count)


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    total = sum(x for _, x in numbers)
    for city, count in numbers:
        percent = 100 * count / total
        yield city, percent


if __name__ == '__main__':
    result = normalize_defensive(LoadCities('population.tsv'))
    print(next(result))
    print(next(result))

    from e2_generator import *
    result = normalize_defensive(load_cities_generator('population.tsv'))
    print(next(result))
