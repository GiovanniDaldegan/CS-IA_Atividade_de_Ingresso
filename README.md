# Atividade de Ingresso - Grupo de Inteligência Artificial, IEEE CS UnB
Atividade introdutória do Grupo de Estudos de IA da CS - Ramo IEEE UnB

## O agente

O agente é o Guia da Dialética, um assitente que explica conceitos da Filosofia e fornece planos de leitura de textos e artigos da área.

## Requisitos e instalação de dependências
Para utilizar o agente, o usuário precisa ter uma chave de API do Google AI Studio. Ela deve ser fornecida durante a execução do programa.

Para instalar as dependências, é necessário ter instalado Python 3.10 ou outra versão mais recente.

Com um terminal aberto na raíz desse diretório, execute o comando:

Para Unix/macOS
```sh
python -m pip install -r requirements.txt
```

Para Windows
```sh
py -m pip install -r requirements.txt
```

## Uso do agente

Para executar o programa execute:

Para Unix/macOS
```sh
python ./hello.py
```

Para Windows
```sh
py .\hello.py
```

Na execução do programa, o agente vai se apresentar e explicar com o que ele pode ajudar. Pergunte questões de Filosofia ou peça referências de um assunto da área e ele vai tentar de explicar e oferecer um plano de leitura adequado para seu nível de familiaridade e compreensão dos conceitos.


>[!note] O arquivo [utils.py](./utils.py) foi reutilizado de um outro projeto meu. O resto foi desenvolvido especificamente para essa atividade.
> 
> Nenhum modelo de linguagem foi utilizado na realização da atividade ou produção dos conteúdos presentes, exceto na comunicação com a API para testes do agente.

