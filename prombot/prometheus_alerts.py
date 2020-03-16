from flask import request, current_app
from . import appblueprint


@appblueprint.route('/prometheus', methods=['POST'])
def from_prometheus():
    message = request.get_data().decode()
    # alerts = request.get_json()
    # message = prometheus.alert_to_message(alerts)
    print(f"zwqees {message}")
    return appblueprint.prombot_sender.send(message)

def alert_to_message():
    pass
