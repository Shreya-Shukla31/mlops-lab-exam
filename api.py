import os
import pandas as pd

def test_data_exists():
    assert os.path.exists("data/data.csv"), "Data file not found"

def test_data_not_empty():
    df = pd.read_csv("data/data.csv")
    assert len(df) > 0, "Data is empty"

if __name__ == "__main__":
    test_data_exists()
    test_data_not_empty()
    print("All tests passed successfully!")