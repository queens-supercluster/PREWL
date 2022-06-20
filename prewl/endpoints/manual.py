
from prewl.endpoints.base import Endpoint

class Manual(Endpoint):
    def call(self, prompt):
        print("\n\tPlease send the following to an LLM:\n")
        print("+----------------------------------------------------+")
        print(prompt)
        print("+----------------------------------------------------+\n")
        return input("Please enter the response: ")
