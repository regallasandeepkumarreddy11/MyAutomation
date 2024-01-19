import os

class LargeFileCreator:
    def __init__(self, fileName, sizeGB):
        self.fileName = fileName
        self.sizeGB = sizeGB
        self.filePath = os.path.join(os.getcwd(), self.fileName)

    def create_large_file(self):
        # Define the block size (in bytes) for each iteration
        blockSize = 1024 * 1024  # 1 MB

        # Calculate the total size in bytes
        sizeBytes = self.sizeGB * 1024**3

        # Open the file in binary write mode
        with open(self.filePath, 'wb') as file:
            # Write blocks of data until the total size is reached
            while file.tell() < sizeBytes:
                # Calculate the remaining bytes to write
                remainingBytes = sizeBytes - file.tell()

                # Determine the block size for this iteration
                currentBlockSize = min(remainingBytes, blockSize)

                # Create a block of null bytes
                nullBlock = b'\x00' * currentBlockSize

                # Write the block to the file
                file.write(nullBlock)

        print(f"File created successfully: {self.filePath}")

# Specify the file name and size (1 GB in this case)
fileName = 'your_file.dat'
fileSizeGB = 1

# Instantiate the class
fileCreator = LargeFileCreator(fileName, fileSizeGB)

# Call the method to create the file
fileCreator.create_large_file()
