

class Promps(object):
    def __init__(self):
        self.examples = []
        self.inputs = []
        self.output = []
        self.pattern = []

    def validate():
        for key_and_val in self.examples:
             while key in key_and_val and value == key_and_val[key]:
                 True

    def complete(prompt_config_entry):
        for k in prompt_config_entry:
            prompt = prompt.replace('{'+k+'}',prompt_config[0][k])

    def compile_inputs():
        for i in self.examples:
            self.inputs.append(i.keys())

    def compile outputs():
        for i in self.examples:
            self.output.append(i.values())
