import json
from pathlib import Path

import inflection
from copier import copy

from horn.path import get_location


def run(opts):
    bindings = {
        'target': opts.get('<target>'),
        'from': convert_path(opts.get('<from>')),
        'checkout': opts.get('<checkout>'),
        'app': 'app',
        'proj': inflection.camelize(opts.get('<target>').split('/')[-1]),
        'file': opts.get('--file')
    }

    if bindings.get('file'):
        with open(bindings.get('file')) as f:
            conf = json.load(f)
            check_conflict(conf)
            bindings.update(conf)

    opt_json = json.loads(opts.get('--json'))
    check_conflict(opt_json)
    bindings.update(opt_json)

    location = get_location(bindings)
    try:
        copy(f'{location}/new', bindings.get('target'), data=bindings, exclude=['*/__pycache__/*'])
    except ValueError as err:
        print(f'Error: {err}')


def convert_path(path):
    rv = path
    if not (path.startswith('http') or path.startswith('git@') or path.startswith('ssh://')):
        rv = str(Path(path).resolve())
    return rv


def check_conflict(opt):
    """
    >>> check_conflict({'app': 'foobar'})
    >>> try:
    ...     check_conflict({'from': 'bbb'})
    ... except:
    ...     pass
    Error: Conflict field found, {from: bbb}
    """
    reserved_words = ["target", 'from', 'checkout', 'file']
    for rw in reserved_words:
        if rw in opt:
            print(f'Error: Conflict field found, {{{rw}: {opt.get(rw)}}}')
            exit(1)
