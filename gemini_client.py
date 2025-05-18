# gemini_client.py

import google.generativeai as genai
import logging # Para logar possíveis erros ou informações

# Configura o logging básico
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GeminiClient:
    """
    Cliente para interagir com a API do Google Gemini.
    Gerencia a configuração e a sessão de chat.
    """
    def __init__(self, api_key: str, model_name: str):
        """
        Inicializa o cliente Gemini.

        Args:
            api_key: A chave de API do Google AI Studio.
            model_name: O nome do modelo Gemini a ser usado.
        """
        if not api_key or api_key == "SUA_CHAVE_DE_API_AQUI":
            logging.error("Chave de API do Google não configurada. Por favor, edite config.py.")
            raise ValueError("Chave de API do Google não configurada.")

        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(model_name)
            self.chat = self.model.start_chat(history=[]) # Inicia uma sessão de chat
            logging.info(f"Cliente Gemini configurado com sucesso para o modelo: {model_name}")
        except Exception as e:
            logging.error(f"Erro ao configurar o cliente Gemini: {e}")
            raise

    def send_message(self, message: str) -> str:
        """
        Envia uma mensagem para o modelo Gemini e retorna a resposta.

        Args:
            message: A mensagem de texto do usuário.

        Returns:
            A resposta de texto do Gemini, ou uma mensagem de erro.
        """
        try:
            # Adiciona um prompt de sistema ou context inicial aqui, se necessário
            # Ex: prompt_parts = ["Você é um assistente de bem-estar amigável e paciente. ", message]
            # response = self.chat.send_message(prompt_parts)

            # Para este exemplo simples, enviamos apenas a mensagem do usuário
            response = self.chat.send_message(message)
            logging.info(f"Mensagem enviada para Gemini. Resposta recebida.")
            return response.text
        except Exception as e:
            logging.error(f"Erro ao enviar mensagem para Gemini: {e}")
            return "Desculpe, tive um problema para entender isso agora. Poderia tentar novamente?"

    def get_chat_history(self):
        """Retorna o histórico da conversa atual."""
        return self.chat.history