
import os
import re
import csv

from rs2.modeler import Model
from rs2.modeler.properties.PropertyEnums import *

from rs2.modeler.properties.DiscreteFunction import DiscreteFunction

"""
Example of how you might write helper classes to support creating
discrete function in RS2 using company-specific data files.

Please read each class carefully. Only the main functionalities required
for the Statistical Analysis example are defined below. 

You may need to add functionality depending on your project requirements
"""

class DiscreteFunctionDataPoint:
    """
    The DiscreteFunctionDataPoint object stores the table values to generate
    a discrete strength function in RS2.

    Args:
        x(float): x coordinate
        y(float): y coordinate
        
        Mohr-Coulomb parameters:
            coh(float): cohesion
            phi(flaot): friction angle
        
        Stiffness parameters:
            mod(float): elastic modulus
            res_mod(float): residual elastic modulus

    Attributes: 
        x(float): x coordinate
        y(float): y coordinate
        
        Mohr-Coulomb parameters:
            coh(float): cohesion
            phi(flaot): friction angle
        
        Stiffness parameters:
            mod(float): elastic modulus
            res_mod(float): residual elastic modulus
        
    """
    def __init__(self, **kwargs):
        self.x = float(kwargs.get('x', 0))
        self.y = float(kwargs.get('y', 0))
        self.coh = float(kwargs.get('coh', 0))
        self.phi = float(kwargs.get('phi', 0))
        self.mod = float(kwargs.get('mod', 0))
        self.res_mod = float(kwargs.get('res_mod', 0))
    
    def __repr__(self):
        return (f"DiscreteFunctionDataPoint(x={self.x}, y={self.y}, coh={self.coh}, phi={self.phi}, "
                f"mod={self.mod}, res_mod={self.res_mod}, ")

class DiscreteFunctionData:
    """
    The DiscreteFunctionData object stores all possible fields exported 
    from RS2 or Slide2 used to create or update a discrete strength function in RS2.

    Args:
        name (str): The name of the discrete function.
        id (int): The ID of the discrete function.
        sample_num (int): The sample number.
        res_strength_factor (float): The residual strength factor.
        tensile_strength (float): The tensile strength.
        residual_tensile_strength (float): The residual tensile strength.
        modulus (float): The modulus.
        modulus_res (float): The residual modulus.
        correlation_flag (int): The correlation flag.
        correlation_num (float): The correlation number.
        randomize_selection (int): The randomize selection type
        randomize_num (int): The approximate number of points for randomizing
        c_dist (float): The cohesion distribution.
        c_mean (float): The cohesion mean.
        c_stdv (float): The cohesion standard deviation.
        c_min (float): The cohesion minimum value.
        c_max (float): The cohesion maximum value.
        phi_dist (float): The friction angle distribution.
        phi_mean (float): The friction angle mean.
        phi_stdv (float): The friction angle standard deviation.
        phi_min (float): The friction angle minimum value.
        phi_max (float): The friction angle maximum value.
        mod_dist (float): The modulus distribution.
        mod_mean (float): The modulus mean.
        mod_stdv (float): The modulus standard deviation.
        mod_min (float): The modulus minimum value.
        mod_max (float): The modulus maximum value.
        mod_res_dist (float): The residual modulus distribution.
        mod_res_mean (float): The residual modulus mean.
        mod_res_stdv (float): The residual modulus standard deviation.
        mod_res_min (float): The residual modulus minimum value.
        mod_res_max (float): The residual modulus maximum value.
        strength_type (str): The strength or function type, such as drained or undrained.
        interpolation (str): The interpolation type.
        symbol_type (str): The symbol type.
        fill_interior (str): The fill interior type.
        color_interior (int): The interior color represented as RGB values converted to a rgb_as_single_int integer value.
        color_exterior (int): The exterior color represented as RGB values converted to a rgb_as_single_int integer value.
        points (int): The number of points.
        data_points (list[DiscreteFunctionDataPoint]): A list of data points for the discrete function.

    Attributes: 
        name (str): The name of the discrete function.
        id (int): The ID of the discrete function.
        sample_num (int): The sample number.
        res_strength_factor (float): The residual strength factor.
        tensile_strength (float): The tensile strength.
        residual_tensile_strength (float): The residual tensile strength.
        modulus (float): The modulus.
        modulus_res (float): The residual modulus.
        correlation_flag (int): The correlation flag.
        correlation_num (float): The correlation number.
        randomize_selection (int): The randomize selection type
        randomize_num (int): The approximate number of points for randomizing
        c_dist (float): The cohesion distribution.
        c_mean (float): The cohesion mean.
        c_stdv (float): The cohesion standard deviation.
        c_min (float): The cohesion minimum value.
        c_max (float): The cohesion maximum value.
        phi_dist (float): The friction angle distribution.
        phi_mean (float): The friction angle mean.
        phi_stdv (float): The friction angle standard deviation.
        phi_min (float): The friction angle minimum value.
        phi_max (float): The friction angle maximum value.
        mod_dist (float): The modulus distribution.
        mod_mean (float): The modulus mean.
        mod_stdv (float): The modulus standard deviation.
        mod_min (float): The modulus minimum value.
        mod_max (float): The modulus maximum value.
        mod_res_dist (float): The residual modulus distribution.
        mod_res_mean (float): The residual modulus mean.
        mod_res_stdv (float): The residual modulus standard deviation.
        mod_res_min (float): The residual modulus minimum value.
        mod_res_max (float): The residual modulus maximum value.
        strength_type (str): The strength or function type, such as drained or undrained.
        interpolation (str): The interpolation type.
        symbol_type (str): The symbol type.
        fill_interior (str): The fill interior type.
        color_interior (int): The interior color represented as RGB values converted to a rgb_as_single_int integer value.
        color_exterior (int): The exterior color represented as RGB values converted to a rgb_as_single_int integer value.
        points (int): The number of points.
        data_points (list[DiscreteFunctionDataPoint]): A list of data points for the discrete function.
    """
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.id = int(kwargs.get('id', -1))
        self.sample_num = int(kwargs.get('sample_num', -1))
        self.res_strength_factor = float(kwargs.get('res_strength_factor', 0.0))
        self.tensile_strength = float(kwargs.get('tensile_strength', 0.0))
        self.residual_tensile_strength = float(kwargs.get('residual_tensile_strength', 0.0))
        self.modulus = float(kwargs.get('modulus', 0.0))
        self.modulus_res = float(kwargs.get('modulus_res', 0.0))
        self.correlation_flag = int(kwargs.get('correlation_flag', 0))
        self.correlation_num = float(kwargs.get('correlation_num', 0.0))
        self.randomize_selection = int(kwargs.get('randomize_selection', 0))
        self.randomize_num = int(kwargs.get('randomize_num', 0))
        self.c_dist = float(kwargs.get('c_dist', 0.0))
        self.c_mean = float(kwargs.get('c_mean', 0.0))
        self.c_stdv = float(kwargs.get('c_stdv', 0.0))
        self.c_min = float(kwargs.get('c_min', 0.0))
        self.c_max = float(kwargs.get('c_max', 0.0))
        self.phi_dist = float(kwargs.get('phi_dist', 0.0))
        self.phi_mean = float(kwargs.get('phi_mean', 0.0))
        self.phi_stdv = float(kwargs.get('phi_stdv', 0.0))
        self.phi_min = float(kwargs.get('phi_min', 0.0))
        self.phi_max = float(kwargs.get('phi_max', 0.0))
        self.mod_dist = float(kwargs.get('mod_dist', 0.0))
        self.mod_mean = float(kwargs.get('mod_mean', 0.0))
        self.mod_stdv = float(kwargs.get('mod_stdv', 0.0))
        self.mod_min = float(kwargs.get('mod_min', 0.0))
        self.mod_max = float(kwargs.get('mod_max', 0.0))
        self.mod_res_dist = float(kwargs.get('mod_res_dist', 0.0))
        self.mod_res_mean = float(kwargs.get('mod_res_mean', 0.0))
        self.mod_res_stdv = float(kwargs.get('mod_res_stdv', 0.0))
        self.mod_res_min = float(kwargs.get('mod_res_min', 0.0))
        self.mod_res_max = float(kwargs.get('mod_res_max', 0.0))
        self.strength_type = kwargs.get('strength_type', '')
        self.interpolation = kwargs.get('interpolation', '')
        self.symbol_type = kwargs.get('symbol_type', '')
        self.fill_interior = kwargs.get('fill_interior', '')
        self.color_interior = kwargs.get('color_interior', (255, 255, 255))
        self.color_exterior = kwargs.get('color_exterior', (0, 0, 0))
        self.points = int(kwargs.get('points', 0))
        self.data_points = kwargs.get('data_points', [])

    def __repr__(self):
        return (f"DiscreteFunctionData(name={self.name}, id={self.id}, res_strength_factor={self.res_strength_factor}, "
                f"tensile_strength={self.tensile_strength}, residual_tensile_strength={self.residual_tensile_strength}, "
                f"modulus={self.modulus}, modulus_res={self.modulus_res}, correlation_flag={self.correlation_flag}, "
                f"correlation_num={self.correlation_num}, randomize_selection={self.randomize_selection}, "
                f"randomize_num={self.randomize_num}, c_dist={self.c_dist}, c_mean={self.c_mean}, c_stdv={self.c_stdv}, "
                f"c_min={self.c_min}, c_max={self.c_max}, phi_dist={self.phi_dist}, phi_mean={self.phi_mean}, "
                f"phi_stdv={self.phi_stdv}, phi_min={self.phi_min}, phi_max={self.phi_max}, mod_dist={self.mod_dist}, "
                f"mod_mean={self.mod_mean}, mod_stdv={self.mod_stdv}, mod_min={self.mod_min}, mod_max={self.mod_max}, "
                f"mod_res_dist={self.mod_res_dist}, mod_res_mean={self.mod_res_mean}, mod_res_stdv={self.mod_res_stdv}, "
                f"mod_res_min={self.mod_res_min}, mod_res_max={self.mod_res_max}, strength_type={self.strength_type}, "
                f"interpolation={self.interpolation}, symbol_type={self.symbol_type}, fill_interior={self.fill_interior}, "
                f"color_interior={self.color_interior}, color_exterior={self.color_exterior}, points={self.points}, "
                f"data_points={self.data_points})")

