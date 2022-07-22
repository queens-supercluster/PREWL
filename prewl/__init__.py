
from prewl.prompts import Prompts
from prewl.model import Model

CONFIG = {
    'defaults': {
        'max_length': 100,
        'newline-delimited': False,
    },
}

# Set the configuration for the prewl library
def configure(config):
    global CONFIG
    CONFIG.update(config)

def load_prompts(pattern, examples, output, inputs=None):
    return Prompts(pattern, examples, output, inputs)

# Takes a Prompts object and returns a Model object
def train(prompts, resp_func = lambda x: x):
    m = Model(prompts, resp_func)
    m.train()
    return m

def silence_tf():
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    import tensorflow as tf
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
