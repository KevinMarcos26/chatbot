""" 
Bloque: Modelo
"""
import openai


class BotChat():
    """Crea la conexion con la api de openai
    """
    def __init__(self, userName):
        """Constructor del objeto

        Args:
            userName (srt): nombre para el usuario a usar
        """
        
        openai.api_key = "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"
        self.userName = userName
        self.nameAI = "OpenAI"
        self.respuestaTxt = ""
    
    def consulta(self, pregunta):
        """metodo de consulta al bot

        Args:
            pregunta (srt): Mensaje a enviar al bot
        """
        conversacion = ""
        question = f"{self.userName}: {pregunta}"
        conversacion += f"\n{self.userName}: " + question + f"\n{self.nameAI}:"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=conversacion,
            temperature=0.3,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n", f" {self.userName}:", f" {self.nameAI}:"]
        )
        anwer=response.choices[0].text.strip()
        conversacion += anwer 
        self.respuestaTxt = "AI: " + anwer + "\n"