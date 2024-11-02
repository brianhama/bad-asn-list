def extract_and_save_numbers(file_path, output_file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    extracted_numbers = []
    for line in lines:
        number = line.split(',')[0].strip()
        if number.isdigit():
            extracted_numbers.append(number)

    with open(output_file_path, 'w') as output_file:
        for number in extracted_numbers:
            output_file.write(number + '\n')

# Paths for the input and output files
input_file_path = 'data.txt'  # Replace with your input file name
output_file_path = 'save.txt'  # This will be the name of your output file

# Process the file
extract_and_save_numbers(input_file_path, output_file_path)

