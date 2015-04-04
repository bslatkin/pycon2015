#!/usr/bin/env python3

def load_cities_list(path):
    result = []
    with open(path) as handle:
        for line in handle:
            city, count = line.split('\t')
            result.append((city, int(count)))
    return result



if __name__ == '__main__':
    result = load_cities_list('population.tsv')
    print(result)
