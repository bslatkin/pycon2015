#!/usr/bin/env python3

def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


log('My numbers are', [1, 2])
log('Hi there', [])

#

def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

log('My numbers are', [1, 2])
log('Hi there', [])

log('My numbers are', 1, 2)
log('Hi there')

#

favorites = [7, 33, 99]
log('Favorite numbers', *favorites)

# TODO
# def explode(i=0):
#     while True:
#         yield i
#         i += 1

# log('All numbers in existence', *explode())
