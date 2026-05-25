import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

from utils import *

AGENT_NAME = "Guia da Dialética"

if __name__ == "__main__":
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


    # aviso de privacidade e uso dos prompts
    clear_terminal()
    print_header(AGENT_NAME)
    input("!! ATENÇÃO !!\nEsse programa utiliza o Gemini como LLM de processamnto e geração de texto.\nOs conteúdos enviados para o modelo podem ser usados para treinamento, então NÃO ENVIE DADOS SENSÍVEIS OU PESSOAIS.")

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
    history = [types.Part.from_text(text=f"system: {SYSTEM_PROMPT}")]

    clear_terminal()
    print_header(AGENT_NAME)
    print("Agente iniciado. Para encerrar o programa, digite 'sair'\n")

    try:
        # apresentação do agente
        history.append(types.Part.from_text(text="Se apresente brevemente e explique com o que você pode ajudar."))

        print("Guia:")
        print(client.models.generate_content(
            model="gemini-3.5-flash",
            contents=history
        ).text)
    except Exception as e:
        print(f"Erro! {e}")


    # execução do chat
    while True:
        print_divider()
        user_input = input("Você: ").strip()
        if user_input.lower() in ("sair", "exit"):
            break

        history.append(types.Part.from_text(text=f"user: {user_input}"))

        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=history
            )

            history.append(types.Part.from_text(text=f"model: {response.text}"))
            
            print_divider()
            print("Agente: ", response.text)

        except Exception as e:
            print(f"Erro! {e}")
