# mean-variance-standard-deviation-calculator


## Overview
This repository contains the implementation of the `calculate()` function in Python, designed as part of a data analysis project. The function computes the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3x3 matrix.

## Features
- Input validation for exactly nine numbers.
- Conversion of input list to a 3x3 Numpy array.
- Calculation of statistical measures along both axes and for the flattened matrix.
- Returns a structured dictionary with calculated values.

## Usage
To use the `calculate()` function, pass a list of nine numbers as an argument. For example:

```python
from mean_var_std import calculate

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)

## Requirements
Python 3
Numpy

## License
MIT
