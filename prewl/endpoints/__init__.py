
from prewl.endpoints.gpt3 import GPT3
from prewl.endpoints.manual import Manual
from prewl.endpoints.gpt2 import GPT2

def create_endpoint(ep_type):
    return {
        'gpt3': GPT3,
        'manual': Manual,
        'gpt2': GPT2,
    }[ep_type]()
