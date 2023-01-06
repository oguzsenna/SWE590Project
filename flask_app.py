from flask import request, jsonify,Flask
import json
import boto3 
import requests
import random
app = Flask(__name__)
access_key = ''
secret_key = ''
s3_client = boto3.resource('s3',aws_access_key_id=access_key,aws_secret_access_key= secret_key)

@app.route('/api/matrix', methods=['POST'])
def matrix_api():
    #  URL for the matrix calculation API
    url = 'https://wpp6mku2z9.execute-api.eu-central-1.amazonaws.com/default/matrix_calculation'

    # Read in the matrix from the request payload
    matrix_file = request.files['matrix_file']
    data_n  = request.files['n']
    content  = data_n.read()
    n_dict = json.loads(content)
    n = int(n_dict['n'])
        # Convert the matrix to a nested list
    matrix_list = [[int(x) for x in line.split()] for line in matrix_file]

    # Create the JSON object
    data = {'matrix': matrix_list, 'n': int(n)}

    # Make the POST request with the JSON object
    response = requests.post(url, json=data)
     
    # Check if the request was successful
    if response.status_code == 200:
        # Get the matrix result from the response
        matrix = response.json()['Result']

        # Convert the matrix to a string
        matrix_str = '\n'.join([' '.join([str(x) for x in row]) for row in matrix])

        # Write the matrix to a text file
        with open('matrix.txt', 'w') as f:
            f.write(matrix_str)

        

        s3_client.meta.client.upload_file('matrix.txt', 'newbucket565', 'result'+str(random.randint(0,200))+'.txt')

        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': response.status_code})
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)