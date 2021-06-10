import os
import numpy 
import argparse #1
def calculate_distance(coords1, coords2):
    x_distance = coords1[0] - coords2[0]
    y_distance = coords1[1] - coords2[1]
    z_distance = coords1[2] - coords2[2]
    distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance
def bond_check(atom_distance, minimum_length=0, maximum_length=1.5):
    """
    Checks if a distance is a bond based on a minimum and a maximum 
    Inputs: distance minimum length for bond, maximum length for bond
    Default: minimum 0 angstroms, maximum:1.5 angstroms
    """
    if atom_distance > minimum_length and atom_distance < maximum_length:
        return True
    else:
        return False
def open_xyz(filename):
    """
    This function opens a standard xyz file.
    It returns the symbols as strings and the coordinates as floats
    """
    
    xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coord = xyz_file[:,1 :]
    coord = coord.astype(float)
    return symbols, coord 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The script analyzes a user given xyz file and outputs the lengths of the bonds.") #2
    parser.add_argument('xyz_file', help='The filepath of the xyz file to analyze.') #3
    args = parser.parse_args() #4

    file_location = args.xyz_file #5
    symbols, coordinates = open_xyz(file_location)
    num_atoms = len(symbols)
    for num1 in range (0, num_atoms):
        for num2 in range(0, num_atoms):
            if num1<num2:
                distance = calculate_distance(coordinates[num1], coordinates[num2])
                if bond_check(distance) is True:
                    print(F'{symbols[num1]} to {symbols[num2]} : {distance: .3f}')

