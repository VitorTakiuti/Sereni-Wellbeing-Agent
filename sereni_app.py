# sereni_app.py

import sys
import logging
from config import (
    GOOGLE_API_KEY, GEMINI_MODEL_NAME, AGENT_NAME,
    WELCOME_MESSAGE, FAREWELL_MESSAGE,
    ADD_HABIT_KEYWORDS, LIST_HABITS_KEYWORDS,
    SCHEDULE_REMINDER_KEYWORDS, LIST_REMINDERS_KEYWORDS
)
from gemini_client import GeminiClient
from services import HabitManager, ReminderService

# Configura o logging para exibir informações
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def detect_simple_intent(text: str) -> tuple[str, str]:
    """
    Detecta intenções simples baseadas em palavras-chave no texto do usuário.
    Retorna a intenção detectada e o restante do texto.

    Args:
        text: O texto de entrada do usuário.

    Returns:
        Uma tupla (intent, remaining_text). Intent pode ser 'add_habit',
        'list_habits', 'schedule_reminder', 'list_reminders', ou 'general_chat'.
        remaining_text é a parte do texto após a palavra-chave da intenção (se aplicável).
    """
    lower_text = text.lower()

    for keyword in ADD_HABIT_KEYWORDS:
        if keyword in lower_text:
            # Assume que o nome/detalhe do hábito vem depois da palavra-chave
            parts = lower_text.split(keyword, 1) # Divide apenas na primeira ocorrência
            remaining = parts[1].strip() if len(parts) > 1 else ""
            logging.info(f"Intenção detectada: add_habit com restante '{remaining}'")
            return 'add_habit', remaining

    for keyword in LIST_HABITS_KEYWORDS:
        if keyword in lower_text:
            logging.info("Intenção detectada: list_habits")
            return 'list_habits', ""

    for keyword in SCHEDULE_REMINDER_KEYWORDS:
        if keyword in lower_text:
             # Assume que a descrição/horário vem depois da palavra-chave
            parts = lower_text.split(keyword, 1)
            remaining = parts[1].strip() if len(parts) > 1 else ""
            logging.info(f"Intenção detectada: schedule_reminder com restante '{remaining}'")
            return 'schedule_reminder', remaining

    for keyword in LIST_REMINDERS_KEYWORDS:
        if keyword in lower_text:
            logging.info("Intenção detectada: list_reminders")
            return 'list_reminders', ""

    logging.info("Intenção detectada: general_chat")
    return 'general_chat', text # Se nenhuma intenção específica, é conversa geral


def parse_habit_details(text: str) -> tuple[str, str]:
    """
    Tenta extrair nome e detalhes de um hábito do texto.
    Formato esperado simples: "nome do habito - detalhes" ou apenas "nome do habito".

    Args:
        text: O texto contendo detalhes do hábito.

    Returns:
        Uma tupla (name, details).
    """
    parts = text.split('-', 1)
    name = parts[0].strip().title() # Capitaliza a primeira letra de cada palavra no nome
    details = parts[1].strip() if len(parts) > 1 else "Sem detalhes adicionais."
    logging.info(f"Detalhes de hábito parsed: Nome='{name}', Detalhes='{details}'")
    return name, details

def parse_reminder_details(text: str) -> tuple[str, str]:
    """
    Tenta extrair descrição e horário de um lembrete do texto.
    Formato esperado simples: "descrição às horário" ou "descrição horario".

    Args:
        text: O texto contendo detalhes do lembrete.

    Returns:
        Uma tupla (description, time).
    """
    # Tenta encontrar " às " ou " as " como separador
    if " às " in text:
        parts = text.split(" às ", 1)
    elif " as " in text: # Permite erro de digitação comum
        parts = text.split(" as ", 1)
    else:
        # Se não encontrar separador, tenta dividir pela última palavra (assumindo ser o horário)
        parts = text.rsplit(" ", 1) # Divide do final, 1 vez

    description = parts[0].strip() if parts else "Lembrete sem descrição"
    time = parts[1].strip() if len(parts) > 1 else "Horário não especificado"

    logging.info(f"Detalhes de lembrete parsed: Descrição='{description}', Horário='{time}'")
    return description, time

