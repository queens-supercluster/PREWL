
import contextlib, sys

from prewl.endpoints.base import Endpoint

class HF(Endpoint):

    def __init__(self, model, remote):
        self.model = model
        self.remote = remote

    def call(self, prompt):
        if self.remote:
            return self._call_remote(prompt)
        else:
            return self._call_local(prompt)

    def _call_remote(self, prompt):
        import requests

        from prewl import CONFIG
        assert 'token' in CONFIG['backend'], "Must provide 'token' in the 'backend' configuration to call huggingface remotely."
        token = CONFIG['backend']['token']

        params = {
            'max_new_tokens': min(250, CONFIG.get('max_length', CONFIG['defaults']['max_length']))
        }

        options = {
            'use_gpu': CONFIG.get('gpu', CONFIG['defaults']['gpu']),
            'use_cache': False
        }

        API_URL = f"https://api-inference.huggingface.co/models/{self.model}"
        headers = {"Authorization": f"Bearer {token}"}

        response = requests.post(API_URL, headers=headers, json={"inputs": prompt, "parameters": params, "options": options})

        resp = response.json()[0]['generated_text']
        assert prompt in resp, "Response doesn't contain prompt:\n" % resp
        resp = resp.split(prompt)[1]
        
        if CONFIG.get('newline-delimited', CONFIG['defaults']['newline-delimited']):
            resp = resp.split('\n')[0].strip()
        
        return resp
            

    def _call_local(self, prompt):

        from prewl import CONFIG

        try:
            import transformers
        except:
            print("\n\tError: For this endpoint, you must install the transformers package\n")
            exit(1)
        
        transformers.utils.logging.set_verbosity(transformers.logging.ERROR)

        # Squash the hugging face outputs
        log_output = CONFIG.get('output_file', CONFIG['defaults']['output_file'])
        with open(log_output, 'w') as f:
            with contextlib.redirect_stdout(f):

                max_length = len(prompt) + CONFIG.get('max_length', CONFIG['defaults']['max_length'])
                device = CONFIG.get('gpu', CONFIG['defaults']['gpu'])

                generator = transformers.pipeline('text-generation', model=self.model, device=device)

                completions = generator(prompt,
                                        max_length=max_length,
                                        num_return_sequences=1,
                                        clean_up_tokenization_spaces=True)

                resp = completions[0]['generated_text']

                assert prompt in resp, "Response doesn't contain prompt:\n" % resp
                resp = resp.split(prompt)[1]

                if CONFIG.get('newline-delimited', CONFIG['defaults']['newline-delimited']):
                    resp = resp.split('\n')[0].strip()

        return resp
