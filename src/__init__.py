
from prompts import Prompts
from model import Model

#prompt example:PROMPTS = """
#[
#    {
#        "text": "I really don't like this movie.",
#        "sentiment": "negative"
 #   },
 #   
#    {
 #       "text": "This flick was sick!",
  #      "sentiment": "positive"
   # },
#
 #   {
  #      "text": "It was ok. I've seen better, though.",
   #     "sentiment": "neutral"
    #}
#]
#"""

# Return a Prompts objects
# prompt = """ """"
#line to read the JSON file
# create object to load the file json.loads(prompt) 
#.loads() needs to load a string

# example of how to parse a JSON file.
#with open('path_to_file/person.json', 'r') as f:
#  data = json.load(f)
#print(data)

def load_prompts(prompt_config, pattern):
    #parse the prompt into seperate {}
    #prompt_list = append to a list of individual prompts
    #loop through each prompt to append each text to a list of texts
    
    #add each sentiment to a list of sentiments
    #name of list (sentiments) is changed according to prompt (can be another label)
    #we have a list of texts and a list of responses (sentiments or other)
    
    pass

# Takes a Prompts object and returns a Model object
def train(prompts):
    pass
    
