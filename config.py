# config.py

# Cole sua chave de API do Google AI Studio aqui.
# É ALTAMENTE recomendado carregar isso de variáveis de ambiente
# ou de um arquivo .env em um projeto real por questões de segurança.
# Para este exemplo, vamos colocá-la diretamente, mas esteja ciente dos riscos.
GOOGLE_API_KEY = "AIzaSyCzpvIYDhLBBm4lQWIj2aOV8GY-Trw4uUU" # <<< SUBSTITUA PELA SUA CHAVE REAL

# Modelo Gemini a ser utilizado
GEMINI_MODEL_NAME = "gemini-1.5-flash-latest"

# --- Configurações Opcionais ---
# Nome do agente (pode ser usado nas respostas)
AGENT_NAME = "Sereni"

# Mensagem de boas-vindas
WELCOME_MESSAGE = f"Olá! Eu sou o {AGENT_NAME}, seu companheiro de bem-estar. Como posso te ajudar hoje?"

# Mensagem de despedida
FAREWELL_MESSAGE = f"Que bom que conversamos! Lembre-se que estou aqui sempre que precisar. Cuide-se bem!"

# Limiares para detecção de intenção simples (ajuste conforme necessário)
ADD_HABIT_KEYWORDS = ["adicionar hábito", "novo hábito", "criar hábito"]
LIST_HABITS_KEYWORDS = ["listar hábitos", "meus hábitos", "quais meus hábitos"]
SCHEDULE_REMINDER_KEYWORDS = ["agendar lembrete", "novo lembrete", "me lembre"]
LIST_REMINDERS_KEYWORDS = ["listar lembretes", "meus lembretes", "quais meus lembretes"]