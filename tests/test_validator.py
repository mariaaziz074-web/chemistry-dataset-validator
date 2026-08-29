from chemistry_validator import validate_dataset


def test_sample_data_reports_two_errors():
    errors = validate_dataset("sample_data.csv")

    assert len(errors) == 2


def test_valid_finite_dataset_has_no_errors(tmp_path):
    csv_file = tmp_path / "valid_dataset.csv"
    csv_file.write_text(
        "Material,Dye,Bandgap_eV,Concentration_mg_L,Time_min,Rate_constant\n"
        "MnSe,MB,2.1,20,120,0.012\n"
    )

    errors = validate_dataset(csv_file)

    assert errors == []


def test_positive_infinity_is_rejected(tmp_path):
    csv_file = tmp_path / "positive_infinity.csv"
    csv_file.write_text(
        "Material,Dye,Bandgap_eV,Concentration_mg_L,Time_min,Rate_constant\n"
        "MnSe,MB,inf,20,120,0.012\n"
    )

    errors = validate_dataset(csv_file)

    assert errors == [
        "ERROR: Bandgap_eV contains 1 non-finite value(s)"
    ]


def test_negative_infinity_is_rejected_without_negative_error(tmp_path):
    csv_file = tmp_path / "negative_infinity.csv"
    csv_file.write_text(
        "Material,Dye,Bandgap_eV,Concentration_mg_L,Time_min,Rate_constant\n"
        "MnSe,MB,2.1,20,-inf,0.012\n"
    )

    errors = validate_dataset(csv_file)

    assert errors == [
        "ERROR: Time_min contains 1 non-finite value(s)"
    ]


def test_finite_negative_value_is_still_rejected(tmp_path):
    csv_file = tmp_path / "finite_negative.csv"
    csv_file.write_text(
        "Material,Dye,Bandgap_eV,Concentration_mg_L,Time_min,Rate_constant\n"
        "MnSe,MB,2.1,20,120,-0.012\n"
    )

    errors = validate_dataset(csv_file)

    assert errors == [
        "ERROR: Rate_constant is negative at row 0"
    ]


def test_missing_file():
    errors = validate_dataset("does_not_exist.csv")

    assert errors == [
        "ERROR: File not found: does_not_exist.csv"
    ]


def test_invalid_values():
    errors = validate_dataset("sample_data.csv")

    assert "ERROR: Bandgap_eV is negative at row 3" in errors
    assert "ERROR: Time_min is negative at row 4" in errors
