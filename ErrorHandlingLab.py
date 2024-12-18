# Error Handling Lab
def read_file_with_error_handling():
    filename = input("ENter the filename: ")
    
    try:
        with open(filename, 'r') as file:
            print("File content:")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        

#Example Usage
read_file_with_error_handling()