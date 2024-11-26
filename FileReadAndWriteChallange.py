def modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
            
            #modify Content: COnvert to uppercase
            modified_content = content.upper()
            
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
            
        print