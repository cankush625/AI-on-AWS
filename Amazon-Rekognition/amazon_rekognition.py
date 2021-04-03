import cv2
import boto3

# Capture the image from the webcam
cap = cv2.VideoCapture(0)
res, photo = cap.read()
myphoto = "ankush.jpg"
cv2.imwrite(myphoto, photo)
cap.release()

# Upload image to the S3 bucket
region = "ap-south-1"
bucketname = "ai-on-aws-test"
filename = "file.jpg"
s3 = boto3.resource('s3')
s3.Bucket(bucketname).upload_file(myphoto, filename)

# Connect to Amazon Rekognition service
rek = boto3.client('rekognition', region)
res = rek.detect_labels(
    Image = {
        'S3Object': {
            'Bucket': bucketname,
            'Name': filename,
        }
    },
    MaxLabels = 10,
    MinConfidence = 90
)

res['Labels'][0]['Name']