"""Listen for prometheus alerts, and convert them to a human readable alert.

Typical format of a received alert:
{
  "version": "4",
  "groupKey": <string>,    // key identifying the group of alerts (e.g. to deduplicate)
  "status": "<resolved|firing>",
  "receiver": <string>,
  "groupLabels": <object>,
  "commonLabels": <object>,
  "commonAnnotations": <object>,
  "externalURL": <string>,  // backlink to the Alertmanager.
  "alerts": [
    {
      "status": "<resolved|firing>",
      "labels": <object>,
      "annotations": <object>,
      "startsAt": "<rfc3339>",
      "endsAt": "<rfc3339>",
      "generatorURL": <string> // identifies the entity that caused the alert
    },
    ...
  ]
}
"""
from flask import request, current_app
from . import appblueprint


@appblueprint.route('/prometheus', methods=['POST'])
def from_prometheus():
    alerts = request.get_json()
    message = alert_to_message(alerts)
    return appblueprint.prombot_sender.send(message)


def alert_to_message(alert_dict):
    # If there is one common summary no need to go through all alerts
    if not alert_dict:
        current_app.logger.error(f"Prometheus is not valid json: {alert_dict}")
    try:
        # Get the prefix and gather the alert short and long descriptions
        prefix = current_app.config['MESSAGE_PREFIX'] or ""
        alert_brief = ",".join([alert['annotations']["summary"] for alert in alert_dict["alerts"]])
        alert_desc = "\n".join([f"<u><a href=\"{alert['generatorURL']}\">{alert['status']}</a></u>: {alert['annotations']['description']}" for alert in alert_dict["alerts"]])

        # Build the message
        msg = f"<b>{prefix} {alert_dict['status']}: {alert_brief}</b>\n\n{alert_desc}"

        # Fix urls if needed
        if len(current_app.config['URL_REPLACE']) == 2:
            msg = msg.replace(
                current_app.config['URL_REPLACE'][0],
                current_app.config['URL_REPLACE'][1]
            )
        return msg
    except KeyError as e:
        current_app.logger.error(f"Couln't decode prometheus alert: {e}. Message: {alert_dict}")
    return "<b>{prefix}</b>\nAn error prevented the alert to be detailed.Please check the logs."
