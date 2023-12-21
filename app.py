from flask import Flask,request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)
@app.route("/sms", methods=['POST'])
def reply():
    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
   
    print(incoming_msg)

    message=response.message()
    responded=False
    words = incoming_msg.split('@')
    if "hello" in incoming_msg:
        reply = "Welcome to BMTC ticket bot. "

        reply = "Hello! \n I am your ticket-bot and I will assist you in purchasing bus tickets, bus passes and tracking live location of busses \n Type your queries or choose one of the options below for me to assist you  "
        message.body(reply)
        responded=True

        

        
    if len(words)== 2 and "Bus Tickets" in incoming_msg:
        reminder_string="Would you like to enter your bus stop or bus number "
        message.body(reminder_string)
        responded = True
        if len(words)== 2 and "Bus stop" in incoming_msg:
            reminder_string="Please enter the source stop name choose one of the following options or type your query"
            message.body(reminder_string)

            if len(words)== 3 and "type stop name" in incoming_msg:
                reminder_string="Please type your stop name now"
                message.body(reminder_string)

            responded = True
        elif len(words)== 2 and "Bus number" in incoming_msg:
            reminder_string="Enter the bus number"
            message.body(reminder_string)
            responded = True
        
    elif len(words)!=1:
        input_type =words[0].strip().lower()
        input_string=words[1].strip()
        if input_type == "date":
            reply= "please enter the reminder message in the following format only.\n\n" "*Reminder @* _type the message_"
            set_reminder_date(input_string)
            message.body(reply)
            responded=True
    if input_type=="reminder":
        reply="your reminder is set"
        set_reminder_body(input_string)
        message.body(reply)
        responded=True
    if not responded:
        message.body('Incorrect request format.Please enter in the correct format')

    return str(response)
def set_reminder_date(msg):
    p = parse(msg)
    date = p.strftime('%d/%m/%Y')
    save_reminder_date(date)
    return 0
def set_reminder_body(msg):
    save_reminder_body(msg)
    return 0

if __name__ == "__main__":
    app.run(debug=True)