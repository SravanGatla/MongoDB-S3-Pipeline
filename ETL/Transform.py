import pandas as pd


def transform_data(data):
    df = pd.DataFrame(data)
    columns_to_drop = ['address', 'grades', '_id']
    df_info = df.drop(columns_to_drop, axis=1)
    replace_column = ['restaurant_id', 'name', 'cuisine', 'borough']
    df_info = df_info.reindex(columns=replace_column)

    df_full_address = pd.json_normalize(df['address'])
    df_full_address[['coord1', 'coord2']] = pd.DataFrame(df_full_address['coord'].tolist(), index=df_full_address.index)
    df_full_address.drop(columns=['coord'], inplace=True)
    df_full_address = df_full_address.merge(df[['restaurant_id']], left_index=True, right_index=True)

    return df_info, df_full_address
