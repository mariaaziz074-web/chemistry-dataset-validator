import pandas as pd


REQUIRED_COLUMNS = [
    "Material",
    "Dye",
    "Bandgap_eV",
    "Concentration_mg_L",
    "Time_min",
    "Rate_constant",
]

NUMERIC_COLUMNS = [
    "Bandgap_eV",
    "Concentration_mg_L",
    "Time_min",
    "Rate_constant",
]


def validate_dataset(file_path):
    """
    Validate a chemistry dataset.

    Returns:
        list[str]: Validation errors.
    """

    errors = []

    # 1. Read CSV
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return [f"ERROR: File not found: {file_path}"]
    except pd.errors.EmptyDataError:
        return [f"ERROR: CSV file is empty: {file_path}"]
    except Exception as exc:
        return [f"ERROR: Could not read CSV: {exc}"]

    # 2. Check empty dataset
    if df.empty:
        errors.append("ERROR: Dataset contains no rows.")
        return errors

    # 3. Check required columns
    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        return [
            f"ERROR: Missing required columns: {missing_columns}"
        ]

    # 4. Check missing values
    for column in REQUIRED_COLUMNS:
        missing_count = df[column].isna().sum()

        if missing_count > 0:
            errors.append(
                f"ERROR: {column} contains "
                f"{missing_count} missing value(s)"
            )

    # 5. Check duplicate rows
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        errors.append(
            f"ERROR: Dataset contains "
            f"{duplicate_count} duplicate row(s)"
        )

    # 6. Check numeric columns
    for column in NUMERIC_COLUMNS:
        numeric_values = pd.to_numeric(
            df[column],
            errors="coerce"
        )

        invalid_count = (
            numeric_values.isna() & df[column].notna()
        ).sum()

        if invalid_count > 0:
            errors.append(
                f"ERROR: {column} contains "
                f"{invalid_count} non-numeric value(s)"
            )

        # 7. Check non-finite values
        non_finite_values = numeric_values.isin(
            [float("inf"), float("-inf")]
        )
        non_finite_count = non_finite_values.sum()

        if non_finite_count > 0:
            errors.append(
                f"ERROR: {column} contains "
                f"{non_finite_count} non-finite value(s)"
            )

        # 8. Check negative values
        negative_rows = df[
            numeric_values.notna()
            & ~non_finite_values
            & (numeric_values < 0)
        ]

        for index in negative_rows.index:
            errors.append(
                f"ERROR: {column} is negative "
                f"at row {index}"
            )

    return errors
