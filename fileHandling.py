def process_file():
    try:
        # Ask user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_filename, "r") as file:
            content = file.read()

        # Count words
        words = content.split()
        word_count = len(words)

        # Convert text to uppercase
        processed_text = content.upper()

        # Create a new file for output
        output_filename = "output.txt"
        with open(output_filename, "w") as outfile:
            outfile.write("PROCESSED TEXT:\n")
            outfile.write(processed_text)
            outfile.write(f"\n\nWORD COUNT: {word_count}")

        print(f"✅ Success! Processed content written to '{output_filename}'.")
    
    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
