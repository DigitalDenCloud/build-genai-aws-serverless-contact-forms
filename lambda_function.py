import json
import boto3
import os
import logging
from botocore.exceptions import ClientError
from template import generate_quote_prompt

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Configuration from environment variables
RECEIVER = os.environ['RECEIVER_EMAIL']
SENDER = os.environ['SENDER_EMAIL']
SENDER_NAME = os.environ['SENDER_NAME']
SES_REGION = os.environ['SES_REGION']
BEDROCK_REGION = os.environ['BEDROCK_REGION']
MODEL_ID = os.environ['MODEL_ID']

# Validate required environment variables
required_vars = [RECEIVER, SENDER, SENDER_NAME, SES_REGION, BEDROCK_REGION, MODEL_ID]
if not all(required_vars):
    raise EnvironmentError("Missing one or more required environment variables")

# Initialize AWS service clients
ses = boto3.client('ses', region_name=SES_REGION)
bedrock = boto3.client('bedrock-runtime', region_name=BEDROCK_REGION)

def lambda_handler(event, context):
    """
    Main handler function for the Lambda.
    Processes incoming events, generates AI-based quotes, and sends emails.
    """
    try:
        # Parse the incoming event data
        data = json.loads(event.get('body', '{}'))
        logger.info(f"Received message from {data.get('name', 'unknown')}")

        # Send notification email about the new form submission
        send_notification_email(data)
        
        try:
            # Generate a quote using Bedrock
            quote = generate_quote_with_bedrock()
        except Exception as e:
            logger.error(f"Error generating quote: {str(e)}")
            quote = "'Believe in yourself and all that you are.'"  # Fallback quote if generation fails

        # Send response email to the user with the generated quote
        send_user_response_email(data, quote)
        
        # Return success response
        return response(200, {'result': 'Success'})
    
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        return response(500, {'result': 'Failed', 'error': str(e)})

def send_notification_email(data):
    """
    Sends a notification email about a new form submission.
    """
    try:
        email_body = (
            f"New contact form submission:\n\n"
            f"Name: {data['name']}\n"
            f"Email: {data['email']}\n"
            f"Message: {data['message']}"
        )
        response = ses.send_email(
            Source=f"{SENDER_NAME} <{SENDER}>",
            Destination={'ToAddresses': [RECEIVER]},
            Message={
                'Subject': {'Data': f"[Contact Form] New submission from {data['name']}"},
                'Body': {'Text': {'Data': email_body}},
            },
            ReplyToAddresses=[data['email']]
        )
        logger.info(f"Notification email sent to {RECEIVER}. Message ID: {response['MessageId']}")
    except ClientError as e:
        logger.error(f"Error sending notification email: {e.response['Error']['Message']}")

def generate_quote_with_bedrock():
    """
    Generates a quote using the Bedrock Messages API with Anthropic Claude.
    """
    try:
        # Prepare the system-level instruction
        system_prompt = "You are an assistant that generates concise and original quotes to engage and inspire users."
        
        # User message for the prompt
        user_message = {"role": "user", "content": generate_quote_prompt()}
        
        # Prepare the request body
        native_request = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 150,                          # Set the maximum token count
            "system": system_prompt,                    # System-level instruction
            "messages": [user_message]                  # Messages array
        }
        
        # Call the Bedrock model
        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(native_request),
            contentType='application/json',
            accept='application/json'
        )
        
        # Parse the response
        response_body = json.loads(response['body'].read())
        logger.info(f"Full response from Bedrock: {json.dumps(response_body, indent=4)}")
        
        # Extract the generated content from the response
        if "content" in response_body and isinstance(response_body["content"], list):
            # Get the first element's 'text' key
            quote = response_body["content"][0]["text"].strip()
            return quote
        else:
            logger.error("The response does not contain the expected 'content' field.")
            raise KeyError("The response does not contain the expected 'content' field.")
    except Exception as e:
        logger.error(f"Error generating quote: {str(e)}")
        raise


def send_user_response_email(data, quote):
    """
    Sends a response email to the user with the generated quote.
    """
    email_body = (
        f"Hi {data['name']},\n\n"
        f"Thanks for reaching out through my website. I've received your message and will get back to you soon.\n\n"
        f"Take a moment to reflect on this:\n\n"
        f"'{quote}'\n\n"
        f"Kind regards,\n"
        f"{SENDER_NAME}\n\n"
        f"{data['name']}, this quote was uniquely generated by AI (Amazon Bedrock) just for you."
    )
    
    try:
        response = ses.send_email(
            Source=f"{SENDER_NAME} <{SENDER}>",
            Destination={'ToAddresses': [data['email']]},
            Message={
                'Subject': {'Data': f"Thank you for contacting {SENDER_NAME}"},
                'Body': {'Text': {'Data': email_body}},
            }
        )
        logger.info(f"User response email sent to {data['email']}. Message ID: {response['MessageId']}")
    except ClientError as e:
        logger.error(f"Error sending user response email: {e.response['Error']['Message']}")

def response(status_code, body):
    """
    Generates a standardized response object for the API Gateway.
    """
    return {
        'statusCode': status_code,
        'body': json.dumps(body),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
    }

# Log that the Lambda function is configured and ready
logger.info("Lambda function configured and ready.")
