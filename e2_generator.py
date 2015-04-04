#!/usr/bin/env python3

def load_cities_generator(path):
    with open(path) as handle:
        for line in handle:
            city, count = line.split('\t')
            yield city, int(count)


if __name__ == '__main__':
    result = load_cities_generator('population.tsv')
    print(next(result))
    print(next(result))
    print(next(result))
