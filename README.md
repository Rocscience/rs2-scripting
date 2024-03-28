## Introduction 
This project is a library that can be used to interact with RS2 through python.  

### Goal
Each function exposed corresponds to an equivalent operation you could have done through the UI.  
Using this idea, the user should be able to edit models and get results without having to go through the UI at all.
Although only a limited set of functionality is exposed for now, some basic workflows should still be possible. For a list of the functionality we have so far, see [Exposed Functionality](#exposed-functionality).

### Python UI equivalents
Events and workflows done in the UI will have equivalents in the python library.  
Wherever a dialog is shown in the UI, there will be an equivalent class with methods that mimick the dialog's behavior.  
Wherever a warning or error dialog is displayed, an exception will be thrown, or a warning will be displayed in python instead.  
Wherever you can select and manipulate an entity, identifiers can be used in the library to get references to those entities in python and objects will be constructed to help you interface with them.  

### How it works
Each function in the library is a wrapper to make an api call to the Application.  
Objects retrieved through function calls will often not contain any data themselves, but will instead be proxies, allowing you to get information from the objects in the application.  
For this reason, debugging will sometimes be tricky, as not all data will always be available for you to inspect unless you get it and assign it to a variable yourself.  

### Warnings
References can be *invalidated* whenever the corresponding object in the application is destroyed or reloaded. You will need to watch out for expired referenecs and renew them when needed as it can cause crashes or incorrect results if not managed properly. Functions that invalidate objects will always be marked with a warning and will indicate which objects should be re-loaded. 

## Exposed Functionality
The current set of functionality exposed is limited. With this version of the library, you can:  
- Manage files through Open, Close, Save and Compute
- Modfy any Property value and stage factor, except for some user defined materials and statistical properties.
- Get any Mesh result, support result, SSR Critical SRF and query result.
- Add and remove queries (material, history, time)
  
## Getting Started

**Getting started guide**  
https://www.rocscience.com/help/rs2/tutorials/scripting/getting-started-with-rs2-python-scripting  
**First Tutorial**  
https://www.rocscience.com/help/rs2/tutorials/scripting/anchored-sheet-pile-wall

# For Contributors:

## Build
Following the steps to this guide: https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives  
1. Run the command below to install the python build module.    
```python -m pip install --upgrade build```  
2. Run this command from the same directory where pyproject.toml is located:  
```python -m build```
3. Run the command below. After installing, a code will be displayed in the terminal. Using a web browser, go to https://www.microsoft.com/devicelogin, where you will be prompted to enter the code.  
```pip install keyring artifacts-keyring```
4. A 'dist' folder should be generated with a .whl file. You can then run the command below to install the project and its dependencies  
```pip install -r requirements.txt```  

*If the client library has been altered or updated, run the commands below to force reinstallation of the packages so that your environment is up to date.*
1. ```python -m build```  
2. ```pip install -r requirements.txt --force-reinstall```

## Unit Testing

To ensure the project's functionality and maintain code quality, a test suite using the `unittest` framework has been implemented. The documentation for `unittest` can be found at the following link: https://docs.python.org/3/library/unittest.html  

### Creating Unit Tests
**Directory Structure:**   
- Place new .py files for unit testing in the tests directory.
- Save any RS2 files required for testing in the tests/resources directory.

**Handling Test Resources:**  
Instead of directly modifying the base files in tests/resources, create copies of these files in each test file's setup and delete them in the teardown phase. This ensures that the original resources remain intact and unmodified after running the tests.

### Running Unit Test Cases
Before running the tests, make sure you have:
1. Built the RS2 library as explained in the [Build](#build) section.
2. Started the RS2 Modeler.
3. Started the RS2 Interpreter.
4. Started the Server on both the RS2 Modeler and RS2 Interpreter. Select ```DeveloperApp > Start Server``` in each program.

To run all the tests, navigate to the root directory of the project and execute the following command:  
```python -m unittest discover -s tests```  

To run an individual test file, navigate to the root directory of the project and execute the following command with the correct filename:  
```python -m unittest discover -s tests -p "<sampleTestFile>.py"```

To run a sub-folder of tests, navigate to the 'tests' folder, and run:  
```python -m unittest discover -v -s Path/To/Folder```  

**_NOTE:_** To display additional information on the results of the unit tests, pass the `-v` option into the testing command:  
```python -m unittest discover -v -s tests```

## Documentation
The following steps can be taken to regenerate the RS2 Scripting Documentation:
1. Create python a virtual environment. Navigate to the root directory of your workspace and run the commands below:  
```python -m venv venv```
```venv/Scripts/activate```
2. Rebuild the RS2 library in your virtual environment by following the [Build](#build) section.
3. Run the commands below to install Sphinx and the copy button extension:  
```python -m pip install sphinx```
```pip install sphinx-copybutton```
4. Install a LaTeX distribution. MiKTeX Reccomended: https://miktex.org/download   
5. To generate the documentation run the following:  
```python generateAndBuildDocumentation.py```  
Note: you may have to downgrade your ssl to an earlier version to successfuly generate the documentation ```.tex``` file. If you get an ssl error, run the following command:  
```pip install urllib3==1.26.5```
6. Open TeXworks (via MiKTeX) and open the documentation file:  
	```RS2 Python Client Library\docs\_build\pdf\rs2scriptingclientlibrary.tex```
7. In the dropdown menu, set the output to pdfLaTeX.
8. Click the play button to generate the documentation file.
Note: The first time you generate documentation using TeXworks, a package installation window will appear indicating that numerous packages could not be found. Deselect the "Always show this dialog" checkbox and click the install button. 
9. The Documentation in PDF format will be located here: ```RS2 Python Client Library\docs/_build/pdf/rs2scriptingclientlibrary.pdf```

### Adding To Documentation
The following steps can be taken to add a new proxy object to the autogenerated documentation:
1. Ensure automatic generation of the proxy object python files has been completed for the new proxy object. 
2. To include an example code snippet, ensure a docstring is being generated at the top of the base proxy object ```.py``` file, which will link to the example.  
   See Below:    
   ```
	"""
	:ref:`Bolt Example`
	"""
   ```
3. Add your example code snippet to ```C:\Users\CarterComish\source\repos\RS2 Python Client Library\docs\example_code```
4. Open examples.rst and following the format of the existing example links, add a link to your code example. Ensure that your link label matches the link label being generated in Step 2.  
   See Below:  
	```
	.. _Bolt Example:
	```
5. Follow the steps in [Documentation](#documentation) to regenerate the new documentaiton.

## Contribution Guidelines
Contributions are welcomed to improve RS2's Scripting Features. To make a contribution, follow the guidelines below:
1. **Make Changes:** Start by making the necessary changes to the relevant `.py` file(s) to address the task or implement new features.
2. **Install Dependencies:** Install the required dependencies specified in the `requirements.txt` file, as explained in the [Build](#build) section. It is recommended that these dependencies be installed within a virtual environment.
3. **Python Interpreter:** Select the same Python interpreter used to install the package. You can specify the interpreter in your virtual environment or project settings.
4. **Testing:** Thoroughly test your changes to ensure they meet the project's requirements and do not introduce regressions. Consult the [Unit Testing](#unit-testing) section for more information. Include additional test cases to cover modifications to the project.
5. **Pull Request:** After thorough testing and review, submit a pull request which describes the purpose of your changes. After review and approval, merge your changes into the main branch.
