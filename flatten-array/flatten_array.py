from collections import Iterable


def flatten_gen(iterable):
    """Yield all items from all iterables in order."""
    for item in iterable:
        # don't flatten strings to avoid infinite recursion
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten_gen(item)
        else:
            yield item


def flatten(iterable):
    return [
        item
        for item in flatten_gen(iterable)
        if item is not None  # Skip None values... why?  Who knows!
    ]
