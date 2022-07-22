from prewl.endpoints.base import Endpoint

class GPT2(Endpoint):

    def call(self, prompt):

        from prewl import CONFIG, silence_tf

        silence_tf()

        from transformers import GPT2TokenizerFast
        tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

        max_length = len(prompt) + CONFIG.get('max_length', CONFIG['defaults']['max_length'])

        from transformers import pipeline
        generator = pipeline('text-generation', model='gpt2')

        completions = generator(prompt,
                                max_length=max_length,
                                num_return_sequences=1,
                                return_full_text=False,
                                clean_up_tokenization_spaces=True,
                                pad_token_id=tokenizer.eos_token_id)

        resp = completions[0]['generated_text']

        if CONFIG.get('newline-delimited', CONFIG['defaults']['newline-delimited']):
            resp = resp.split('\n')[0].strip()

        return resp
