## Introduction 
This project is the client python library that users can install to interact with RS2 through python. 

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
```python -m build```
```pip install -r requirements.txt --force-reinstall```

## Unit Testing

To ensure the project's functionality and maintain code quality, a test suite using the `unittest` framework has been implemented. The documentation for `unittest` can be found at the following link: https://docs.python.org/3/library/unittest.html  
Before running the tests, make sure you have installed the RS2 library as explained in the [Build](#build) section.

### Running Unit Test Cases

To run all the tests, navigate to the root directory of the project and execute the following command:  
```python -m unittest discover -s tests```  
*Note:* To display additional information on the results of the unit tests, pass the `-v` option into the testing command:  
```python -m unittest discover -v -s tests```

## Contribution Guidelines
Contributions are welcomed to improve RS2's Scripting Feature. To make a contribution, follow the guidelines below:
1. **Make Changes:** Start by making the necessary changes to the relevant `.py` file(s) to address the task or implement new features.
2. **Install Dependencies:** Install the required dependencies specified in the `requirements.txt` file, as explained in the [Build](#build) section. It is reccomended that these dependancies be installed within a virtual environment.
3. **Python Interpreter:** Select the same Python interpreter used to install the package. You can specify the interpreter in your virtual environment or project settings.
4. **Testing:** Thoroughly test your changes to ensure they meet the project's requirements and do not introduce regressions. Consult the [Unit Testing](#unit-testing) section for more information. Include additional test cases to cover modifications to the project.
5. **Pull Request:** After thorough testing and review, submit a pull request. Describe the purpose of your changes and reference any related issues. After review and approval, merge your changes into the main branch.
