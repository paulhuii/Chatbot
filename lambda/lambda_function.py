# lambda_function.py
import json

def lambda_handler(event, response):
    try:
        # Parse the incoming message
        body = json.loads(event['body'])
        message = body['message']
        
        # Add your chatbot logic here
        response_message = f"You said: {message}"
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({
                'message': response_message
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }