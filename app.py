from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse

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
        reply = "hello! \ndo ypu want to set a reminder? "
        message.body(reply)
        responded=True
    if len(words)== 1 and "yes" in incoming_msg:
        reminder_string="please provide date in the following format only.\n\n" "*Date @* _type the date_ "
        message.body(reminder_string)
        responded = True
    if len(words) == 1 and "no" in incoming_msg:
        reply="ok. have a nice day!"
        message.body(reply)
        responded =True
    elif len(words)!=1:
        input_type =words[0].strip().lower()
        input_string=words[1].strip()
        if input_type == "date":
            reply= "please neter the reminder message in the following format only.\n\n" "*Reminder @* _type the message_"
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