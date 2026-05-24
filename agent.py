import os
from dotenv import load_dotenv
from google import genai

from utils import *

AGENT_NAME = "<AGENTE TOP>"

# carrega variáveis de ambiente
load_dotenv()

clear_terminal()

# definição da chave da API
if not os.environ.get("GEMINI_API_KEY"):
    print_header(AGENT_NAME)
    new_api_key = input("\n## SETUP ##\nPara que o agente funcione, ele precisa da sua chave de API do Gemini. Será criado um arquivo .env com ela.\nNÃO COMPARTILHE sua chave com ninguém.\n\nInsira sua chave: ")

    try:
        with open(".env", "w") as f:
            f.write(f"GEMINI_API_KEY={new_api_key}")
    except Exception as e:
        input(f"Erro! {e}")


# instanciação do cliente
global client, api_key

while True:
    try:
        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")

        client = genai.Client(api_key=api_key)
        break

    except Exception as e:
        input(f"Erro! {e}")

        clear_terminal()

        api_key = input("## REDEFINIÇÃO DE CHAVE ##\n\nInsira sua chave: ")

        with open(".env", "w") as f:
            f.truncate(0)
            f.write(f"GEMINI_API_KEY={api_key}")


    

SYSTEM_PROMPT = open("system_prompt.txt").read()
history = [{"role" : "system", "content" : SYSTEM_PROMPT}]

clear_terminal()
print_header(AGENT_NAME)
print("Agente iniciado. Para encerrar o programa, digite 'sair'")
# execução do agente
while True:
    user_input = input("\nVocê: ").strip()
    if user_input.lower() == "sair":
        break

    history.append({"role" : "user", "content" : user_input})

    agent_input = []
    agent_ans = "fala meu bom"

    history.append({"role" : "assistant", "content" : agent_ans})

    print("\nAgente: ", agent_ans)



# execução do chat
    # mensagem inicial
    # loop de execução
    # gravação da entrada do usuário
    # repasse pra API da LLM
    # repasse da resposta do modelo para usuário
    # gravação da resposta
