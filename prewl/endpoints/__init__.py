
from prewl.endpoints.gpt3 import GPT3
from prewl.endpoints.manual import Manual
from prewl.endpoints.hf import HF

huggingface_options = {
    'gpt2': 'gpt2',
    'bloom': 'bigscience/bloom',
    'gpt-j-6b': 'EleutherAI/gpt-j-6B',
}

def create_endpoint(ep_type, remote):

    if ep_type in huggingface_options:
        return HF(huggingface_options[ep_type], remote)
    else:
        return {
            'gpt3': GPT3,
            'manual': Manual
        }[ep_type]()
