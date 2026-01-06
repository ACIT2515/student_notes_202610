"""File reading demonstration showing common patterns for text file processing.

This module demonstrates:
- Opening and reading files with context managers
- Different methods for reading file content (readlines, iteration)
- Stripping whitespace from strings
- Using sets to find unique values
- Sorting results

References:
    - Reading and Writing Files:
        https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    - File Objects: https://docs.python.org/3/glossary.html#term-file-object
    - String Methods: https://docs.python.org/3/library/stdtypes.html#string-methods
    - Set Types: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
"""

import os


def read_with_readlines(filename: str) -> list[str]:
    """Read all lines from a file using readlines() method.

    The readlines() method reads the entire file and returns a list
    of strings, where each string is a line from the file.
    Lines include the newline character \\n at the end.

    Args:
        filename: Path to the file to read.

    Returns:
        A list of strings, one per line in the file.
    """
    # Context manager (with statement) ensures file is properly closed
    # even if an error occurs
    with open(filename, "r") as file_obj:
        # readlines() returns a list of all lines
        lines = file_obj.readlines()

    return lines


def read_with_iteration(filename: str) -> list[str]:
    """Read lines from a file using file iteration.

    File objects are iterable - you can loop over them directly.
    This is memory efficient for large files as it reads one line
    at a time instead of loading the entire file into memory.

    Args:
        filename: Path to the file to read.

    Returns:
        A list of strings, one per line in the file.
    """
    lines = []

    with open(filename, "r") as file_obj:
        # Iterate over file object directly - reads one line at a time
        for line in file_obj:
            lines.append(line)

    return lines


def count_non_empty_lines(filename: str) -> int:
    """Count the number of non-empty lines in a file.

    Empty lines are lines that contain only whitespace characters
    (spaces, tabs, newlines). We use strip() to remove whitespace
    and check if anything remains.

    Args:
        filename: Path to the file to read.

    Returns:
        The number of non-empty lines in the file.
    """
    count = 0

    with open(filename, "r") as file_obj:
        for line in file_obj:
            # strip() removes leading and trailing whitespace
            # including newline characters (\n, \r\n)
            if line.strip() != "":
                count += 1

    return count


def main() -> None:
    """Demonstrate file reading techniques.

    Uses the sample data file (ingredients.txt) to demonstrate
    various file reading operations.
    """
    print("File Reading Demonstration")
    print("=" * 50)
    print()

    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Sample file in the same directory
    filename = "ingredients.txt"
    filepath = os.path.join(script_dir, filename)

    # Check if file exists before processing
    if not os.path.exists(filepath):
        print(f"\nFile not found: {filename}")
        print("Please ensure the sample data file exists in the same directory.")
        return

    print("\nDemonstrating with sample file:")
    print("=" * 50)
    print(f"\n--- Processing: {filename} ---")

    # Demonstrate reading with readlines()
    print("\n1. Reading with readlines():")
    lines = read_with_readlines(filepath)
    print(f"   Third Line: {lines[2]}")
    print(f"   Total lines (including empty): {len(lines)}")

    # Demonstrate reading with iteration
    print("\n2. Reading with iteration:")
    lines_iter = read_with_iteration(filepath)
    print(f"   Third Line: {lines_iter[2]}")
    print(f"   Total lines (including empty): {len(lines_iter)}")

    # Count non-empty lines
    print("\n3. Counting non-empty lines:")
    count = count_non_empty_lines(filepath)
    print(f"   Non-empty lines: {count}")
    print(f"   Empty or whitespace-only lines: {len(lines) - count}")


if __name__ == "__main__":
    main()
