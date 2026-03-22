import pandas as pd
import re


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    # Check if new_column already exists
    if new_column in df.columns:
        return pd.DataFrame()

    # Validate new column name
    if not re.match(r'^[a-zA-Z_]+$', new_column):
        return pd.DataFrame()

    # Validate role expression (allow letters, underscores, spaces, +, -, *, and digits for numeric literals)
    if not re.match(r'^[a-zA-Z_\s+*-]+$', role):
        return pd.DataFrame()

    # Extract column names from role
    for col in df.columns:
        if not re.match(r'^[a-zA-Z_\s+*-]+$', str(col)):
            return pd.DataFrame()

    try:
        result_df = df.copy()
        result_df[new_column] = df.eval(role)
        return result_df
    except (SyntaxError, KeyError, TypeError, ValueError, pd.errors.UndefinedVariableError):
        return pd.DataFrame()
