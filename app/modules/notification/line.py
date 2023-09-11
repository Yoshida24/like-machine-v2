import requests

import os

line_notify_friendly_name = os.environ["LINE_NOTIFY_FRIENDLY_NAME"]
line_notify_token = os.environ["LINE_NOTIFY_TOKEN"]
line_notify_endpoint = os.environ["LINE_NOTIFY_ENDPOINT"]


def notify(notification_message):
    headers = {"Authorization": f"Bearer {line_notify_token}"}
    data = {"message": notification_message}
    response = requests.post(line_notify_endpoint, headers=headers, data=data)
