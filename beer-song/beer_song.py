from textwrap import dedent


def verse(n):
    if n == 2:
        lyrics = f"""
        {n} bottles of beer on the wall, {n} bottles of beer.
        Take one down and pass it around, {n-1} bottle of beer on the wall.
        """
    elif n == 1:
        lyrics = f"""
        {n} bottle of beer on the wall, {n} bottle of beer.
        Take it down and pass it around, no more bottles of beer on the wall.
        """
    elif n == 0:
        lyrics = f"""
        No more bottles of beer on the wall, no more bottles of beer.
        Go to the store and buy some more, 99 bottles of beer on the wall.
        """
    else:
        lyrics = f"""
        {n} bottles of beer on the wall, {n} bottles of beer.
        Take one down and pass it around, {n-1} bottles of beer on the wall.
        """
    return dedent(lyrics).lstrip()


def song(start=99, end=0):
    return "\n".join(
        verse(n)
        for n in range(start, end-1, -1)
    ) + "\n"
