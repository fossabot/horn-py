from pampy import match, _, TAIL
from copier import copy

from horn.naming import Naming
from horn.path import TPL_PATH, get_location
from horn.tpl import get_proj_info, validate_opts
from . import model, schema


TYPE_MAP = {
    'integer': 'integer',
    'float': 'float',
    'decimal': 'decimal',
    'boolean': 'boolean',
    'string': 'string',
    'date': 'date',
    'time': 'time',
    'datetime': 'datetime',
    'uuid': 'uuid',

    'ref': 'ref',
    'nest': 'nest',

    'array': 'list'
}


def run(opts):
    model.run(opts)
    sch_opts = opt_pipe(opts)
    schema.run(sch_opts)

    validate_opts(opts)

    bindings = {
        'service': opts.get('<service>'),
        'module': opts.get('<module>'),
        'mod': Naming.underscore(opts.get('<module>')),
        'singular': Naming.underscore(opts.get('<service>')),
        'table': opts.get('<table>'),
        'fields': opts.get('<fields>')
    }
    bindings.update(get_proj_info())

    location = get_location(bindings) or TPL_PATH
    copy(f'{location}/gen', '.', data=bindings,
         exclude=['*/models/*', '*/schemas/*', '*/views/*', 'test/*'])


def opt_pipe(opts):
    o = prepare_opts(opts)
    p = drop_assign(o)
    t = convert_type(p)
    s = ref_to_nest(t)
    return s


def prepare_opts(opts):
    rv = opts.copy()
    rv.update({
        '--model': opts.get('<module>')
    })
    return rv


def drop_assign(opts):
    opts['<fields>'] = [':'.join(match(
        field.split(':'),
        [_, _],        lambda x, y: [x, y],  # noqa
        [_, _, TAIL],  lambda x, y, t: [x, y] + drop_pair(t)  # noqa
    )) for field in opts['<fields>']]
    return opts


def drop_pair(attrs, key='default'):
    if key in attrs:
        idx = attrs.index(key)
        del attrs[idx:idx+2]    # noqa: E226
    return attrs


def convert_type(opts):
    opts['<fields>'] = [':'.join(match(
        field.split(':'),
        [_, _],        lambda x, y: [x, TYPE_MAP.get(y, 'string')],  # noqa
        [_, _, TAIL],  lambda x, y, t: [x, TYPE_MAP.get(y, 'string')] + t ,  # noqa
    )) for field in opts['<fields>']]
    return opts


def ref_to_nest(opts):
    opts['<fields>'] = [':'.join(match(
        field.split(':'),
        [_, 'ref', _],       lambda x, y: [x, 'nest', Naming.singular(y)],  # noqa
        [_, 'ref', _, TAIL], lambda x, y, t: [x, 'nest', Naming.singular(y)] + t,  # noqa
        list,                lambda x: x  # noqa
    )) for field in opts['<fields>']]
    return opts
