from sqlalchemy import create_engine
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def fetch_data():
    # Database connection details
    host = "00"
    dbname = "zete_dues_and_fine"
    user = "root"
    password = "password" #password is hidden 

    # Create an SQLAlchemy engine
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{dbname}")

    # SQL query
    sql_query = "SELECT * FROM brothersspring2024"

    # Fetch the data using the engine
    data = pd.read_sql(sql_query, engine)

    return data

def send_email(to_email, name, dues_amount):
    print("Here")
    # Email server details (Replace with your details)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'gibbsngresge@gmail.com'
    smtp_password = 'mfde fjdi ivis xpog'

    # Email content
    message = MIMEMultipart()
    message['Subject'] = 'Your Dues for This Semester'
    message['From'] = smtp_user
    message['To'] = to_email
    body = f"Hello this is Gibbs Gresge.\n{name}, your dues this semester come out to {dues_amount}. If you have any issues with this please reach out to me.\nIn TKPhi, Gibbs Gresge"
    message.attach(MIMEText(body, 'plain'))

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(message)

def main():
    data = fetch_data()
    for index, row in data.iterrows():
        send_email(row['email'], row['name'], row['total_amount_of_dues'])

if __name__ == '__main__':
    main()
