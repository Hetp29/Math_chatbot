import json #load intents from json file
import re #module for regular expressions, module in python
import random

with open('intents.json', 'r') as file: 
    intents = json.load(file)
#opens json file using with open(), loads json data
#assigns to variable intents 

def calculate(expression):
    try:
        match = re.match(r"(-?\d+)\s*([-+*/])\s*(-?\d+)$", expression)
        if match:
            val1, operator, val2 = match.groups()

            if operator == '+':
                return int(val1) + int(val2)
            elif operator == '-':
                return int(val1) - int(val2)
            elif operator == '*':
                return int(val1) * int(val2)
            elif operator == '/':
                if int(val2) == 0:
                    return "Cannot divide by 0."
                else:
                    return int(val1) / int(val2)
        else:
            return "Not valid math expression."
    except ValueError as e:
        return f"Error: {e}"

#function for user input 
def chatbot(input_txt):
    for intent in intents_data["intents"]:
        for pattern in intent["patterns"]:
            if re.search(pattern, input_txt, re.IGNORECASE):
                if intent["tag"] == "math":
                    return intent["responses"][0].format(result=calculate(input_txt))
            else:
                return random.choice(intent["responses"])
            
    return "I didn't understand that."

user_input = input("You: ")
response = chatbot(user_input)
print("Bot:", response)
    





