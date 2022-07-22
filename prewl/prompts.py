

class Prompts(object):
    def __init__(self, pattern, examples, output, inputs=None):
        self.examples = examples
        self.inputs = inputs
        self.output = output
        self.pattern = pattern

        if self.inputs is None:
            self.inputs = [inp for inp in self.examples[0].keys() if inp != self.output]

        self.validate()


    def validate(self):
        """Validate the prompt examples"""

        # Non-trivial examples
        assert self.examples, "No examples provided"
        keys = self.examples[0].keys()
        assert keys, "No keys provided"
        assert len(set(keys)) == len(keys), "Duplicate keys in examples"
        keys = set(keys)

        # Each example has the same keys
        for e in self.examples:
            assert set(e.keys()) == keys, "Keys in examples do not match"

        # Inputs and output are distinct and equal to keys
        assert self.output not in self.inputs, "Output can't be an input"
        assert set(self.inputs + [self.output]) == keys, "Inputs and output should equal the keys"

        # Each key appears only once in the pattern
        for k in keys:
            assert 1 == self.pattern.count('{'+k+'}'), f"Key {k} should appear exactly once in pattern"

        # Output appears at the very end of the prompt
        assert self.pattern.strip()[-len('{'+self.output+'}'):] == '{'+self.output+'}', "Output should appear at the end of the pattern"


    def complete(self, prompt_config_entry, include_output=False):
        """
        Complete a prompt given configuration

        :param prompt_config_entry: A dictionary of inputs and (optionally) outputs
        :param include_output: Whether to include the output in the prompt

        """
        if include_output:
            assert set(self.inputs + [self.output]) == set(prompt_config_entry.keys()), "Inputs and output don't match the keys provided"
            return self.pattern.format(**prompt_config_entry)
        else:
            assert set(self.inputs) == set(prompt_config_entry.keys()), "Inputs don't match the keys provided"
            return self.pattern.format(**prompt_config_entry, **{self.output: ''})
