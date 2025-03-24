def process_file():
    try:
        # Ask the user for a filename
        filename = input("Enter the filename to read: ")

        # Open the file for reading
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (Example: Append a new line)
        modified_content = content + "\n[Modified Version]"

        # Create a new file and write modified content
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been saved to '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
process_file()
