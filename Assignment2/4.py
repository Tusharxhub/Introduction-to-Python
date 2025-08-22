# Implement a context manager FileManager that ensures a file is automatically closed, even if errors occur during file operations. Use it to write to a file and demonstrate its functionality with a try...except block.

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Error occurred: {exc_value}")

# Example usage
if __name__ == "__main__":
    try:
        with FileManager("test.txt", "w") as f:
            f.write("Hello, World!")
            # Simulate an error
            1 / 0
    except Exception as e:
        print(f"Exception caught: {e}")