def modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
            
            #modify Content: COnvert to uppercase
            modified_content = content.upper()
            
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
            
        print(f"Content from {input_file} has been modified and written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occured: {e}")
        

# Example Usage
input_filename = "example.txt"
output_filename = "modified_example.txt"
modify_file(input_filename, output_filename)