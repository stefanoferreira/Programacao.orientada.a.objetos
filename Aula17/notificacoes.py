class  SistemaMensagens:
    def __init__(self):
        print(f"SISTEMA DE MENSAGENS")
        
class NotificacaoEmail:
    def enviar(self, mensagem):
        self.mensagem = mensagem
        print(f"E-mail enviado: {mensagem}")
        
class NotificacaoSMS:
    def enviar(self, mensagem):
        self.mensagem = mensagem
        print(f"SMS enviado: {mensagem}")
        
class NotificacaoWhatsApp:
    def enviar(self, mensagem):
        print(f"WhatsApp enviado: {mensagem}")
        
notificacoes = [NotificacaoEmail(), NotificacaoSMS(), NotificacaoWhatsApp()]

SistemaMensagens()

for notificacao in notificacoes:
    notificacao.enviar(f"Sua Compra foi Aprovada .")
    
        
   