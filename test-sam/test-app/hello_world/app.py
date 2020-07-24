import json
import requests
import boto3


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        # ip = requests.get("http://checkip.amazonaws.com/")

        Access_key_id = "AKIASNKK654OYMYJ42MC"
        Secret_key_id = "wwungwb0b/e8HyJtOBLnjLkS2AYz2Z9ZG/nzMPQR"
        bucket = "crawler-data-lotus"
        key = "newsData1.json"

        s3 = boto3.client('s3', aws_access_key_id=Access_key_id, aws_secret_access_key=Secret_key_id)
        content_object = s3.get_object(Bucket=bucket, Key=key)

        file_content = content_object['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)

        # msg = event["body"]
        msg = json_content["News_ID"]

    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e



    return {
        'statusCode': 200,
        'body': json.dumps(json_content)
        # "body": json.dumps({
        #     "event": msg,
        #     # "message": event,
        #     # "location": ip.text.replace("\n", "")
        # }),
    }
