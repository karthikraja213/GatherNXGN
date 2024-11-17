import boto3
import json

def lambda_handler(event, context):
    # Initialize AWS SDK clients for Rekognition and S3
    rekognition_client = boto3.client('rekognition')
    s3_client = boto3.client('s3')

    # Extract the bucket name and file key from the event that triggered the Lambda
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Use Rekognition to analyze the image for faces
    response = rekognition_client.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': file_key
            }
        },
        Attributes=["ALL"]  
    )


    output_bucket = 'gathernxgnresultsbucket'  
    output_key = 'results/' + file_key.split('/')[-1] + '_analysis.json'
    s3_client.put_object(
        Bucket=output_bucket,
        Key=output_key,
        Body=json.dumps(response['FaceDetails'], indent=4)
    )

    # Return the response
    return {
        'statusCode': 200,
        'body': json.dumps(response['FaceDetails'])
    }
