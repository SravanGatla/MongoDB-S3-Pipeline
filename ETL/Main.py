from ETL.Extract import extract_mongo_data
from ETL.Transform import transform_data
from ETL.Load import load_to_s3

# Extraction
data = extract_mongo_data()

# Transformation
df_info, df_full_address = transform_data(data)

# Loading
load_to_s3(df_info, df_full_address, 'restaurant_info.csv', 'address.csv')
