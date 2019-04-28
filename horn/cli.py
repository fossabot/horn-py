"""\t\t\033[1;33mHorn: A Flask scaffolding tool.\033[0m

Usage:
  horn new <folder> [<repo>]
                    ([--app=<app> --proj=<proj> --pypi=<pypi> --bare]
                     | [--checkout=<ref>] [--json=<json>]
                       [-f=PATH | --file=PATH])
  horn gen (api | service) <service> <module> <table> <fields>...
  horn gen model <module> <table> <fields>...
  horn gen schema <module> <fields>...
  horn (-h | --help)
  horn --version

Options:
  --app=<app>               App name [default: app].
  --proj=<proj>             Project name.
  --pypi=<pypi>             Pypi domain [default: pypi.org].
  --bare                    Bare project.
  --repo=<repo>             Git repo url.
  --checkout=<ref>          Git branch, tag or ref.
  --json=<json>             Json string [default: {}].
  -f=PATH, --file=PATH      Json file PATH.

  -h, --help                Show this screen.
  --version                 Show version.

Examples:
  horn \033[34mnew\033[0m tmp/foo_bar \033[32m--app\033[0m foobar \033[32m--proj\033[0m FooBar
  horn \033[34mnew\033[0m tmp/foo_bar \033[32m--repo\033[0m git@some.repo \033[32m--json\033[0m '{"app":"someapp"}' \033[32m-f\033[0m conf.json
  horn \033[34mgen api\033[0m Blog Post posts \033[36mtitle:string:uniq content:string:null author:ref:users\033[0m
  horn \033[34mgen service\033[0m Blog Post posts \033[36mtitle:string:uniq content:string:null author:ref:users\033[0m
  horn \033[34mgen model\033[0m Post posts \033[36mtitle:string:uniq content:string:null author:ref:users\033[0m
  horn \033[34mgen schema\033[0m Post \033[36mtitle:string content:string author:nest:user\033[0m

"""
from docopt import docopt
from . import impl


__version__ = '0.1.0'

ACTION_MAP = {
    'new': ['<folder>', '--app', '<repo>', '--proj', '--bare', '--pypi', '--checkout', '--json', '--file'],
    'api': ['<service>', '<module>', '<table>', '<fields>'],
    'service': ['<service>', '<module>', '<table>', '<fields>'],
    'model': ['<module>', '<table>', '<fields>'],
    'schema': ['<module>', '<fields>'],
}

ACTIONS = list(ACTION_MAP.keys())


class Hub(object):

    @classmethod
    def filter_opts(cls, action, params):
        keys = ACTION_MAP.get(action)
        return {k: v for k, v in params.items() if k in keys}

    @classmethod
    def run(cls, args):
        for action in ACTIONS:
            if args.get(action):
                opts = cls.filter_opts(action, args)
                getattr(impl, action).run(opts)
                break


def main():
    args = docopt(__doc__, version=f'Horn {__version__}')
    Hub.run(args)
