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

import logging

try:
    flow = flow_rate(
        weight_diff, time_diff)
    assert False
except TypeError:
    logging.exception('Expected')


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
