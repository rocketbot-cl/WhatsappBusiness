'''
    Whatsapp Business API Requests
'''
import requests

class Whatsapp_auth: #pylint: disable=invalid-name
    '''
        Clase Whatsapp
    '''
    def __init__(self, api_key, phone_id):
        self.api_key = "Bearer " + api_key
        self.url = f"https://graph.facebook.com/v15.0/{phone_id}/"
        self.valid = None
        self.get_valid()
        self.headers = {
                "Authorization": self.api_key
            }

    def get_valid(self):
        '''
            Metodo para validar la API Key
        '''
        try:
            url = self.url
            headers = {
                "Authorization": self.api_key
            }
            r = requests.get(url, headers=headers, timeout=30)
            j = r.json()

            if j.get('error'):
                raise Exception(j.get('error').get('message'))
            else:
                self.valid = True


        except Exception as exc:
            raise exc

    def send_message(self, message, phone_number, template=None, code="en_US"):
        '''
            Metodo para enviar mensajes
        '''
        try:
            url = self.url + "messages"
            headers = {
                "Authorization": self.api_key
            }
            data = {
                "messaging_product": "whatsapp",
                "to": phone_number,
                }

            if template:
                data["type"] = "template"
                data["template"] = {
                    "name": template,
                    "language": {
                        "code": code
                    }
                }

            else:
                data["type"] = "text"
                data["text"] = {
                    "body": message
                }

            r = requests.post(url, headers=headers, json=data, timeout=30)
            j = r.json()
            print(j)
            if j.get('error'):
                raise Exception(j.get('error').get('message'))
            else:
                return True

        except Exception as exc:
            raise exc