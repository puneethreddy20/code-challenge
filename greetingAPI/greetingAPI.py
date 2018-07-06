from flask import Flask
from flask import request
from flask import Response
import jwt


app = Flask(__name__)


##convert to bytes
shared_JWT_secretkey="aoR6E4tb6TWDgP8dQdkpcg".encode()

#decode the jwt token received from backend service and get the claims in it.
def decode_jwt_token(jwt_token):
    try:
        payload = jwt.decode(jwt_token, shared_JWT_secretkey,algorithms=['HS256'])
        return payload['UserName']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please try again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please Contact Administrator.'



@app.route('/greetings')
def greetingHandler():

    Token=request.headers["Authorization"]

    username=decode_jwt_token(Token)

    if username=='Signature expired. Please try again':

        return Response('Signature expired. Please try again',status=401)

    if username=='Invalid token. Please Contact Administrator.':

        return Response('Invalid token. Please Contact Administrator.',status=400)

    output="Greetings! "+username

    return Response(output,status=200)


if __name__ == '__main__':
    app.run(host='172.18.0.20',port='8000')
