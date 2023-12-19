import pickle
import os

def split_large_file(input_file, output_directory, chunk_size):
    with open(input_file, 'rb') as f:
        data = f.read()

    num_chunks = (len(data) + chunk_size - 1) // chunk_size

    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size
        output_file = os.path.join(output_directory, f"chunk_{i + 1}.pkl")

        with open(output_file, 'wb') as f:
            f.write(data[start_idx:end_idx])

if __name__ == "__main__":
    input_file = "INPUT LOCATION"  # Replace with your file path
    output_directory = "OUTPUT LOCATION"  # Replace with your desired output directory
    chunk_size = 25 * 1024 * 1024  # 25MB in bytes

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    split_large_file(input_file, output_directory, chunk_size)
