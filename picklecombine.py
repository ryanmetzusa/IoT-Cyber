import pickle
import os

def concatenate_files(input_directory, output_file):
    data = bytearray()

    for filename in sorted(os.listdir(input_directory)):
        if filename.endswith(".pkl"):
            file_path = os.path.join(input_directory, filename)

            with open(file_path, 'rb') as f:
                chunk_data = f.read()
                data.extend(chunk_data)

    with open(output_file, 'wb') as f:
        f.write(data)

if __name__ == "__main__":
    input_directory = "INPUT LOCATION"  # Replace with your directory path
    output_file = "OUTPUT LOCATION"  # Replace with your desired output file

    concatenate_files(input_directory, output_file)
