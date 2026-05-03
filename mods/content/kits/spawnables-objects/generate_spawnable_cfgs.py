#!/usr/bin/env python3
from pathlib import Path
import re

ASSET_CATEGORY = "spawnables"


def slug_to_title(slug: str) -> str:
    """
    Converts filenames like:
    dog-tag
    dog_tag
    dog tag

    into:
    Dog Tag
    """
    words = re.split(r"[-_\s]+", slug.strip())
    return " ".join(word.capitalize() for word in words if word)


def make_cfg_content(slug: str) -> str:
    title = slug_to_title(slug)

    return f"""[asset]
name = "{title}"
key = "{slug}"
asset_category = "{ASSET_CATEGORY}"
"""


def main() -> None:
    root = Path.cwd()

    for tscn_path in sorted(root.glob("*.tscn")):
        slug = tscn_path.stem
        cfg_path = root / f"{slug}.cfg"

        if cfg_path.exists():
            print(f"Skipping existing: {cfg_path.name}")
            continue

        cfg_path.write_text(make_cfg_content(slug), encoding="utf-8")
        print(f"Created: {cfg_path.name}")


if __name__ == "__main__":
    main()
