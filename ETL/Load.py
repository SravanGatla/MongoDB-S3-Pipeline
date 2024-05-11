import boto3
from io import StringIO


def load_to_s3(data1, data2, file_name_1, file_name_2):
    s3 = boto3.client('s3')
    bucket_name = 'my-unique-tf-test-bucket001'
    folder_name = 'destination/'

    # Convert first DataFrame to CSV
    buffer1 = StringIO()
    data1.to_csv(buffer1, index=False)
    key_1 = folder_name + file_name_1
    s3.put_object(Bucket=bucket_name, Key=key_1, Body=buffer1.getvalue())

    # Convert second DataFrame to CSV
    buffer2 = StringIO()
    data2.to_csv(buffer2, index=False)
    key_2 = folder_name + file_name_2
    s3.put_object(Bucket=bucket_name, Key=key_2, Body=buffer2.getvalue())

    print(f"Dataframes uploaded to S3 bucket {bucket_name} as {file_name_1} and {file_name_2}")
