import os
import requests

import json


class WhatsAppWrapper:

    API_URL = "https://graph.facebook.com/v13.0/"
    # API_TOKEN = os.environ.get("WHATSAPP_API_TOKEN")
    # NUMBER_ID = os.environ.get("WHATSAPP_NUMBER_ID")
    API_TOKEN = 'EAAI0fSBwMZAABAAecP0GhTJdWAUhG1AsEdVkYfyH1GZCUYykIx4viFAEAdngeppZCobatF1lKR6nOIpZCFwoyJWwT8D91nLYEhvzGVy4OgxWf5wUqO8B68YNn4rq37l3sB5oJQMg8xBFGgQRGYp18QXdxDRuaw6rtnuEYzTdl85AiZBXCjH4ogpNzvgwEOv3D58R0SVvhcgZDZD'
    NUMBER_ID = '103588822656276'
    print(NUMBER_ID, "BBBBBBBBBBBBBBBBBBBBBBBBBBB")

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {self.API_TOKEN}",
            "Content-Type": "application/json",
        }
        self.API_URL = self.API_URL + self.NUMBER_ID
        print(self.API_URL, 'CCCCCCCCCCCCCCCCCCCCCCCC')

    def send_template_message(self, template_name, language_code, phone_number):

        payload = ({
            "messaging_product": "whatsapp",
            "to": "9982908095",
            "type": "text",
            "text": "Congrations you are in the whatsapp business api."

            # "template": {
            #     "name": template_name,
            #     "language": {
            #         "code": language_code
            #     }
            # }
        })

        response = requests.request("POST", f"{self.API_URL}/messages", headers=self.headers, data=payload)

        assert response.status_code == 200, "Error sending message"

        return response.status_code