#!/usr/bin/env python3


def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return (
        weight_diff
        / units_per_kg
        / time_diff
        * period)

weight_diff = 0.5
time_diff = 3

oz_per_min = flow_rate(
    weight_diff, time_diff, 60, 35.274)

oz_per_min = flow_rate(
    weight_diff, time_diff, 35.274, 60)

#

def flow_rate(weight_diff, time_diff, *, period=1, units_per_kg=1):
    return (
        weight_diff
        / units_per_kg
        / time_diff
        * period)

import logging

try:
    oz_per_min = flow_rate(
        weight_diff, time_diff, 60, 35.274)
    assert False
except TypeError:
    logging.exception('Expected')

#

def flow_rate_py2(weight_diff, time_diff, **kwargs):

  period = kwargs.pop('period', 1)
  units_per_kg = kwargs.pop('units_per_kg', 1)
  if kwargs:
    raise TypeError('Unexpected: %r' % kwargs)

  return (
    weight_diff / units_per_kg
    / time_diff * period)

try:
    oz_per_min = flow_rate_py2(
        weight_diff, time_diff, 60)
    assert False
except TypeError:
    logging.exception('Expected')

try:
    oz_per_min = flow_rate_py2(
        weight_diff, time_diff, period=60, units_per_kg=2.2, extra=10)
    assert False
except TypeError:
    logging.exception('Expected')

#

def log(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))


log(1, 'Favorites', 7, 33)
log('Favorites', 7, 33)

#

from datetime import datetime

def log(message, *values, sequence=None):
    if sequence is None:
        sequence = datetime.utcnow()
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))

log('Favorites', 7, 33, sequence=1)
log('Favorites', 7, 33)
log('Favorites', 7, 33, 25)
