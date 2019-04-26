from copier import copy

from pampy import match, _, TAIL


TYPES = {
    'integer': 'Integer',
    'float': 'Float',
    'decimal': 'Decimal',
    'boolean': 'Boolean',
    'string': 'String',
    'text': 'Text',
    'date': 'Date',
    'time': 'Time',
    'datetime': 'DateTime',
    'uuid': 'UUID',
    'json': 'JSON',
    'array': 'ARRAY',
    'ref': 'reference'
}


def run(opts):
    bindings = {
        'service': opts.get('<service>'),
        'module': opts.get('<module>'),
        'table': opts.get('<table>'),
        'fields': parse_fields(opts.get('<fields>'))
    }

    bindings.update(opts)
    print(bindings)


def validate_type(arg):
    if arg not in TYPES:
        print(f'field type error: {arg}')
        exit(1)
    return TYPES.get(arg)


def validate_tail(*args):
    affix = ['uniq', 'null']
    for arg in args:
        if arg not in affix:
            print(f'fields type error: {":".join(args)}')
            exit(1)

    return dict(zip(args, [True for i in args]))


def compose_field(base, affix={}):
    base.update(affix)
    return base


def parse_fields(fields):
    attrs = [f.split(':') for f in fields]
    return [match(attr,
                [_, _],              lambda x, y: {'field': x, 'type': validate_type(y)}, # noqa
                [_, 'ref', _],       lambda x, table: {'field': x, 'type': validate_type('ref'), 'table': table},  # noqa
                [_, 'ref', _, TAIL], lambda x, table, t: compose_field({'field': x, 'type': validate_type('ref'), 'table': table}, validate_tail(*t)),  # noqa
                [_, _, TAIL],        lambda x, y, t: compose_field({'field': x, 'type': validate_type(y)}, validate_tail(*t))  # noqa
    ) for attr in attrs]
