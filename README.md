# deltae

[![Build Status](https://app.travis-ci.com/kaineyb/deltae.svg?branch=master)](https://app.travis-ci.com/kaineyb/deltae)

Written in Python. 

Requires 3.6 or greater (uses f-strings)

Currently has DeltaE1976, DeltaE2000 with the others looking to be implemented in the future.

Based on the whitepaper by Gaurav Sharma, Wencheng Wu and Endul N. Dala from the University of Rochester NY

## User Dependancies:
None

## Dev Dependancies:
Pandas for creating test_functions.py 

## Background

Uses the data set provided from: http://www2.ece.rochester.edu/~gsharma/ciede2000/dataNprograms/CIEDE2000.xls to test against. (converted to csv as rochester_data.csv)

Based on using Bruce Lindblooms (http://www.brucelindbloom.com/) DE2000 calcuation. Then updated with the maths from the Rochester white paper.

It seems as though Rochester uses a different calculation for hPrime, h1Prime, h2Prime and hBarPrime than Bruce. However the whole dataset does return the correct deltae2000 values for both formulas. Perhaps there are some combinations of lab values that would be different.

## Installation

Pip: 

```pip install deltae
```


## Example Usage:
```python
    import deltae
```
##### Takes CIELAB values as a dictionary - example below:
```python
    Lab1 = {'L': 50.00, 'a': 2.6772, 'b': -79.7751}
    Lab2 = {'L': 50.00, 'a': 0.00, 'b': -82.7485}
```

##### Get the DeltaE 1976 Formula of 2 Lab Values:
```python
    deltae.delta_e_1976(Lab1, Lab2)
```
##### Get the DeltaE 2000 Formula of 2 Lab Values:
```python
    deltae.delta_e_2000(Lab1, Lab2)
```