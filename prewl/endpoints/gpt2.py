
import contextlib, sys

from prewl.endpoints.base import Endpoint

class GPT2(Endpoint):

    def call(self, prompt):

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

                generator = transformers.pipeline('text-generation', model='gpt2', device=device)

                completions = generator(prompt,
                                        max_length=max_length,
                                        num_return_sequences=1,
                                        return_full_text=False,
                                        clean_up_tokenization_spaces=True)

                resp = completions[0]['generated_text']

                if CONFIG.get('newline-delimited', CONFIG['defaults']['newline-delimited']):
                    resp = resp.split('\n')[0].strip()

        return resp