def main():
    """Função principal para executar o chatbot Sereni."""
    print(WELCOME_MESSAGE)
    print("-" * 30) # Separador visual

    try:
        # Inicializa os componentes
        gemini_client = GeminiClient(api_key=GOOGLE_API_KEY, model_name=GEMINI_MODEL_NAME)
        habit_manager = HabitManager()
        reminder_service = ReminderService()
        # accessibility_helper = AccessibilityHelper() # Futuramente, um módulo de acessibilidade

        # Loop principal de interação
        while True:
            user_input = input("Você: ").strip() # Remove espaços em branco no início/fim

            if user_input.lower() in ['sair', 'tchau', 'adeus']:
                print(FAREWELL_MESSAGE)
                break # Sai do loop

            if not user_input:
                continue # Ignora entrada vazia

            # 1. Detectar intenção do usuário (simplificado)
            intent, remaining_text = detect_simple_intent(user_input)

            # 2. Processar a intenção
            sereni_response = ""
            if intent == 'add_habit':
                if remaining_text:
                    habit_name, habit_details = parse_habit_details(remaining_text)
                    if habit_name:
                        if habit_manager.add_habit(habit_name, habit_details):
                            sereni_response = f"Ótimo! O hábito '{habit_name}' foi adicionado. Posso te ajudar com outra coisa?"
                        else:
                            sereni_response = f"Você já tem um hábito chamado '{habit_name}'. Quer tentar adicionar outro?"
                    else:
                         sereni_response = "Para adicionar um hábito, diga 'adicionar hábito:' seguido do nome e detalhes (opcional). Por exemplo: 'adicionar hábito: beber água - 8 copos por dia'."
                         # Podemos pedir ao Gemini para refinar a resposta:
                         # sereni_response = gemini_client.send_message(f"O usuário tentou adicionar um hábito mas não especificou o nome após 'adicionar hábito'. Responda de forma amigável explicando como adicionar um hábito. Contexto: {user_input}")

                else:
                     sereni_response = "O que você gostaria de adicionar como hábito? Diga 'adicionar hábito:' e o nome."
                     # Pedir ajuda ao Gemini:
                     # sereni_response = gemini_client.send_message(f"O usuário disse 'adicionar hábito' mas não completou a frase. Peça a ele para especificar o hábito de forma amigável. Contexto: {user_input}")

            elif intent == 'list_habits':
                sereni_response = habit_manager.list_habits()
                # Podemos pedir ao Gemini para adicionar um toque motivacional à lista:
                # sereni_response += "\n" + gemini_client.send_message("Dado a lista acima, escreva uma frase curta e motivacional sobre manter hábitos saudáveis.")

            elif intent == 'schedule_reminder':
                 if remaining_text:
                     reminder_description, reminder_time = parse_reminder_details(remaining_text)
                     if reminder_description and reminder_time != "Horário não especificado":
                        # Neste exemplo simples, o tipo é 'geral'. Em uma versão real, a NLU
                        # precisaria inferir se é medicamento, consulta, etc.
                        if reminder_service.schedule_reminder('geral', reminder_description, reminder_time):
                            sereni_response = f"Ok, anotei para te lembrar de '{reminder_description}' às {reminder_time}. Lembre-se que neste momento eu apenas guardo essa informação."
                     else:
                          sereni_response = "Para agendar um lembrete, diga 'lembre-me:' seguido da descrição e horário. Exemplo: 'lembre-me: tomar remédio às 8:00'."
                          # Pedir ajuda ao Gemini:
                          # sereni_response = gemini_client.send_message(f"O usuário tentou agendar um lembrete mas não especificou a descrição e horário após 'lembre-me:'. Responda de forma amigável explicando o formato. Contexto: {user_input}")
                 else:
                      sereni_response = "O que você gostaria que eu te lembrasse e a que horas? Diga 'lembre-me:' e os detalhes."
                      # Pedir ajuda ao Gemini:
                      # sereni_response = gemini_client.send_message(f"O usuário disse 'lembre-me' mas não completou. Peça os detalhes do lembrete de forma amigável. Contexto: {user_input}")


            elif intent == 'list_reminders':
                 sereni_response = reminder_service.list_reminders()
                 # Podemos pedir ao Gemini para adicionar um toque amigável:
                 # sereni_response += "\n" + gemini_client.send_message("Dado a lista de lembretes acima, escreva uma frase curta encorajando o usuário a seguir a rotina.")


            else: # 'general_chat'
                # Se não detectou uma intenção específica, envia a mensagem para o Gemini para conversa geral
                logging.info("Enviando para Gemini para conversa geral...")
                sereni_response = gemini_client.send_message(user_input)

            # 3. Exibir a resposta (futuramente, aplicar adaptações de acessibilidade aqui)
            # sereni_response = accessibility_helper.adapt_text(user_id, sereni_response) # Exemplo futuro
            print(f"{AGENT_NAME}: {sereni_response}")

            print("-" * 30) # Separador visual

    except ValueError as ve:
        print(f"Erro de configuração: {ve}")
        print("Por favor, verifique o arquivo config.py e sua chave de API.")
        sys.exit(1) # Sai do programa com erro
    except Exception as e:
        logging.exception("Ocorreu um erro inesperado:")
        print(f"Desculpe, ocorreu um erro inesperado: {e}")
        print("Por favor, tente novamente mais tarde.")
        sys.exit(1) # Sai do programa com erro


if __name__ == "__main__":
    main()