import os


def load_data(day, strip=True):
    with open(os.path.join("data", f"day{day:02d}.data")) as f:
        if strip:
            return [l.strip() for l in f.readlines()]
        return f.readlines()
