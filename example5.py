#!/usr/bin/env python3

# Copyright 2014 Brett Slatkin, Pearson Education Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
