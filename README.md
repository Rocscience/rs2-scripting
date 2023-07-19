# Introduction 
This project is the client python library that users can install to interact with RS2 through python. 

# Build and Test
Following the steps to this guide: https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives  
- Run the command below to install the python build module.  
```python -m pip install --upgrade build```  
- Run this command from the same directory where pyproject.toml is located:  
```python -m build```
- Run the command below. After installing, a code will be displayed in the terminal. Using a web browser, go to www.microsoft.com/devicelogin, where you will be prompted to enter the code.
```pip install keyring artifacts-keyring```
- A 'dist' folder should be generated with a .whl file. You can then run the command below to install the project and its dependencies  
```pip install -r requirements.txt```  
 - If the client library has been altered or updated, run the command below to force reinstallation of the packages so that your environment is up to date. 
```pip install -r requirements.txt --force-reinstall```

# Contribute
- Make change to .py file  
- Build and install using requirements.txt, probably in a virtual environment.   
- Select the python interpreter you used to install the package  
- Run a <sampleScript>.py which imports and tests rs2.  
