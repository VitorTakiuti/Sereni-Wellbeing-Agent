# Sereni: Seu Companheiro de Bem-Estar Acessível ✨


## Sobre o Projeto 💖🫂

Sereni (uma fusão de "Ser" e "Serenidade") é mais do que um simples chatbot. Ele foi concebido para ser um **companheiro digital empático e paciente**, focado em auxiliar na **construção e manutenção de hábitos saudáveis** e na promoção do **bem-estar físico e mental**.

Nosso grande diferencial e missão central é a **acessibilidade e inclusão**. Sereni foi pensado desde o início para ser amigável e facilmente utilizável por **todos**, com especial atenção às necessidades de **idosos** 👵 e **pessoas com deficiência** ♿, adaptando-se a diferentes ritmos e formas de interação.

Este projeto serve como um ponto de partida robusto, utilizando o poder da **Inteligência Artificial Generativa** (via Google Gemini) para compreender e responder de forma natural e útil.

## Funcionalidades Principais ✨

Mesmo nesta versão inicial, Sereni oferece funcionalidades essenciais para começar sua jornada de bem-estar:

* **Conversa Empática e Natural:** 💬 Utilize linguagem natural para interagir. Sereni foi treinado (através de prompts no Gemini) para ser paciente, compreensivo e evitar jargões.
* **Gestão de Hábitos Simples:** 🎯 Adicione e liste hábitos que você deseja cultivar ("beber água", "ler 15 minutos", "caminhar leve").
* **Lembretes Básicos:** ⏰ Agende lembretes simples para suas atividades ou hábitos (ex: "me lembre de tomar remédio às 8:00").
* **Dicas de Bem-Estar:** 🧘‍♀️🍎 Pode oferecer sugestões leves de relaxamento, hidratação ou nutrição em resposta a perguntas gerais.
* **Base para Acessibilidade:** Embora as adaptações de interface dependam da plataforma final, a base conversacional em linguagem simples e a paciência na interação já são pilares de acessibilidade.

## Por Que Sereni? 🤔

No mundo digital acelerado, muitas ferramentas de bem-estar podem ser complexas ou inacessíveis para certas populações. Sereni (junção de Ser e Serenidade) nasceu da necessidade de criar uma ponte digital que seja:

* **Simples:** Fácil de entender e usar, mesmo para quem não tem familiaridade com tecnologia.
* **Paciente:** Sem pressa, permitindo que o usuário se expresse em seu tempo.
* **Inclusiva:** Pensada para se adaptar a diversas necessidades, promovendo autonomia.
* **Um Companheiro:** Oferecendo suporte motivacional e lembretes de forma amigável, como um amigo preocupado com seu bem-estar.

## Tecnologias Utilizadas 🛠️

* **Python:** 🐍 A linguagem de programação principal pela sua flexibilidade e ecossistema de bibliotecas.
* **Google AI Studio (Gemini API):** ☁️ Fornece o poder da compreensão de linguagem natural (NLU) e a geração de respostas empáticas e contextuais. Utilizamos o modelo `gemini-1.5-flash-latest` pela sua eficiência e velocidade.
* **Estrutura Modular:** Código organizado em módulos (`config`, `gemini_client`, `services`, `sereni_app`) para facilitar a manutenção e futuras expansões.

## Como Começar (Setup) 🚀

Siga estes passos simples para colocar o Sereni rodando no seu ambiente:

