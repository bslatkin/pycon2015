#!/usr/bin/env python3

def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)

print('%.3f kg per second' % flow)

#

def flow_rate(weight_diff, time_diff, period, units_per_kg):
    return (
        weight_diff
        / units_per_kg
        / time_diff
        * period)


flow = flow_rate(
    weight_diff, time_diff,
    period=3600, units_per_kg=2.2)

print('%.3f lbs per hour' % flow)

#

flow = flow_rate(
    weight_diff, time_diff,
    period=1, units_per_kg=1)


def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return (
        weight_diff
        / units_per_kg
        / time_diff
        * period)

kgs_per_second = flow_rate(
    weight_diff, time_diff)

print(kgs_per_second)

lbs_per_hour = flow_rate(
    weight_diff, time_diff,
    period=3600, units_per_kg=2.2)

print(lbs_per_hour)
