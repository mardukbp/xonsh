def as_iterable(iterable_or_scalar):
    """Utility for converting an object to an iterable.
   Parameters
   ----------
   iterable_or_scalar : anything
   Returns
   -------
   l : iterable
       If `obj` was None, return the empty tuple.
       If `obj` was not iterable returns a 1-tuple containing `obj`.
       Otherwise return `obj`
   Notes
   -----
   Although both string types and dictionaries are iterable in Python, we are treating them as not iterable in this
   method.  Thus, as_iterable(dict()) returns (dict, ) and as_iterable(string) returns (string, )
   Examples
   ---------
   >>> as_iterable(1)
   (1,)
   >>> as_iterable([1, 2, 3])
   [1, 2, 3]
   >>> as_iterable("my string")
   ("my string", )
   >>> as_iterable({'a': 1})
   ({'a': 1}, )
   """

    if iterable_or_scalar is None:
        return ()
    elif isinstance(iterable_or_scalar, string_types):
        return (iterable_or_scalar,)
    elif hasattr(iterable_or_scalar, "__iter__"):
        return iterable_or_scalar
    else:
        return (iterable_or_scalar,)
