import sys

from chemistry_validator import validate_dataset


def main():
    """Run dataset validation from the command line."""

    if len(sys.argv) != 2:
        print("Usage: python validate_dataset.py <csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    errors = validate_dataset(file_path)

    if errors:
        for error in errors:
            print(error)

        print("\nValidation status: FAILED")
        sys.exit(1)

    print("Validation status: PASSED")
    sys.exit(0)


if __name__ == "__main__":
    main()