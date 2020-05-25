import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return 'Welcome to edd butcher'


@app.route('/callback/ussd', methods=['POST'])
def ussd():
    response = ""

    text_param = request.form.get('text')
    text_list = text_param.split('*')

    # sessionId, phoneNumber, networkCode, serviceCode, text
    # If user just dialed *384#
    if not text_list[0]:
        response = "CON Welcome to edd butcher app\n"
        response += "1. See list of available kinds of meat\n"
        response += "2. Transfer money"

        # If user selects 1 from 1st menu
    elif text_list[0] == "1":
        response = "END "
        response += "1. beef\n"
        response += "2. chicken\n"
        response += "3. goat"
    # If user selects 2 from 1st menu
    elif text_list[0] == "2":
        response = "END You selected transfer money"

    return response


app.run()
