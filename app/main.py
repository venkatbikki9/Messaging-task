from flask import Flask, request, jsonify
from app.celery_app import send_email_task, log_time_task


app = Flask(__name__)

@app.route('/action')
def action():
    email = request.args.get('sendmail')
    talk = request.args.get('talktome')

    if email:
        send_email_task.delay(email)
        return jsonify({'status': 'Email task queued', 'email': email})
    elif talk is not None:
        log_time_task()
        return jsonify({'status': 'Time logged'})
    else:
        return jsonify({'status': 'No valid action provided'})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

