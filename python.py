# Qn 1: File Read & Write Challenge

def read_and_write_file(maokid, maokidwell):
    try:
        with open(maokid, 'r') as input_file:
            content = input_file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        with open(maokidwell, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Modified content written to {maokidwell}")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{maokid}' or write to '{maokidwell}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Qn 2: Error Handling Lab

def main():
    maokid = input("Enter the input filename: ")
    maokidwell = input("Enter the output filename: ")
    read_and_write_file(maokid, maokidwell)

if __name__ == "__main__":
    main()
