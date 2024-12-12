import os
import openai
from openai import OpenAI
from pyswip import Prolog 
# pyswip is a python module that acts as a wrapper to interact with the actual interpreter,
# SWI-Prolog, 



# INITS
model_engine = "gpt-4o-mini"
client = OpenAI()
natural_language_text = "Hans is a fan of great musicians. Jacob Collier is a great musician. Hans is a fan of Jakob Collier."

messages=[
        {	"role": "system", 
        	"content": "You are test subject translating information to prolog."},
        {
            "role": "user", 
            "content": f"Translate the following text to Prolog:\n\n{natural_language_text}"
        }
    ]

# Function to translate natural language to Prolog using OpenAI
def translate_to_prolog(natural_language_text):
    # Define prompt for OpenAI API
    

    # Call OpenAI API
    response = client.chat.completions.create(
    	model=model_engine, 
    	messages=messages)

    # Extract Prolog code from response
    print(response)
    # prolog_code = response.choices[0].message
    prolog_code = response.choices[0].message.content
    
    # this syntax retrieves the text content of the AI's reply from the response object 
	# and removes unnecessary whitespace around it
	
	# response objects are dictionaries with the model's response being usually choice one
	# it's hard to read output directly but accessing is very object-oriented
    
    print("Generated Prolog Code:\n", prolog_code)
    return prolog_code

# Function to check if the Prolog code runs
def check_prolog_code(prolog_code):
    prolog = Prolog()

    try:
        # Assert the Prolog code directly into the Prolog environment
        for clause in prolog_code.split(". "):  # Split clauses by period
            if clause.strip():
                prolog.assertz(clause.strip())
        # Run a test query to ensure it was loaded successfully
        query_result = list(prolog.query("true"))
        if query_result:
            print("Prolog code executed successfully.")
        else:
            print("Prolog code did not execute as expected.")
    except Exception as e:
        print("Error running Prolog code:", e)

# Main function
def main():
    # Example natural language input
    natural_language_input = "A parent is someone who has a child. Check if Mary is a parent of John."

    # Step 1: Translate natural language to Prolog
    prolog_code = translate_to_prolog(natural_language_input)

    # Step 2: Check if Prolog code runs
    check_prolog_code(prolog_code)

if __name__ == "__main__":
    main()

