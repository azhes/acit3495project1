import boto3

def upload_video_file(filename):
    s3 = boto3.client("s3")

    s3.upload_file(
        filename,
        Bucket="acit3495-filestorage",
        Key=filename
    )

    print(f'File {filename} successfully uploaded.')