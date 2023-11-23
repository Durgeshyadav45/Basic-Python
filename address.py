# json Example

book = {}
book['amit'] = {
    'name': 'amit',
    'address': 'lucknow',
    'phone': 9089089
}
book['ankit'] = {
    'name': 'ankit',
    'address': 'kanpur',
    'phone': '6734782'
}

import json
s=json.dumps(book)
print(s)