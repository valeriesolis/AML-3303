import pandas as pd

def load_dataset(url: str) -> pd.DataFrame:
    """
    Load dataset from a URL into a pandas DataFrame.

    Args:
        url (str): URL to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame.

    Raises:
        RuntimeError: If the CSV cannot be loaded.
    """
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load data from URL: {e}")

def calculate_column_mean(df: pd.DataFrame, column_name: str) -> float:
    """
    Calculate the mean (average) of a specified column in the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The column for which to calculate the mean.

    Returns:
        float: Mean of the column.

    Raises:
        ValueError: If the specified column does not exist.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in dataset.")
    return df[column_name].mean()

def calculate_column_max(df: pd.DataFrame, column_name: str) -> float:
    """
    Calculate the maximum value of a specified column in the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The column for which to find the max value.

    Returns:
        float: Maximum value in the column.

    Raises:
        ValueError: If the specified column does not exist.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in dataset.")
    return df[column_name].max()

def filter_by_category(df: pd.DataFrame, column_name: str, value: str) -> pd.DataFrame:
    """
    Filter the DataFrame by a specific category in the given column.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The column to filter on.
        value (str): The value to match in the column.

    Returns:
        pd.DataFrame: Filtered DataFrame containing only matching rows.

    Raises:
        ValueError: If the specified column does not exist.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in dataset.")
    return df[df[column_name] == value]

if __name__ == "__main__":
    # Constants
    DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    
    # Load and process data
    iris_df = load_dataset(DATA_URL)

    avg_sepal_length = calculate_column_mean(iris_df, 'sepal_length')
    max_petal_width = calculate_column_max(iris_df, 'petal_width')
    setosa_df = filter_by_category(iris_df, 'species', 'setosa')

    # Output results
    print("Average sepal length:", avg_sepal_length)
    print("Max petal width:", max_petal_width)
    print("First 5 Setosa rows:")
    print(setosa_df.head())