1.  **Pré-requisitos:**
    * Certifique-se de ter o **Python 3.7+** instalado. Você pode baixar em [python.org](https://www.python.org/downloads/).
    * Obtenha uma **Chave de API do Google AI Studio (Gemini)**. Se você não tem, visite [https://makersuite.google.com/](https://makersuite.google.com/), crie um projeto e gere sua chave. Guarde-a em um local seguro! 🔑

2.  **Clone o Repositório:**
    * Abra o terminal ou prompt de comando.
    * Navegue até o diretório onde deseja salvar o projeto.
    * Clone este repositório (se você estiver vendo isso no GitHub, este é o comando para baixar os arquivos):
        ```bash
        git clone [URL_DO_SEU_REPOSITÓRIO]
        cd [pasta_do_projeto] # Ex: cd sereni_project
        ```

3.  **Instale as Dependências:**
    * Dentro da pasta do projeto clonado, execute o comando para instalar a biblioteca necessária do Google:
        ```bash
        pip install google-generativeai
        ```
    * *(Opcional, mas recomendado: Crie e ative um ambiente virtual antes de instalar as dependências para isolar as bibliotecas do projeto).*

4.  **Configure Sua Chave de API:** ⚠️ **Passo Crucial!**
    * Abra o arquivo `config.py` no seu editor de código (como VS Code, que foi usado na explicação de execução).
    * Localize a linha que define `GOOGLE_API_KEY`.
    * **Substitua `"SUA_CHAVE_DE_API_AQUI"` pela sua chave de API real do Google AI Studio.**
    * Salve o arquivo `config.py`.
    * *(Em um projeto de produção, você NUNCA deve colocar sua chave diretamente no código. Use variáveis de ambiente ou arquivos `.env` e adicione `config.py` (ou o arquivo com a chave) ao `.gitignore`. Para este exemplo inicial, a abordagem direta em `config.py` é usada por simplicidade).*

## Como Usar o Sereni (via Terminal) ▶️

Uma vez que o setup esteja completo e sua chave de API configurada, você pode rodar o Sereni:

1.  Abra o terminal ou prompt de comando na pasta raiz do projeto.
2.  Execute o arquivo principal:
    ```bash
    python sereni_app.py
    ```
3.  O Sereni iniciará e você verá a mensagem de boas-vindas.
4.  Digite suas mensagens no prompt "Você: " e pressione Enter.
5.  Para sair, digite `sair` ou `tchau`.

**Exemplos de Interação:**
Você: Olá Sereni
Sereni: Olá! Eu sou o Sereni, seu companheiro de bem-estar. Como posso te ajudar hoje?
------------------------------
Você: Quero adicionar um hábito: ler por 15 minutos antes de dormir
Sereni: Ótimo! O hábito 'Ler Por 15 Minutos Antes De Dormir' foi adicionado. Posso te ajudar com outra coisa?
------------------------------
Você: adicionar hábito: caminhar - 30 minutos por dia
Sereni: Ótimo! O hábito 'Caminhar' foi adicionado. Posso te ajudar com outra coisa?
------------------------------
Você: listar hábitos
Sereni: Seus hábitos atuais:
- Ler Por 15 Minutos Antes De Dormir: Sem detalhes adicionais.
- Caminhar: 30 minutos por dia
------------------------------
Você: lembre-me: tomar vitamina às 9:00
Sereni: Ok, anotei para te lembrar de 'tomar vitamina' às 9:00. Lembre-se que neste momento eu apenas guardo essa informação.
------------------------------
Você: agendar lembrete: consulta médica às 14:30
Sereni: Ok, anotei para te lembrar de 'consulta médica' às 14:30. Lembre-se que neste momento eu apenas guardo essa informação.
------------------------------
Você: listar lembretes
Sereni: Seus lembretes agendados (lembre-se, eu apenas os guardo por enquanto):
- [geral] 09:00: tomar vitamina
- [geral] 14:30: consulta médica
------------------------------
Você: Como posso relaxar agora?
Sereni: Claro! Uma forma simples de relaxar é focar na sua respiração. Encontre uma posição confortável, feche os olhos se quiser, e apenas observe o ar entrando e saindo. Não tente mudar nada, apenas observe por um minuto ou dois. Isso pode ajudar a acalmar a mente.
------------------------------
Você: tchau
Sereni: Que bom que conversamos! Lembre-se que estou aqui sempre que precisar. Cuide-se bem!
