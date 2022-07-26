
from prewl.endpoints import create_endpoint

class Model(object):

    def __init__(self, prompts, resp_func):
        self.prompts = prompts
        self.resp_func = resp_func

    def train(self):
        self._PROMPT = ''
        for e in self.prompts.examples:
            self._PROMPT += self.prompts.complete(e, include_output=True)

    def infer(self, input):
        """
        Inference function for the model. Should call the appropriate backend.

        :param input: The input to the prompt. May be either a dictionary or a string.
        """

        # (1) Build the prompt

        # If input is a dictionary, then infer the output
        if isinstance(input, dict):
            prompt = self._PROMPT + self.prompts.complete(input)
        elif isinstance(input, str):
            assert 1 == len(self.prompts.inputs), "If input is a string, then there should be only one input"
            prompt = self._PROMPT + self.prompts.complete({self.prompts.inputs[0]: input})
        prompt = prompt.strip() + ' '

        # (2) Call the appropriate backend
        from prewl import CONFIG
        backend = CONFIG.get('backend', CONFIG['defaults']['backend'])

        assert 'service' in backend, "Backend must at least include 'service'."

        ep = create_endpoint(backend['service'], remote = ('remote' in backend and backend['remote']))

        resp = ep.call(prompt)

        # (3) Parse the output and return
        return self.resp_func(resp)
