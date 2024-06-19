import pandas as pd
import numpy as np


# Function to load data in chunks, exclude all-NaN columns and reduce memory usage
def _reduce_memory(df):
    for col in df.columns:
        col_type = df[col].dtype
        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                else:
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype('category')
    return df


def load_data_in_chunks(path, chunk_size=50000, usecols=None, high_na_threshold=0.9):
    chunks = []
    for chunk in pd.read_csv(path, chunksize=chunk_size, usecols=usecols, low_memory=False):
        chunk = _reduce_memory(chunk)
        chunk.dropna(axis=1, thresh=chunk_size * (1 - high_na_threshold), inplace=True)
        chunk.dropna(axis=0, thresh=int((1 - high_na_threshold) * len(chunk.columns)), inplace=True)
        date_cols = chunk.select_dtypes(include=['object']).columns
        for col in date_cols:
            chunk[col] = pd.to_datetime(chunk[col], errors='coerce')
        chunks.append(chunk)

    combined_df = pd.concat(chunks, ignore_index=True)

    return combined_df
# %%
