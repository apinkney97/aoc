import os


def load_data(day):
    with open(os.path.join('data', 'day{:02d}.data'.format(day))) as f:
        return [l.strip() for l in f.readlines()]
