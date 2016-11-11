def hey(what):
    if not what.strip():
        return 'Fine. Be that way!'
    if what.isupper():
        return 'Whoa, chill out!'
    elif what.endswith('?'):
        return 'Sure.'
    else:
        return 'Whatever.'
