import pandas as pd
import datetime as dt
import smtplib
import random
import os

data = pd.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day

for dat in data_dict:
    if dat["month"] == month:
        if dat["day"] == day:
            email = dat["email"]
            name = dat["name"]
            path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
            with open(file=path, mode="r") as bday:
                contents = bday.read()
                content = contents.replace("[NAME]", name)

                my_email = os.environ.get("P_MAIL")
                pas = os.environ.get('P_MAIL_PASSWORD')

                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=pas)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs=email,
                                        msg=f"Subject:Happy birthday\n\n{content}")