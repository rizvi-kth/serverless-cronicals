import json
import boto3

session = boto3.session.Session(profile_name='rz-robot')
s3 = session.resource('s3')

# Get all the buckets
for bucket in s3.buckets.all():
    print(bucket.name)


bucket = "crawl-data"
key = "2020/05/2020-05-01/sample-data.json"

content_object = s3.Object(bucket, key)
file_content = content_object.get()['Body'].read().decode('utf-8')
json_content = json.loads(file_content)
print(json_content[0]['URL'])
