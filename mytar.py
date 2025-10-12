import os 
from buffers import BufferedWriter, BufferedReader 
from framing import FramedWriter, FramedReader
import sys

if __name__ == "__main__":
    # Check if the user specified 'c' (create) or 'x' (extract)
    if len(sys.argv) < 2:
        # Not enough arguments, print error to stderr
        os.write(2, b"Usage: mytar.py [c|x] [file1...]\n")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == 'c':
        # --- CREATE MODE ---
        files_to_add = sys.argv[2:]
        # Create a writer that will write to stdout.
        writer = FramedWriter() 
        for filename in files_to_add:
            try:
                writer.write_file(filename)
            except FileNotFoundError:
                os.write(2, f"Error: File '{filename}' not found.\n".encode())
        writer.close()

    elif mode == 'x':
        # --- EXTRACT MODE ---
        # Create a reader that will read from stdin.
        reader = FramedReader()
        while reader.read_next_file():
            pass # The method does all the work.
        reader.close()
    else:
        os.write(2, f"Error: Unknown mode '{mode}'\n".encode())
        sys.exit(1)