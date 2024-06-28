import os

class FileUtilities:
    @staticmethod 
    def findFilesWithExtension(directory, extension):
        """
        Recursively find all files with a given extension in the directory and its subdirectories. 
        Pass in a tuple of extensions to find more than one type
        
        :param directory: The root directory to start the search from.
        :param extension: The file extension to search for.
        :return: A list of paths to the files with the given extension.
        """
        # Add a period to the extension if it doesn't start with one
        if not extension.startswith('.'):
            extension = '.' + extension

        matching_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    matching_files.append(os.path.join(root, file))
        return matching_files
