d = [
    {
        'surname': 'Zhapar',
        'id': '19B030307'
    },
    {
        'surname': 'Ashim',
        'id': '19B030307'
    },
    {
        'surname': 'Ernat',
        'id': '21B21893040'
    }
]

# print(*sorted(d, key=lambda x: x['id'][:3]))
print(*sorted(d, key=lambda x: (x['id'][:3], x['surname'])))
