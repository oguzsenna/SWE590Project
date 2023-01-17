# 590 Power of 5x5 Matrix
This repository consisty flask app running on ec2, python code that running on lambda function and text file for sending request.

The user sends a text file consist a 5x5 matrix and desired power of that matrix. After that EC2 instance get the text file and converts it into JSON format. Then make a post request to the AWS Lambda for the calculation of the nth power of the matrix. When Lambda finishes calculations, it sends results back to the EC2 instance in JSON format. After getting results, the EC2 instance writes JSON data to the text file and sends this result text file to the s3 bucket.





![last_arch](https://user-images.githubusercontent.com/57816597/209660066-e408f41e-93fa-45cc-82b5-04bccb8c6d8f.png)
