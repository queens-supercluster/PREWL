
from prewl.prompts import Prompts
from prewl.model import Model

CONFIG = {}

# Set the configuration for the prewl library
def configure(config):
    global CONFIG
    CONFIG = config

def load_prompts(pattern, examples, output, inputs=None):
    return Prompts(pattern, examples, output, inputs)

# Takes a Prompts object and returns a Model object
def train(prompts, resp_func = lambda x: x):
    m = Model(prompts, resp_func)
    m.train()
    return m

