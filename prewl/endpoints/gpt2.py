from prewl.endpoints.base import Endpoint

class GPT2(Endpoint):
    
    def call(self, prompt):
        # Avoids warnings.
        import os
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        import tensorflow as tf
        tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

        from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        
        # Add the EOS token as PAD token to avoid warnings.
        model = TFGPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

        # Encode context the text generation is conditioned to.
        input_ids = tokenizer.encode(prompt, return_tensors='tf')

        # Generates text until the output length using greedy search as the decoding method.
        greedy_output = model.generate(input_ids, max_length=100)

        print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))

