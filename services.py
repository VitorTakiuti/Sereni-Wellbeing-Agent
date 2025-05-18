# services.py

import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HabitManager:
    """Gerencia a criação, listagem e acompanhamento (simples) de hábitos."""
    def __init__(self):
        # Usaremos um dicionário simples para armazenar hábitos {nome: detalhes}
        self.habits = {}
        logging.info("HabitManager inicializado.")

    def add_habit(self, name: str, details: str) -> bool:
        """
        Adiciona um novo hábito.

        Args:
            name: O nome do hábito.
            details: Detalhes ou descrição do hábito.

        Returns:
            True se adicionado com sucesso, False se já existir.
        """
        if name in self.habits:
            logging.warning(f"Tentativa de adicionar hábito existente: {name}")
            return False
        self.habits[name] = details
        logging.info(f"Hábito adicionado: {name} - {details}")
        return True

    def list_habits(self) -> str:
        """
        Lista todos os hábitos registrados.

        Returns:
            Uma string formatada com a lista de hábitos, ou mensagem se não houver.
        """
        if not self.habits:
            return "Você ainda não adicionou nenhum hábito. Que tal começar com um pequeno passo?"

        habit_list = "Seus hábitos atuais:\n"
        for name, details in self.habits.items():
            habit_list += f"- {name}: {details}\n"
        return habit_list.strip() # Remove a última linha em branco

    # Métodos futuros poderiam incluir: track_habit_completion, remove_habit, get_habit_progress, etc.


class ReminderService:
    """
    Gerencia o agendamento (apenas armazenamento neste exemplo) e listagem de lembretes.
    NOTA: Este serviço APENAS armazena os lembretes. A lógica para dispará-los
    no horário correto NÃO está implementada aqui e exigiria um agendador
    em segundo plano (como APScheduler, Celery, ou cron jobs do sistema).
    """
    def __init__(self):
        # Usaremos uma lista de dicionários para armazenar lembretes
        # Ex: [{'type': 'medication', 'description': 'tomar remédio X', 'time': '8:00', 'details': 'com comida'}]
        self.reminders = []
        logging.info("ReminderService inicializado.")

    def schedule_reminder(self, reminder_type: str, description: str, time: str, details: str = "") -> bool:
        """
        Agenda um novo lembrete (apenas armazena).

        Args:
            reminder_type: Tipo do lembrete (ex: 'habit', 'medication', 'appointment', 'safety').
            description: Descrição do lembrete.
            time: Horário agendado (string, ex: '8:00', '14:30').
            details: Detalhes adicionais (opcional).

        Returns:
            True se adicionado com sucesso. (Sem validação complexa neste exemplo)
        """
        # Validação simples do horário (poderia ser mais robusta)
        try:
            datetime.datetime.strptime(time, '%H:%M')
        except ValueError:
            logging.warning(f"Formato de horário inválido para lembrete: {time}")
            # Podemos decidir se adiciona mesmo assim ou retorna False
            # Por enquanto, adiciona e deixa a validação para o usuário/implementação futura
            pass # Continua mesmo com formato inválido simples

        new_reminder = {
            'type': reminder_type,
            'description': description,
            'time': time,
            'details': details
        }
        self.reminders.append(new_reminder)
        logging.info(f"Lembrete agendado (armazenado): {new_reminder}")
        return True # Sempre retorna True neste exemplo simples

    def list_reminders(self) -> str:
        """
        Lista todos os lembretes agendados.

        Returns:
            Uma string formatada com a lista de lembretes, ou mensagem se não houver.
        """
        if not self.reminders:
            return "Você não tem nenhum lembrete agendado no momento."

        reminder_list = "Seus lembretes agendados (lembre-se, eu apenas os guardo por enquanto):\n"
        # Ordena por horário para melhor legibilidade
        sorted_reminders = sorted(self.reminders, key=lambda r: r.get('time', ''))

        for reminder in sorted_reminders:
            time = reminder.get('time', 'Horário não especificado')
            description = reminder.get('description', 'Sem descrição')
            details = reminder.get('details', '')
            r_type = reminder.get('type', 'Geral')

            line = f"- [{r_type}] {time}: {description}"
            if details:
                line += f" ({details})"
            reminder_list += line + "\n"

        return reminder_list.strip()

    # Métodos futuros poderiam incluir: remove_reminder, trigger_due_reminders (exige agendador externo)