import os

class FileUtilities:
    @staticmethod 
    def findFilesWithExtension(directory:str, extension:str):
        """
        Recursively find all files with a given extension in the directory and its subdirectories. 
    
        Args:
            directory(str): full path to folder directory to carry out search
            extension(str): file extension for search with or without the period at the beginning

        Raises: None

        Returns: 
            list of file paths found with extension
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
