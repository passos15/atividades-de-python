#Registro de logs
import datetime #É um módulo usado para registrar quando o evento aconteceu.

def registrar(mensagem, tipo = 'INFO', arquivo = 'app.log'):
#A função ira registrar 3 parâmetros, 'mensagem' que recebera o texto, 'tipo' pode receber as informações e 'arquivo' onde tudo será salvo.                                                  
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #Mostra a data, hora, minutos e segundos.O 'ditetime.detetime.now() pega a data e hora atual, 'Strftime' transforma a data em texto formatado (2026-05-26 15:51:00).
    linha_log = f"[{timestamp}] [{tipo}] {mensagem}\n" #Juntará todas as  informações.

    with open(arquivo, 'a', encoding ='utf-8') as f:
    #Abrirá o arquivo 'app.log' em modo de a 'adicionar texto', usando UTF -8 (permite o uso da acentuação padrão), O arquivo será fechado automaticamente ao sair do bloco.
        f.write(linha_log)  #Salva o texto dentro do arquivo.

registrar("Aplicação iniciada.", "INFO")  #Salva o arquivo que o foi inserido.
registrar("Variável 'x' não definida", "WARNING")   #Envia um alerta de que algo está  errado, mas continua.
registrar("Falha na conexão com o banco  de dados.", "ERROR") #Indica que algo está errado e não é possivel continuar.

print("Logs registrados em 'app.log'.")