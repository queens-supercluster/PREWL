
from prewl.endpoints.gpt3 import GPT3
from prewl.endpoints.manual import Manual

def create_endpoint(ep_type):
    return {
        'gpt3': GPT3,
        'manual': Manual,
    }[ep_type]()
