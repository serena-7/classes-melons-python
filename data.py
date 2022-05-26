# Melons
#
# fields are:
#
# species, color, is-imported (else is domestic), shape, seasons

melons = [
    ('Watermelon', 'green', False, False, 'natural', [
     'Fall', 'Summer'], {'amount': 3, 'percent': .75}),
    ('Cantaloupe', 'tan', False, False, 'natural', [
     'Spring', 'Summer'], {'amount': 5, 'percent': .50}),
    ('Casaba', 'green', True, True, 'natural', [
     'Spring', 'Summer', 'Fall', 'Winter'], None),
    ('Sharlyn', 'tan', True, False, 'natural', ['Summer'], None),
    ('Santa Claus', 'green', True, False,
     'natural', ['Winter', 'Spring'], None),
    ('Christmas', 'green', False, False, 'natural', ['Winter'], None),
    ('Horned Melon', 'yellow', True, False, 'natural', ['Summer'], None),
    ('Xigua', 'black', True, 'square', False, ['Summer'], None),
    ('Ogen', 'tan', False, 'natural', False, ['Spring', 'Summer'], None)
]
