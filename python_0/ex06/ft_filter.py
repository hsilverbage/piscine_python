def ft_filter(function, iterable):
    '''Note that filter(function, iterable) is equivalent to the generator
    expression (item for item in iterable if function(item)) if function is
    not None and (item for item in iterable if item) if function is None.
    https://docs.python.org/3/library/functions.html#filter'''

    if function is not None:
        return (item for item in iterable if function(item))
    return (item for item in iterable if item)
