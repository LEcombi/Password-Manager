import random
import string

# Function to generate a random password
def generate_password(length=12):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Main block to run the password generator from the command line
if __name__ == "__main__":
    from translate_text import load_config, translate_text
    target_language = load_config()
    print(translate_text("Password Generator", target_language))
    # Prompt the user to enter the desired password length
    pass_length_prompt = translate_text("Enter the desired password length (default is 12):", target_language)
    pass_length = input(pass_length_prompt)
    # Use default length if no input is provided
    if not pass_length:
        pass_length = 12
    else:
        pass_length = int(pass_length)
    # Generate and display the password
    generated_password_text = translate_text("Generated Password:", target_language)
    print(generated_password_text, generate_password(pass_length))