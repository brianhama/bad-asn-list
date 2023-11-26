#author: Chandima Galahitiyawa
#date: 27th Nov 2023

def create_formatted_strings(input_file_path, max_length=4096):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    all_expressions = []
    current_expression = ""
    for line in lines:
        number = line.strip()
        part = f"(ip.geoip.asnum eq {number})"
        # Check if adding the next part will exceed the limit
        if len(current_expression) + len(part) + 4 > max_length:  # 4 for ' or ' length
            all_expressions.append(current_expression.rstrip(' or '))
            current_expression = part
        else:
            current_expression += part + ' or '

    # Add the last expression if it's not empty
    if current_expression:
        all_expressions.append(current_expression.rstrip(' or '))

    return all_expressions

# Path for the input file
input_file_path = 'save.txt'  # Replace with your file path

# Create the formatted strings
formatted_strings = create_formatted_strings(input_file_path)

# Output the result to a file or print it
for index, expression in enumerate(formatted_strings, start=1):
    print(f"Expression {index}:\n{expression}\n")
    # Optionally, write each expression to a separate file
    with open(f'output_expression_{index}.txt', 'w') as file:
        file.write(expression)
