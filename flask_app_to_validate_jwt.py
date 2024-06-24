from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

# Secret key to encode the JWT. In production, use a secure secret and keep it safe.
SECRET_KEY = 'your_secret_key'

def create_jwt(email_id, expire_minutes=30):
    expire_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=expire_minutes)
    payload = {
        'email_id': email_id,
        'exp': expire_time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt(token):
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

@app.route('/protected', methods=['GET'])
def protected():
    # Get the token from the request headers
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing!'}), 403

    # Verify the token
    payload = verify_jwt(token)
    if payload is None:
        return jsonify({'message': 'Invalid or expired token!'}), 403
    current_time = datetime.datetime.utcnow()
    exp_time = datetime.datetime.utcfromtimestamp(payload['exp'])
    if current_time > exp_time:
        return jsonify({'message': 'Expired token!'}), 403

    # If the token is valid, return a success message
    return jsonify({'message': 'Token is valid!', 'data': payload})

@app.route('/login', methods=['POST'])
def login():
    email_id = request.json.get('email_id')
    if not email_id:
        return jsonify({'message': 'Email ID is missing!'}), 400

    token = create_jwt(email_id)
    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(debug=True)
