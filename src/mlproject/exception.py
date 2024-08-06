import sys
from src.mlproject.logger import logging


class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_details)

    def __str__(self):
        return self.error_message    