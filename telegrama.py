import requests as r

# enviar mensaje al chat
class telegrama_api:
    def __init__(self, a):
        mensaje = {'chat_id' : <chatid>, 'text' : a}
        r.post('API_TOKEN', mensaje)

if __name__ == '__main__':
    None