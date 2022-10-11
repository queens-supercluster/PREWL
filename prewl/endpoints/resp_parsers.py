"""
This file contains functions that take a response from hf
and they parse out the response for a given task. For example,
the text_gen_parser collects the result from the first item in the
response json, and in the 'generated_text' attribute. The mask_fill 
parser simply returns the json response.
"""

def text_gen_parser(response, prompt):
    resp = response.json()
    resp = resp[0]['generated_text']
    assert prompt in resp, "Response doesn't contain prompt:\n" % resp
    resp = resp.split(prompt)[1]
    
    from prewl import CONFIG
    if CONFIG.get('newline-delimited', CONFIG['defaults']['newline-delimited']):
        resp = resp.split('\n')[0].strip()
    
    return resp

def mask_fill_parser(response, prompt):
    resp = response.json()
    # assert prompt in resp, "Response doesn't contain prompt:\n" % resp
    return resp
    
resp_parser_dict = {'text_gen_parser': text_gen_parser,
'mask_fill_parser': mask_fill_parser}