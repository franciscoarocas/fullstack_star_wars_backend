
from typing import Optional

from app.api.IA_Agent.base import IAAgentBase
from app.utils.ia_common import TYPES_QUESTION, ANSWER_QUESTIONS

import random



class IAAgentFake(IAAgentBase):
    """
    Fake IA Agent for testing purposes.
    This class simulates the behavior of an IA Agent without actual implementation.
    """

    def __init__(self):
        super().__init__()

    def __get_prompt_question_type(self, prompt: str) -> Optional[str]:
        """
        Determine the type of question based on the prompt.
        Args:
            prompt (str): The input prompt to analyze.
        Returns:
            str: The type of question (e.g., "open-ended", "yes/no", etc.).
        """
        prompt = prompt.lower()
        for key in TYPES_QUESTION:
            if key in prompt:
                return TYPES_QUESTION[key]
        return None

    def execute_prompt(self, prompt: str) -> str:
        """
        Process a prompt and return a simulated response.
        Args:
            prompt (str): The input prompt to process.
        Returns:
            str: A simulated response based on the type of question.
        """
        question_type = self.__get_prompt_question_type(prompt)
        if question_type is None:
            return "I don't know how to answer that question."
        return f"Yes sure, and example of {question_type} is: {random.choice(ANSWER_QUESTIONS[question_type])}"

    def get_name(self) -> str:
        """
        Get the name of the Fake IA Agent.
        Returns:
            str: The name of the agent.
        """
        return "Fake IA Agent"
