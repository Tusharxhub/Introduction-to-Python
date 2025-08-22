# Implement a context manager FileManager that ensures a file is automatically closed, even if errors occur during file operations. Use it to write to a file and demonstrate its functionality with a try...except block.

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"File {self.filename} closed.")
        # If an exception occurred, it will be propagated unless we return True
        if exc_type:
            print(f"An error occurred: {exc_val}")
        return False   # Re-raise the exception if one happened


# Example usage with try...except
try:
    with FileManager("example.txt", "w") as f:
        f.write("Hello, this is a test line.\n")
        f.write("Writing using our custom FileManager context manager.\n")
        # Force an error for demonstration
        raise ValueError("Simulated error during file write")
except Exception as e:
    print("Caught exception in try...except block:", e)
