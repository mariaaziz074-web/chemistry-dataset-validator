import pandas as pd

from validate_dataset import validate_dataset


def test_valid_dataset(tmp_path):
    data = pd.DataFrame({
        "Material": ["MnSe"],
        "Dye": ["MB"],
        "Bandgap_eV": [2.1],
        "Concentration_mg_L": [20],
        "Time_min": [120],
        "Rate_constant": [0.012]
    })

    file_path = tmp_path / "valid.csv"
    data.to_csv(file_path, index=False)

    errors = validate_dataset(file_path)

    assert errors == []


def test_negative_bandgap(tmp_path):
    data = pd.DataFrame({
        "Material": ["MnSe"],
        "Dye": ["MB"],
        "Bandgap_eV": [-1.0],
        "Concentration_mg_L": [20],
        "Time_min": [120],
        "Rate_constant": [0.012]
    })

    file_path = tmp_path / "invalid.csv"
    data.to_csv(file_path, index=False)

    errors = validate_dataset(file_path)

    assert "ERROR: Bandgap_eV is negative at row 0" in errors


def test_negative_time(tmp_path):
    data = pd.DataFrame({
        "Material": ["CoSe"],
        "Dye": ["MB"],
        "Bandgap_eV": [2.5],
        "Concentration_mg_L": [20],
        "Time_min": [-30],
        "Rate_constant": [0.031]
    })

    file_path = tmp_path / "invalid.csv"
    data.to_csv(file_path, index=False)

    errors = validate_dataset(file_path)

    assert "ERROR: Time_min is negative at row 0" in errors