import argparse
import json
import os
import shutil
from pathlib import Path

from link_map import LinkData, LinkMap

SKIP = [".git", ".venv", ".pytest_cache", ".mypy_cache", ".ruff_cache"]


def get_symlinks(root: Path, exclude=None):
    """Recursively find all symbolic links in a directory tree.

    Args:
        root (Path): Root directory to search recursively
        exclude (list, optional): List of directory names to skip. Defaults to SKIP.

    Yields:
        Path: Each symbolic link found in the directory tree
    """
    for item in root.iterdir():
        if exclude and item.name in exclude:
            continue

        if item.is_symlink():
            yield item

        if item.is_dir():
            yield from get_symlinks(item, exclude)


def process_links(project_root: Path, map_file: Path, exclude=None):
    """
    Recursively find symbolic links in project path,
    Store link sources and targets as JSON in map_file,
    Replace symlinks with target data so they can be committed to git can manage it.

    Args:
        project_root: Root directory to search
        map_file: path to save JSON output

    Returns:
        LinkMap containing link information
    """

    link_map = LinkMap()
    links = get_symlinks(project_root, exclude)

    for link in links:
        target = link.resolve()
        source = link.absolute()
        link_map.add_link(LinkData(source=source, target=target))
        replace_link_w_content(source, target)

    with open(map_file, "w") as f:
        json.dump(link_map.to_json(), f, indent=2)

    return link_map


def replace_link_w_content(link_src: Path, link_target: Path):
    """Replace link with the content of target

    Args:
        link_path: Path to the symbolic link to replace

    Returns:
        bool: True if successful, False otherwise
    """
    if not link_src.is_symlink():
        print(f"Warning: {link_src} is not a symbolic link")
        return False

    if not link_target.exists():
        print(f"Error: Target {link_target} does not exist")
        return False

    # Remove the symbolic link
    link_src.unlink()

    try:
        if link_target.is_file():
            # Copy file content
            shutil.copy2(link_target, link_src)
        elif link_target.is_dir():
            # Copy directory tree
            shutil.copytree(link_target, link_src)
        return True

    except Exception as e:
        print(f"Error replacing {link_src}: {e}")

        # Try to restore the symlink
        link_src.symlink_to(link_target)

        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate a JSON map of symbolic links a directory tree"
    )
    parser.add_argument(
        "project_path", help="Root directory to search for symbolic links"
    )
    parser.add_argument(
        "map_file", nargs="?", default=None, help="Optional output JSON file path"
    )

    args = parser.parse_args()

    if not os.path.exists(args.project_path):
        print(f"Error: Path '{args.project_path}' does not exist")
        return 1

    link_map = process_links(Path(args.project_path), args.map_file, SKIP)

    # Print results if no map_file specified
    if not args.map_file:
        print(json.dumps(link_map.to_json(), indent=2))
    else:
        print(f"Found {len(link_map.links)} symbolic link(s). Saved to {args.map_file}")

    return 0


if __name__ == "__main__":
    exit(main())
