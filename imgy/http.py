import requests
import boto3

BUCKET_NAME = 'imgy'

def upload_file(filename):
    # Create an S3 client
    s3 = boto3.client('s3')

    filename = filename
    bucket_name = BUCKET_NAME

    s3.upload_file(filename, bucket_name, filename)

    with open(filepath) as fh:
        mydata = fh.read()
        response = requests.put('https://api.elasticemail.com/attachments/upload',
                    data=mydata,
                    headers={'content-type':'text/plain'},
                    params={'file': filepath}
                    )

def download_file():


    requests.get('https://api.github.com/user', auth=('user', 'pass'))
