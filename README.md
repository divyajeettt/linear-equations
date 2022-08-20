# linear-equations

## About linear-equations

linear-equations is a mathematical Python module providing Linear Equations in one variable, and Linear Equations in two variables as Python objects through two classes called `LinearEquation1D` and `LinearEquation2D`. 

*Date of creation:* `April 04, 2021` \
*Date of first release on [PyPI](https://pypi.org/):* `April 29, 2021`

Along with the classes describing algebra of linear equations, a class `Symbol` has also been provided to allocate the symbols used in these equations.

## gui-linear-equations

A small graphical-user interface based program is also available as a sub-part of this project. The GUI version of linear-equations has a dependency on this module, `linear_equations`. \
*Date of creation:* `April 20, 2021`

## Edit the logging settings

## Some features and functionalities

- class `Symbol`
    > symbols to use in Linear Equations, forexample: Symbol("x") -> x
- class `LinearEquation1D`
    > objects of type `ax + b = 0`
- class `LinearEquation2D`
    > objects of type `ax + by + c = 0`
- function `solve1D(eqn)`
    > used to retrieve the solution to a 1D equation
- function `solve2D(eqn1, eqn2)`
    > used to retrieve solution to two 2D equations
- function `consistency(eqn1, eqn2)`
    > checks and returns if the given LinearEquation2D objects are consistent or not
- function `satisfies(eqn, x, y)`
    > returns True if the given pair of numbers satisfy a particular LinearEquation2D and False otherwise

All classes, methods and functions are enriched with help-text that can be acccessed using the following syntax:

```python
help(linear_equations.thing)
```

## Run

To use, execute:

```
pip install linear-equations
```

Import this file in your project, wherever needed, using:

```python
import lienar_equations as le
```

To use the graphical-user interface, clone the repository on your device, navigate to the folder, and execute:

```
python3 gui_linear_equations.py
```
