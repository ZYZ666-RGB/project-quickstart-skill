#!/usr/bin/env python3
"""Keep a tiny local note list in a JSON file.

Teaching fixture for the project-quickstart skill. Standard library only.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "notes.json"


def load_notes(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_notes(path: Path, notes: list[dict]) -> None:
    path.write_text(json.dumps(notes, indent=2) + "\n", encoding="utf-8")


def next_id(notes: list[dict]) -> int:
    if not notes:
        return 1
    return max(int(note["id"]) for note in notes) + 1


def cmd_add(path: Path, text: str) -> int:
    notes = load_notes(path)
    note = {"id": next_id(notes), "text": text, "done": False}
    notes.append(note)
    save_notes(path, notes)
    print(f"added #{note['id']}")
    return 0


def cmd_list(path: Path) -> int:
    notes = load_notes(path)
    if not notes:
        print("no notes")
        return 0
    for note in notes:
        mark = "x" if note.get("done") else " "
        print(f"{note['id']}. [{mark}] {note['text']}")
    return 0


def cmd_done(path: Path, note_id: int) -> int:
    notes = load_notes(path)
    for note in notes:
        if int(note["id"]) == note_id:
            note["done"] = True
            save_notes(path, notes)
            print(f"done #{note_id}")
            return 0
    print(f"no note #{note_id}", file=sys.stderr)
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Keep a tiny local note list in JSON.")
    parser.add_argument(
        "--file",
        type=Path,
        default=DEFAULT_PATH,
        help="JSON file to read and write (default: notes.json next to this script)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="Append a note")
    add.add_argument("text", help="Note text")

    sub.add_parser("list", help="Print every note")

    done = sub.add_parser("done", help="Mark a note done by id")
    done.add_argument("id", type=int, help="Note id")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "add":
        return cmd_add(args.file, args.text)
    if args.command == "list":
        return cmd_list(args.file)
    return cmd_done(args.file, args.id)


if __name__ == "__main__":
    raise SystemExit(main())
