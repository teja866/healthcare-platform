import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    AWS Lambda function that processes messages from the SQS queue.
    """
    logger.info(f"Received event: {json.dumps(event)}")
    
    for record in event.get('Records', []):
        try:
            # The body of the SQS message
            message_body = record['body']
            logger.info(f"Processing message: {message_body}")
            
            # Parse the payload
            payload = json.loads(message_body)
            
            task_type = payload.get('task')
            
            if task_type == 'welcome_email':
                email = payload.get('email')
                logger.info(f"Simulating sending welcome email to: {email}")
                # Real implementation would call SES or Resend API here
                
            elif task_type == 'process_health_data':
                user_id = payload.get('userId')
                logger.info(f"Simulating heavy health data processing for user: {user_id}")
                
            else:
                logger.info(f"Processed generic task: {task_type}")
                
        except Exception as e:
            logger.error(f"Error processing record {record.get('messageId')}: {str(e)}")
            # Raise exception so SQS retries the message
            raise e
            
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed SQS messages.')
    }
