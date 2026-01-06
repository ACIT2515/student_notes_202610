import argparse
import json
import os
import shutil
from pathlib import Path

from link_map import LinkMap


def restore_symlinks(map_file: Path):
    """Restore symbolic links from a JSON map file.

    Replaces actual file/directory content with symbolic links based on the map.

    Args:
        map_file: Path to the JSON file containing link mappings

    Returns:
        int: Number of symlinks successfully restored
    """
    if not map_file.exists():
        print(f"Error: Map file '{map_file}' does not exist")
        return 0

    with open(map_file, "r") as f:
        data = json.load(f)

    link_map = LinkMap.from_json(data)

    for link in link_map.links:
        source_path = link.source
        target_path = link.target

        if not target_path.exists():
            print(f"Warning: Target '{target_path}' does not exist, skipping")
            continue

        if source_path.is_symlink():
            print(f"Info: '{source_path}' is already a symlink, skipping")
            continue

        try:
            # Remove existing content
            if source_path.exists():
                if source_path.is_file():
                    source_path.unlink()
                elif source_path.is_dir():
                    shutil.rmtree(source_path)

            # Create symlink
            source_path.symlink_to(target_path)

        except Exception as e:
            print(f"Error restoring {source_path}: {e}")

    return len(link_map.links)


def main():
    parser = argparse.ArgumentParser(
        description="Restore symbolic links from a JSON map file"
    )
    parser.add_argument("map_file", help="JSON file containing symbolic link mappings")

    args = parser.parse_args()

    if not os.path.exists(args.map_file):
        print(f"Error: Map file '{args.map_file}' does not exist")
        return 1

    count = restore_symlinks(Path(args.map_file))
    print(f"\nRestored {count} symbolic link(s)")

    return 0


if __name__ == "__main__":

    exit(main())