class DiscreteFunctionHelpers:
    """
    The DiscreteFunctionHelpers object provides supporting functionality to 
    create or update discrete functions in RS2. These include functions 
    to read and write data related to discrete functions 

    Args: None

    Attributes: None
    """
    @staticmethod
    def readDiscreteFunctionFilefn6(file_path: str, extract_sample_num_from_name:bool=True)->DiscreteFunctionData:
        """
        Initialize DiscreteFunctionData object from fn6 file type
        
        Args:
            file_path(str): full file path to data file
            extract_sample_num_from_name(bool): set True if file name is written as "NAME Sample 1.fn6" where "Sample" is a keyword indicating 
                the next string is the sample number, False otherwise
        
        Raises: None 
        
        Returns:
            a DiscreteFunctionData object that is initialized using read data from the given 'file_path' or
            a DiscreteFunctionData object with default values if file is not found. 
        """
        data = {}
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('color'):
                    # color interior/exterior information, assuming rgb format
                    match = re.match(r'(\w[\w\s]*):\s+(.*)', line)
                    if match:
                        key = match.group(1).strip().replace(' ', '_') 
                        value = match.group(2).strip()
                        # store rgb as a tuple of three integers
                        r, g, b = map(int, re.findall(r'\d+', value))
                        value = (int(r),int(g),int(b))
                        data[key] = value
                else:
                    # header information assuming key: value format, keys and values can be multiple words
                    # this is a key: this is a value
                    # key must be alphanumeric character from the basic Latin alphabet, including the underscore [A-Za-z0-9_]
                    # value can be any character
                    match = re.match(r'(\w[\w\s]*):\s+(.*)', line)
                    if match:
                        key = match.group(1).strip().replace(' ', '_') 
                        value = match.group(2).strip()
                        
                        data[key] = value
                    
                        if key == 'points': 
                            # data points below the header information, only works if keys and values are not multiple words
                            # ex. x: 1 y: 2 c: 3 d: 4 e: 5
                            data_points = []
                            for _ in range(int(value)):
                                try:
                                    line = next(file).strip()
                                    key_value_pairs = re.findall(r'(\w[\w]*:\s+\S[\S]*)', line)
                                    data_point_data = {}
                                    for key_value_pair in key_value_pairs:
                                        key, value = key_value_pair.split(':')
                                        key = key.strip()
                                        value = value.strip()
                                                                                
                                        data_point_data[key] = value
                                    
                                    data_points.append(DiscreteFunctionDataPoint(**data_point_data))  
                                except StopIteration:
                                    print("Reached end of file before expected number of points read")
                                    break

                            data['data_points'] = data_points

        # Create new discrete function data object
        discrete_function_data = DiscreteFunctionData(**data)
        
        # If you have the sample number as part of the name, you can extract it as follows
        # ex. "Sandy Clay Sample 1.fn6" where "Sample" is a keyword and "1" is the value
        if extract_sample_num_from_name and discrete_function_data.name:
            # Extract material name and sample number
            material_name = discrete_function_data.name # "Sandy Clay Sample 1"
            sample_num = -1 # default if no sample number found
            sample_num_str = ""
            # Find the index of the last occurrence of "Sample"
            index_sample = material_name.rfind("Sample")
            # If "Sample" is found in the text
            if index_sample != -1:
                # Split the text at the found index
                sample_num_str = material_name[index_sample:] # "Sample 1"
                sample_num_str = sample_num_str.split()[-1].strip() # "1"
                material_name = material_name[:index_sample].strip() # "Sandy Clay"
            
            # Validate sample number found
            try:
                sample_num = int(sample_num_str)
            except ValueError:
                print(f'Sample number not found from {file_path} sample number of -1 used')
            
            # Separate name and sample number in separate fields
            discrete_function_data.name = material_name
            discrete_function_data.sample_num = sample_num

        return discrete_function_data

    @staticmethod
    def writeDiscreteFunctionFilefn6(output_file_path: str, df_data: DiscreteFunctionData):
        """
        Write 'df_data' using the fn6 format to the file found in 'output_file_path'. 
        Does nothing if output file not found.
        
        FOR CHECKING VALUES ONLY. File not expect to be imported directly into the RS2 discrete function feature
        
        Args:
            output_file_path(str): full file path to output data
            df_data(DiscreteFunctionData): discrete function data object 
        
        Raises: None 
        
        Returns: None
        """
        with open(output_file_path, 'w') as file:
            file.write(f'Slide Discrete Function\n')
            file.write(f'    name: {df_data.name}') 
            if (df_data.sample_num > 0): 
                file.write(f' Sample {df_data.sample_num}')
            file.write('\n')
            file.write(f'    strength type: {df_data.strength_type}\n')
            file.write(f'    interpolation: {df_data.interpolation}\n')
            file.write(f'    symbol type: {df_data.symbol_type}\n')
            file.write(f'    fill interior: {df_data.fill_interior}\n')
            file.write(f'    color interior:   r: {df_data.color_interior[0]} g: {df_data.color_interior[1]} b: {df_data.color_interior[2]}\n')
            file.write(f'    color exterior:   r: {df_data.color_exterior[0]} g: {df_data.color_exterior[1]} b: {df_data.color_exterior[2]}\n')
            file.write(f'    points: {df_data.points}\n')  
            for data_point in df_data.data_points:
                file.write(f'    x: {data_point.x}  y: {data_point.y}  coh: {data_point.coh}  phi: {data_point.phi}\n')

    @staticmethod
    def readDiscreteFunctionFileCustom(file_path)->list[DiscreteFunctionData]:
        """
        Initialize a list of DiscreteFunctionData objects from a custom data file format
                
        Args:
            file_path(str): full file path to data file

        Raises: None 
        
        Returns:
            a list of DiscreteFunctionData objects that is initialized using read data from the given 'file_path'.
            an empty list if file is not found.
        """
        all_discrete_function_data = []
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)

            # Extract header
            header_row = next(reader)
            name = header_row[0].strip()
            headers = [header.strip() for header in header_row[2:] if header]
            
            # read data till end of file
            row = next(reader,None)
            while row is not None:
                if not any(row):
                    continue  # skip empty rows
                
                try:
                    sample_tag, sample_number_str = row[0].split()
                    if sample_tag != 'Sample':
                        raise ValueError('Expected sample data information')

                    sample_number = int(sample_number_str)

                except ValueError:
                    print(f'Unexpected line in {file_path}')
                    return all_discrete_function_data

                # Initialize the data points list
                data_points = []   
                while (row:=next(reader,None)) is not None: 
                    if not any(row):
                        continue # skip empty rows

                    if row[0].strip().split()[0] == 'Sample':
                        break
                              
                    # Create a dictionary to map headers to row values
                    row_data = {headers[i]: row[i] for i in range(len(headers))}
                    
                    # Create a DataPoint instance
                    data_point = DiscreteFunctionDataPoint(
                        x=row_data.get('x', 0),
                        y=row_data.get('y', 0),
                        coh=row_data.get('cohesion', 0),
                        phi=row_data.get('phi', None)
                    )
                    data_points.append(data_point)

                new_df = DiscreteFunctionData(name=name, sample_num=sample_number, data_points=data_points) 
                all_discrete_function_data.append(new_df)

        # Create and return the DiscreteFunctionData instance
        return all_discrete_function_data 

    @staticmethod
    def writeDiscreteFunctionFileCustom(output_file_path: str, all_df_data: list[DiscreteFunctionData]):
        """
        Write 'all_df_data' in a custom format to the file found in 'output_file_path'. 
        Does nothing if output file not found.
        Good for checking read values
    
        Args:
            output_file_path(str): full file path to output data
            all_df_data(list[str]): list of discrete function data objects
            
        Raises: None 
        
        Returns: None
        """
        with open(output_file_path, 'w', newline='') as file:
            if all_df_data:
                writer = csv.writer(file)
                # write header
                df_data_first = all_df_data[0]
                writer.writerow([df_data_first.name,'','x','y','cohesion','phi'])
                for df_data in all_df_data:
                    writer.writerow([f'Sample {df_data.sample_num}'])
                    for data_point in df_data.data_points:
                        x = int(data_point.x) if data_point.x.is_integer() else data_point.x
                        y = int(data_point.y) if data_point.y.is_integer() else data_point.y
                        coh = int(data_point.coh) if data_point.coh.is_integer() else data_point.coh
                        phi = int(data_point.phi) if data_point.phi.is_integer() else data_point.phi
                        writer.writerow([x,y,coh,phi]) 

    @staticmethod
    def readDiscreteFunctionFile(file_path:str)->list[DiscreteFunctionData]:
        """ 
        Initialize a list of discrete function data objects using data read from a file based on its extension
    
        Args:
            file_path(str): full file path to data file
            all_df_data(list[str]): list of discrete function data objects
            
        Raises: None 
        
        Returns:
            A list of DiscreteFunctionData objects that is initialized using read data from the given 'file_path'.
            An empty list if file is not found or file extension type is not supported
        """
        all_discrete_function_data = []
        # Read data
        root, extension = os.path.splitext(file_path)
        if  extension == '.fn6':
            # RS2 or Slide2 exported discrete function type
            all_discrete_function_data.append(DiscreteFunctionHelpers.readDiscreteFunctionFilefn6(file_path))
        elif extension =='.cust': 
            # Custom file type
            all_discrete_function_data.extend(DiscreteFunctionHelpers.readDiscreteFunctionFileCustom(file_path))
        else: 
            print(f'{discrete_function_file_path} has an unsuported extension')
            return []

        return all_discrete_function_data

    @staticmethod
    def getDiscreteFunctionDataPerSample(discrete_function_file_paths: list[str])->dict[int,list[DiscreteFunctionData]]:
        """
        Read discrete function data from files and return a dictionary of data per sample id

        Args:
            discrete_function_file_paths (list[str]): A list of file paths containing discrete function data.
            
        Raises:
            None

        Returns:
            A dictionary of sample id to a list of DiscreteFunctionData objects
        """
        # Collect all discrete function file data to minimize number of times models are opened in update
        samplenum_to_discretefunctiondata = {}
        for discrete_function_file_path in discrete_function_file_paths:
            # Get list of discrete_function_data to update model
            all_discrete_function_data = DiscreteFunctionHelpers.readDiscreteFunctionFile(discrete_function_file_path)
            for discrete_function_data in all_discrete_function_data:
                if discrete_function_data.sample_num in samplenum_to_discretefunctiondata:
                    samplenum_to_discretefunctiondata[discrete_function_data.sample_num].append(discrete_function_data)
                else: 
                    samplenum_to_discretefunctiondata[discrete_function_data.sample_num] = [discrete_function_data]
        
        return samplenum_to_discretefunctiondata        


    @staticmethod
    def updateDiscreteFunction(df_data: DiscreteFunctionData, df: DiscreteFunction)->bool:
        """
        Update df, discrete function object outputted by RS2, using the data stored in df_data

        Only MAIN functionality is implemented in this example. Please update if there are
        discrete function parameters you want to update which aren't implemented.

        Args:
            file_path(str): full file path to data file
            all_df_data(list[str]): list of discrete function data objects
            
        Raises: None 
        
        Returns:
            True if discrete function was updated with no warnings or issues, False othwerise
        """
        # Only set parameters which are initialized in the input data

        # Set general parameters, mostly leave as default if importing from Slide 2
        curr_params = df.getFunctionParameters()

        # Set function type, other function parameters NOT IMPLEMENTED 
        function_type = DiscreteDrainedMode.DRAINED #drained default
        if df_data.strength_type == 'drained':
            function_type = DiscreteDrainedMode.DRAINED
        elif df_data.strength_type == 'undrained':
            function_type = DiscreteDrainedMode.UNDRAINED

        df.setFunctionParameters(function_type, curr_params[1],curr_params[2],curr_params[3],curr_params[4],curr_params[5])

        # Set interpolation method
        if df_data.interpolation == 'thin plate spline':
            df.setInterpolationMethod(InterpolationMethod.THIN_PLATE_SPLINE)
        elif df_data.interpolation == 'chugh':
            df.setInterpolationMethod(InterpolationMethod.MODIFIED_CHUGH)
        elif df_data.interpolation == 'local thin plate':
            df.setInterpolationMethod(InterpolationMethod.LOCAL_THIN_PLATE_SPLINE)
        elif df_data.interpolation == 'tin triangulation':
            df.setInterpolationMethod(InterpolationMethod.TIN_TRIANGULATION)
        elif df_data.interpolation == 'inverse distance': 
            df.setInterpolationMethod(InterpolationMethod.INVERSE_DISTANCE)
        elif df_data.interpolation == 'linear by elevation': 
            df.setInterpolationMethod(InterpolationMethod.LINEAR_BY_ELEVATION)
        elif df_data.interpolation == 'original chugh':
            df.setInterpolationMethod(InterpolationMethod.CHUGH)

        # Set symbol drawing, NOT IMPLEMENTED 

        # Set point locations, add more data types as needed
        point_locations = []
        coh_list = []
        phi_list = []
        mod_list = []
        res_mod_list = []
        for data_point in df_data.data_points:
            point_locations.append((data_point.x, data_point.y))
            coh_list.append(data_point.coh)
            phi_list.append(data_point.phi)
            mod_list.append(data_point.mod)
            res_mod_list.append(data_point.res_mod)

        if point_locations:
            df.setPointLocations(point_locations)

            if len(coh_list) != len(point_locations):
                print(f'Sample {df_data.sample_num} for {df_data.name} discrete function has invalid number of cohesion values compared to point locations')
                return False
            df.setPointsC(coh_list)

            if len(phi_list) != len(point_locations):
                print(f'Sample {df_data.sample_num} for {df_data.name} discrete function has invalid number of phi values compared to point locations')
                return False
            df.setPointsPhi(phi_list)

            if len(mod_list) != len(point_locations):
                print(f'Sample {df_data.sample_num} for {df_data.name} discrete function has invalid number of modulus values compared to point locations')
                return False
            df.setPointsModulus(mod_list)

            if len(res_mod_list) != len(point_locations):
                print(f'Sample {df_data.sample_num} for {df_data.name} discrete function has invalid number of residual modulus values compared to point locations')
                return False
            df.setPointsModulusResidual(res_mod_list)
        
        return True

    @staticmethod
    def updateModelMaterialsWithDiscreteFunctionData(model: Model, all_discrete_function_data: list[DiscreteFunctionData]):
        """
        Update materials in model object with discrete function data of same name

        Args:
            model(Model): RS2 modeler Model object
            all_discrete_function_data(list[DiscreteFunctionData]): list of discrete function data objects to use
            
        Raises: None  
        
        Returns: None

        """

        # Update materials
        for discrete_function_data in all_discrete_function_data:
            # Get header values
            material_name = discrete_function_data.name               

            # Find discrete function
            try:
                discrete_function = model.getDiscreteFunctionByName(material_name)
            except RuntimeError:
                # Create new if not found
                model.createNewDiscreteFunction(material_name)
                discrete_function = model.getDiscreteFunctionByName(material_name)

            # Update with read data
            DiscreteFunctionHelpers.updateDiscreteFunction(discrete_function_data, discrete_function)

            # Change material to use new discrete function of same name
            try: 
                material = model.getMaterialPropertyByName(material_name)
                material.Strength.setFailureCriterion(StrengthCriteriaTypes.DISCRETE_FUNCTION)
                material.Strength.DiscreteFunction.setSelectedDiscreteFunctionByName(material_name)
            except ValueError:
                print(f'material {material_name} not found in {discrete_function_file_path}, file not used')
                continue



