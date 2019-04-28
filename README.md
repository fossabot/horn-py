### Horn: A Flask scaffolding tool.

```console

Usage:
  horn new <folder> [<repo>]
                    ([--app=<app> --proj=<proj> --pypi=<pypi> --bare]
                     | [--checkout=<ref>] [--json=<json>]
                       [-f=PATH | --file=PATH])
  horn gen (api | service) <service> <module> <table> <fields>...
  horn gen model <module> <table> <fields>...
  horn gen schema <module> [<fields>...] [--model=<model>]
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

  --model=<model>           Schema baseed on model.

  -h, --help                Show this screen.
  --version                 Show version.


```