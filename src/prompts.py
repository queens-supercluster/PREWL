

class Promps(object):
    def __init__(self):
	self.examples = []
	self.inputs = []
	self.output = []
	self.pattern = []
    def validate():
	for key_and_val in self.examples:
		if key in key_and_val and value == key_and_val[key]:
			#I want to say while this is true, pass to the next key
			pass
    def complete(prompt_config_entry):
	for k in prompt_config_entry:
		prompt = prompt.replace('{'+k+'}',prompt_config[0][k])
	
