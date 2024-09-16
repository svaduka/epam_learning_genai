from chat.openai_integration import generate_response
from prompts import test_prompts as tp

# Global variables
prompt_type = None
current_context = None

def extract_item_from_user_input(user_input):
    global prompt_type  # Declare as global to modify the global variable
    if not user_input:
        return None
    
    if prompt_type:
        return prompt_type

    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching

    if "movie" in user_input:
        prompt_type = "movie"
    elif "book" in user_input:
        prompt_type = "books"
    elif "product" in user_input:
        prompt_type = "products"
    elif "restaurant" in user_input:
        prompt_type = "restaurants"
    
    return prompt_type

def get_prompt_template(prompt_type):
    if prompt_type.casefold() == "books".casefold():
        return tp.get_book_template()
    elif prompt_type.casefold() == "products".casefold():
        return tp.get_product_template()
    elif prompt_type.casefold() == "restaurants".casefold():
        return tp.get_restaurant_template()

def process_user_input(user_input):
    global prompt_type  # Declare as global to modify the global variable
    if prompt_type is None:
        prompt_type = extract_item_from_user_input(user_input=user_input)
    
    if prompt_type is None:
        return "Sorry, I couldn't identify the type of item you're looking for."

    print(f"Using prompt type: {prompt_type}")
    prompt_template = get_prompt_template(prompt_type)
    print(f"Using the prompt template: {prompt_template}")

    return generate_response(prompt_template, user_input)