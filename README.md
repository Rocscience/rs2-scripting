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

# Documentation
The following steps can be taken to regenerate the RS2 Scripting Documentation:
1. Create python a virtual environment. Navigate to the root directory of your workspace and run the commands below:  
```python -m venv venv```
```venv/Scripts/activate```
2. Rebuild the RS2 library in your virtual environment by following the [Build And Test](#build-and-test) section.
3. Run the command below to install Sphinx:  
```python -m pip install sphinx```
4. Install a LaTeX distribution: https://www.latex-project.org/. MiKTeX Reccomended. 
5. To generate the documentation run the following:  
```python generateAndBuildDocumentation.py```
Note: you may have to downgrade your ssl to an earlier version to successfuly generate the documentation ```.tex``` file. If you get an ssl error, run the following command:  
```pip install urllib3==1.26.5```
6. Open TeXworks (via MiKTeX) and open the documentation file:  
	```RS2 Python Client Library\docs\_build\pdf\rs2scriptingclientlibrary.pdf```
7. In the dropdown menu, set the output to pdfLaTeX.
8. Click the play button to generate the documentation file.


# Contribute
- Make change to .py file  
- Build and install using requirements.txt, probably in a virtual environment.   
- Select the python interpreter you used to install the package  
- Run a <sampleScript>.py which imports and tests rs2.
