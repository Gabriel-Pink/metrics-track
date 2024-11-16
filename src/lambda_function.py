import json


def lambda_handler(event, context):
    

    headers = event.get('headers', {})

    return {
        "statusCode": 200,
        "body": json.dumps({
            "headers": headers,
        }),
        "headers": {
            "Content-Type": "application/json"
        }
    }
