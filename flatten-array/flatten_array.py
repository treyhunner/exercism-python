from collections import Iterable


def flatten_gen(iterable):
    """Yield all non-None, items from all iterables in order."""
    for item in iterable:
        if item is None:
            continue  # Skip None values... why?  Who knows!
        # don't flatten strings to avoid infinite recursion
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten_gen(item)
        else:
            yield item


def flatten(iterable):
    return list(flatten_gen(iterable))
