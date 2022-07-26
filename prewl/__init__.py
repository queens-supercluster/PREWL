
from prewl.prompts import Prompts
from prewl.model import Model

CONFIG = {
    'defaults': {
        'max_length': 100,
        'newline-delimited': False,
        'output_file': 'output.log',
        'gpu': -1,
        'backend': {'service': 'manual', 'remote': False}
    },
}

# Set the configuration for the prewl library
def configure(config):
    global CONFIG
    CONFIG.update(config)
    if 'gpu' in CONFIG and CONFIG['gpu'] in [True, False]:
        CONFIG['gpu'] = {True: 0, False: -1}[CONFIG['gpu']]

def load_prompts(pattern, examples, output, inputs=None):
    return Prompts(pattern, examples, output, inputs)

# Takes a Prompts object and returns a Model object
def train(prompts, resp_func = lambda x: x):
    m = Model(prompts, resp_func)
    m.train()
    return m
