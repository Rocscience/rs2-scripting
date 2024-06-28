
import os
import re
import csv

from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.DiscreteFunction import DiscreteFunction

class RGBColorData:
    def __init__(self, r=0, g=0, b=0):
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0  or b > 255: 
            raise TypeError('RGB values should be between 0 and 255')

        self.r = int(r)
        self.g = int(g)
        self.b = int(b)


class DiscreteFunctionDataPoint:
    def __init__(self, x=0, y=0, coh=0, phi=0, gsi=0, mi=0, d=0, ucs=0):
        self.x = float(x)
        self.y = float(y)
        self.coh = float(coh)
        self.phi = float(phi)
        self.gsi = float(gsi)
        self.mi = float(mi)
        self.d = float(d)
        self.ucs = float(ucs)

    def __repr__(self):
        return f"dataPoint(x={self.x}, y={self.y}, coh={self.coh}, phi={self.phi}, " \
               f"gsi={self.gsi}, mi={self.mi}, d={self.d}, ucs={self.ucs})"

class DiscreteFunctionData:
    def __init__(self, name="", id=-1, group_id=-1, res_strength_factor=0.0, tensile_strength=0.0, residual_tensile_strength=0.0,
                 modulus=0.0, modulus_res=0.0, correlation_flag=0, correlation_num=0.0, randomize_selection=0, 
                 randomize_num=0, c_dist=0.0, c_mean=0.0, c_stdv=0.0, c_min=0.0, c_max=0.0, phi_dist=0.0, phi_mean=0.0, 
                 phi_stdv=0.0, phi_min=0.0, phi_max=0.0, mod_dist=0.0, mod_mean=0.0, mod_stdv=0.0, mod_min=0.0, mod_max=0.0, 
                 mod_res_dist=0.0, mod_res_mean=0.0, mod_res_stdv=0.0, mod_res_min=0.0, mod_res_max=0.0, 
                 strength_type="", interpolation="", symbol_type="", fill_interior="", color_interior=None, 
                 color_exterior=None, points=0, data_points: list[DiscreteFunctionDataPoint] =None):
        
        self.name = name
        self.group_id = group_id
        self.id = int(id)
        self.res_strength_factor = float(res_strength_factor)
        self.tensile_strength = float(tensile_strength)
        self.residual_tensile_strength = float(residual_tensile_strength)
        self.modulus = float(modulus)
        self.modulus_res = float(modulus_res)
        self.correlation_flag = int(correlation_flag)
        self.correlation_num = float(correlation_num)
        self.randomize_selection = int(randomize_selection)
        self.randomize_num = int(randomize_num)
        self.c_dist = float(c_dist)
        self.c_mean = float(c_mean)
        self.c_stdv = float(c_stdv)
        self.c_min = float(c_min)
        self.c_max = float(c_max)
        self.phi_dist = float(phi_dist)
        self.phi_mean = float(phi_mean)
        self.phi_stdv = float(phi_stdv)
        self.phi_min = float(phi_min)
        self.phi_max = float(phi_max)
        self.mod_dist = float(mod_dist)
        self.mod_mean = float(mod_mean)
        self.mod_stdv = float(mod_stdv)
        self.mod_min = float(mod_min)
        self.mod_max = float(mod_max)
        self.mod_res_dist = float(mod_res_dist)
        self.mod_res_mean = float(mod_res_mean)
        self.mod_res_stdv = float(mod_res_stdv)
        self.mod_res_min = float(mod_res_min)
        self.mod_res_max = float(mod_res_max)
        self.strength_type = strength_type
        self.interpolation = interpolation
        self.symbol_type = symbol_type
        self.fill_interior = fill_interior
        self.color_interior = color_interior if color_interior else {'r': 255, 'g': 255, 'b': 255}
        self.color_exterior = color_exterior if color_exterior else {'r': 0, 'g': 0, 'b': 0}
        self.points = int(points)
        self.data_points = data_points if data_points else []

    def __repr__(self):
        return (f"SlideDiscreteFunction(name={self.name}, id={self.id}, res_strength_factor={self.res_strength_factor}, "
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

    @staticmethod
    def readDiscreteFunctionFilefn6(file_path: str, extract_sample_num_from_name:bool=True)->DiscreteFunctionData:
        data = {}
        data_points = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith('x:'):
                    # data points below the header information, only works if keys and values are not multiple words
                    # ex. x: 1 y: 2 c: 3 d: 4 
                    key_value_pairs = re.findall(r'(\w[\w]*:\s+\S[\S]*)', line)
                    data_point_data = {}
                    for key_value_pair in key_value_pairs:
                        key, value = key_value_pair.split(':')
                        key = key.strip()
                        value = value.strip()
                        data_point_data[key] = value

                    data_points.append(DiscreteFunctionDataPoint(**data_point_data))    

                elif line.startswith('color'):
                    # color interior/exterior information, assuming r g b format
                    match = re.match(r'(\w[\w\s]*):\s+(.*)', line)
                    if match:
                        key = match.group(1).strip().replace(' ', '_') 
                        value = match.group(2).strip()
                        # extract rgb data
                        r, g, b = map(int, re.findall(r'\d+', value))
                        value = {'r': r, 'g': g, 'b': b}
                        data[key] = RGBColorData(**value)
                else:
                    # header information assuming key: value format, keys and values can be multiple words
                    # this is a key: this is a value
                    match = re.match(r'(\w[\w\s]*):\s+(.*)', line)
                    if match:
                        key = match.group(1).strip().replace(' ', '_') 
                        value = match.group(2).strip()
                        data[key] = value

        data['data_points'] = data_points

        if extract_sample_num_from_name and 'name' in data:
            # Extract material name and sample number
            material_name = data['name']
            sample_num = None
            # Find the index of the last occurrence of "Sample"
            index_sample = material_name.rfind("Sample")
            # If "Sample" is found in the text
            if index_sample != -1:
                # Split the text at the found index
                sample_num_str = material_name[index_sample:].split()[-1].strip()
                material_name = material_name[:index_sample].strip()
            
            # Validate sample number found
            try:
                sample_num = int(sample_num_str)
            except ValueError:
                print(f'sample number not found from {file_path} sample number of 1 used')
                sample_num = 1
            
            # Separate name and sample number in separate fields
            data['name'] = material_name

        return DiscreteFunctionData(group_id=sample_num, **data)

    @staticmethod
    def writeDiscreteFunctionFilefn6(output_file_path: str, all_df_data: list[DiscreteFunctionData]):
        with open(output_file_path, 'w') as file:
            file.write(f'name: {df_data.name}\n')
            file.write(f'strength type: {df_data.strength_type}\n')
            file.write(f'interpolation: {df_data.interpolation}\n')
            file.write(f'symbol type: {df_data.symbol_type}\n')
            file.write(f'fill interior: {df_data.fill_interior}\n')
            file.write(f'color interior: r: {df_data.color_interior.r} g: {df_data.color_interior.g} b: {df_data.color_interior.b}\n')
            file.write(f'color exterior: r: {df_data.color_exterior.r} g: {df_data.color_exterior.g} b: {df_data.color_exterior.b}\n')
            file.write(f'points: {df_data.points}\n')
            for data_point in df_data.data_points:
                file.write(f'x: {data_point.x} y: {data_point.y} coh: {data_point.coh} phi: {data_point.phi} gsi: {data_point.gsi} mi: {data_point.mi} d: {data_point.d} ucs: {data_point.ucs:.14e}\n')

    @staticmethod
    def readDiscreteFunctionFileDev(file_path)->list[DiscreteFunctionData]:
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

                new_df = DiscreteFunctionData(name=name, group_id=sample_number, data_points=data_points) 
                all_discrete_function_data.append(new_df)

        # Create and return the DiscreteFunctionData instance
        return all_discrete_function_data 

    @staticmethod
    def writeDiscreteFunctionFileDev(output_file_path: str, all_df_data: list[DiscreteFunctionData]):
        with open(output_file_path, 'w', newline='') as file:
            if all_df_data:
                writer = csv.writer(file)
                # write header
                df_data_first = all_df_data[0]
                writer.writerow([df_data_first.name,'','x','y','cohesion','phi'])
                for df_data in all_df_data:
                    writer.writerow([f'Sample {df_data.group_id}'])
                    for data_point in df_data.data_points:
                        x = int(data_point.x) if data_point.x.is_integer() else data_point.x
                        y = int(data_point.y) if data_point.y.is_integer() else data_point.y
                        coh = int(data_point.coh) if data_point.coh.is_integer() else data_point.coh
                        phi = int(data_point.phi) if data_point.phi.is_integer() else data_point.phi
                        writer.writerow([x,y,coh,phi]) 

    @staticmethod
    def readDiscreteFunctionFile(file_path:str)->list[DiscreteFunctionData]:
        all_discrete_function_data = []
        # Read data
        root, extension = os.path.splitext(file_path)
        if  extension == '.fn6':
            # One function per file
            all_discrete_function_data.append(DiscreteFunctionHelpers.readDiscreteFunctionFilefn6(file_path))
        elif extension =='.txt': 
            # change later
            all_discrete_function_data.extend(DiscreteFunctionHelpers.readDiscreteFunctionFileDev(file_path))
        else: 
            print(f'{discrete_function_file_path} has an invalid extension')
            return []

        return all_discrete_function_data

    @staticmethod
    def updateDiscreteFunction(df_data: DiscreteFunctionData, df: DiscreteFunction)->bool:
        # Only set parameters which are initialized in the input data

        # Set general parameters, mostly leave as default if importing from Slide 2
        curr_params = df.getFunctionParameters()

        # Set function type
        function_type = DiscreteDrainedMode.DRAINED #drained default
        if df_data.strength_type == 'drained':
            function_type = DiscreteDrainedMode.DRAINED
        elif df_data.strength_type == 'undrained':
            function_type = DiscreteDrainedMode.UNDRAINED

        df.setFunctionParameters(function_type, curr_params[1],curr_params[2],curr_params[3],curr_params[4],curr_params[5])

        # Set interpolation method, add more later
        if df_data.interpolation == 'chugh':
            df.setInterpolationMethod(InterpolationMethod.CHUGH)

        # Set symbol drawing, do later

        # Set point locations
        point_locations = []
        coh_list = []
        phi_list = []
        for data_point in df_data.data_points:
            point_locations.append((data_point.x, data_point.y))
            coh_list.append(data_point.coh)
            phi_list.append(data_point.phi)

        if point_locations:
            df.setPointLocations(point_locations)

            if len(coh_list) != len(point_locations):
                print(f'Group {df_data.group_id} for {df_data.name} discrete function has invalid number of cohesion values compared to point locations')
                return False
            df.setPointsC(coh_list)

            if len(phi_list) != len(point_locations):
                print(f'Group {df_data.group_id} for {df_data.name} discrete function has invalid number of phi values compared to point locations')
                return False
            df.setPointsPhi(phi_list)
        
        return True



    @staticmethod
    def importDiscreteFunctionFilesToRS2(modeler: RS2Modeler, base_file_path: str,
        discrete_function_file_paths: list[str],
        output_dir: str, compute_models=False, allow_updating_existing_files=False):

        # Start Test
        '''
        pr = cProfile.Profile()
        pr.enable()
        '''
        # Collect all discrete function file data to minimize number of times models are opened in update
        samplenum_to_discretefunctiondata = {}
        for discrete_function_file_path in discrete_function_file_paths:
            # Get list of discrete_function_data to update model
            all_discrete_function_data = DiscreteFunctionHelpers.readDiscreteFunctionFile(discrete_function_file_path)
            for discrete_function_data in all_discrete_function_data:
                if discrete_function_data.group_id in samplenum_to_discretefunctiondata:
                    samplenum_to_discretefunctiondata[discrete_function_data.group_id].append(discrete_function_data)
                else: 
                    samplenum_to_discretefunctiondata[discrete_function_data.group_id] = [discrete_function_data]
        
        # Open base model
        try:
            model = modeler.openFile(base_file_path)
        except RuntimeError:
            print(f'Unable to find file to update for {discrete_function_file_path}')
            return

        # Update model(s)
        for sample_number, all_discrete_function_data in samplenum_to_discretefunctiondata.items():
            # Output file path
            output_file_name = f'{sample_number}.fez'
            output_path = os.path.join(output_dir, output_file_name)

            if allow_updating_existing_files:
                 # Enable updating existing models, it's slow though, not typically worth it
                if(os.path.isfile(output_path)):
                    model = modeler.openFile(output_path)
                else:
                    model = modeler.openFile(base_file_path)
            else:
                # Save as a new file, faster: only won't work if you have different materials updated in different samples
                model.saveAs(output_path)
            
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
                
            # Save changes
            model.save()

            # Compute if required
            if compute_models:
                model.compute()

            # Updating existing files will open a new file each update, so close it before next update
            if allow_updating_existing_files: 
                model.close()
        