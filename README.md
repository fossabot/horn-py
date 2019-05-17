
# ![flask](chili.png)  Horn: A Flask scaffolding tool

[![PyPI - License](https://img.shields.io/pypi/l/horn-py.svg)](https://mit-license.org)
[![PyPI](https://img.shields.io/pypi/v/horn-py.svg)](https://pypi.org/project/horn-py)


## Installation

```console
$ pip install horn-py
```


## Usage

```text

Usage:
  horn new <target> [--app=<app> --proj=<proj> --pypi=<pypi> --bare]
  horn new <target> <from> [<checkout>] [--json=<json>] [-f=PATH | --file=PATH]
  horn gen api <module> <table> <fields>...
  horn gen model <module> <table> <fields>...
  horn gen schema <module> (<fields>... | --model=<model> | <fields>...  --model=<model>)
  horn (-h | --help)
  horn --version

Options:
  --app=<app>               App name [default: app].
  --proj=<proj>             Project name.
  --pypi=<pypi>             Pypi domain [default: pypi.org].
  --bare                    Bare project.

  --json=<json>             Json string [default: {}].
  -f=PATH, --file=PATH      Json file PATH.

  --model=<model>           Schema baseed on model.

  -h, --help                Show this screen.
  --version                 Show version.

```
