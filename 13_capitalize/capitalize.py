def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

   #  easy way -->
   #  return phrase.capitalize()

   #  Longer way
    return phrase[:1].upper() + phrase[1:]