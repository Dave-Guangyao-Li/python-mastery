from collections import namedtuple
import csv


def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records


class Row:
    # Uncomment to see effect of slots
    __slots__ = ('route', 'date', 'daytype', 'rides')

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


# Uncomment to use a namedtuple instead
# Row = namedtuple('Row', ('route', 'date', 'daytype', 'rides'))


def read_rides_as_instances(filename):
    '''
    Read the bus ride data as a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    read_rides = read_rides_as_instances
    # read_rides = read_rides_as_dicts
    # read_rides = read_rides_as_tuples
    rides = read_rides('../Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())

    """
    instance with __slots__ is the most efficient implementation
    Memory Use: Current 119068774, Peak 119099160
    """
