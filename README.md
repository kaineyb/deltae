# deltae

Based on the whitepaper by Gaurav Sharma, Wencheng Wu and Endul N. Dala from University of Rochester, Rochester, NY

## Dependancies:
Uses pandas only for testing.

## Background

Uses the data set provided from: http://www2.ece.rochester.edu/~gsharma/ciede2000/dataNprograms/CIEDE2000.xls to test against. (converted to csv as rochester_data.csv)

Started out using Bruce Lindblooms (http://www.brucelindbloom.com/) DE2000 javascript file converting to python, then trying to get this to pass the rochester dataset which didn't work. 

Upon reading the whitepaper I realised that there was probably some issues within Bruce's calculations, and started adjusting where necessary. 

It seems as though Rochester uses a different calculation for hPrime, h1Prime, h2Prime and hBarPrime than Bruce. However the whole dataset does return the correct deltae2000 values for both formulas. Perhaps there are some combinations of lab values that would be different.

## Example Usage:

    import deltae

##### Takes CIELAB values as a dictionary - example below:

    Lab1 = {'L': 50.00, 'a': 2.6772, 'b': -79.7751}
    Lab2 = {'L': 50.00, 'a': 0.00, 'b': -82.7485}

##### Get the DeltaE 1976 Formula of 2 Lab Values:
    deltae.delta_e_1976(Lab1, Lab2)

##### Get the DeltaE 2000 Formula of 2 Lab Values:
    deltae.delta_e_2000(Lab1, Lab2)

##### Test a Rochester Pair - takes a rochester data set pair that you want to see the values off.

    deltae.delta_e_2000_test_pair(33)
