OBJECTIVE :
The goal of this project is to build a simple messaging system that demonstrates asynchronous task processing using RabbitMQ as a message broker and Celery as a task queue. The system is exposed via a Python web application served behind Nginx, with endpoints that allow users to either send an email asynchronously via SMTP or log the current time. An external testing endpoint is exposed using ngrok.

Step 1: Creating the Setup Project Directory and subdirectories:
mkdir messaging-system
cd messaging-system

Create subdirectories:
mkdir app logs
app → Python code and Celery tasks
logs → For app.log

Tree:
<img width="224" height="245" alt="tree" src="https://github.com/user-attachments/assets/11534ede-2c39-4d9e-97b3-1e7bad5d2d17" />


Step 2: Creating Python Virtual Environment shows venv.
python3 -m venv venv
source venv/bin/activate

Upgrade pip:
pip install --upgrade pip

Step 3: Install Dependencies
pip install flask celery[redis] requests python-dotenv
pip install fastapi uvicorn

Step 4: Set Up RabbitMQ
Using Docker  : docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
Management UI: http://localhost:15672
Default username/password: guest/guest
sudo apt-get install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
Check status:
sudo systemctl status rabbitmq-server

Step 5: Creating app/celery_app.py:

Step 6: Creating Flask App  : app/main.py

Step 7: Setup Environment Variables : Create .env:
EMAIL_USER=venkatbikki9gmail@gmail.com
EMAIL_PASS=************
I wont be metioning my password here. To generate a password ,Go to your gmail security and turn on 2 step verifiation first .
Then open app passwords in the gmail security.Create an App name there and a 12 digit password will be given.

Step 8: Run venv, Celery, Flask, configure nginx, Ngrok.
commands to run :
Venv    - source venv/bin/activate
Celery  - celery -A app.celery_app.celery_app worker --loglevel=info
Flask   - python app/main.py
Ngrok   - ngrok http 80

Step 9: I added a shell script named start_all.sh
this includes all the commands to run the above venv,Celery,flask and Ngrok

start_all.sh
#Activate virtual environment
source venv/bin/activate

#Start Celery worker in background
echo "Starting Celery worker..."
celery -A app.celery_app.celery_app worker --loglevel=info &

#Give Celery a few seconds to start
sleep 5

#Start Flask app
echo "Starting Flask app..."
python -m app.main &

#Give Flask a few seconds to start
sleep 5

#Start Ngrok tunnel
echo "Starting Ngrok..."
ngrok http 5000


Check :To check if it is woriking ,to send the mail , enter this URL:
http://localhost:5000/action?sendmail=venkatbikki9@gmail.com
Screenshots:
<img width="1920" height="1080" alt="Screenshot (21)" src="https://github.com/user-attachments/assets/f34bc3de-35b8-46b4-809e-8424c48e7819" />

<img width="1920" height="1080" alt="Screenshot (17)" src="https://github.com/user-attachments/assets/52d7022c-0d04-4af8-a940-c26304a76d8e" />

<img width="1920" height="1080" alt="Screenshot (19)" src="https://github.com/user-attachments/assets/faa7aa83-2ede-4ed4-9f3c-d247978771f1" />

<img width="668" height="328" alt="Screenshot 2025-11-21 110609" src="https://github.com/user-attachments/assets/9a602f4f-cac1-4e46-bbf2-9c66e7eff6da" />


CONCLUSION:
This project successfully walked through building a messaging system using Flask, Celery, RabbitMQ, and Ngrok, with optional Nginx. we have learned to send emails asynchronously using Celery workers, run RabbitMQ for message brokering, expose the local app publicly via Ngrok, manage environment variables securely with .env, and improve deployment by configuring Nginx as a reverse proxy. Along the way, you debugged installation, routing, and port issues—gaining practical real-world experience.





