# Tiny Notes CLI

A local notes list in one Python file. It exists so the [worked example](../tiny-brief.md) has a real, small repository to inspect. It is not a product, and it does not use the network.

## Run

Python 3.9+ and the standard library are enough.

```bash
python notes.py add "buy milk"
python notes.py list
python notes.py done 1
```

Notes are stored in `notes.json` next to `notes.py`. Pass `--file some.json` to use another path.

## Test

```bash
python -m unittest test_notes.py
```
