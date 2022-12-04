search_request = {
  'type': 'object',
  'properties': {
    'search_type': {'type': 'string'},
    'payload': {'type': 'string'},
  },
  'required': ['search_type', 'payload'],
}

checkout_request = {
  'type': 'object',
  'properties': {
    'products': {
      'type': 'array',
      'items': {
        'type': 'object',
        'properties': {
          'barcode_id': {'type': 'string'},
          'quantity': {'type': 'number'},
        },
        'required': ['barcode_id', 'quantity'],
      },
    },
    'discount': 'number',
  },
  'required': ['products'],
}