import sender

SUCCESS_MESSAGE = """This is an automatic notification that one of your orders was auto-accepted using our service:\n
Name: {}\n
"""

print('Connected to email')
try:
    Name='GR'
    mail = sender.Mail('smtp.gmail.com','ecesistesting@gmail.com','ngottpshjiypzlcs', 465, use_ssl=True,fromaddr='ecesistesting@gmail.com')
    success_message = SUCCESS_MESSAGE.format(Name)
    print(success_message)
    #success_message=success_message.encode('utf-8')
    success_message = success_message.encode('ascii', 'ignore').decode('ascii')
    subject = 'Testing AWS'
    print(subject)
    print('--------------------------------------------------------------')
    mail.send_message(subject=subject, to=('kaviya.v@ecesistech.com'), body=success_message)
except Exception as ex:
    print(ex)
