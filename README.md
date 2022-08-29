# linear-equations

## About linear-equations

linear-equations is a mathematical Python module providing Linear Equations in one variable, and Linear Equations in two variables as Python objects through two classes called `LinearEquation1D` and `LinearEquation2D`. 

*Date of creation:* `April 04, 2021` \
*Date of first release on [PyPI](https://pypi.org/project/linear-equations/):* `April 29, 2021`

Along with the classes describing algebra of linear equations, a class `Symbol` has also been provided to allocate the symbols used in these equations.

## gui-linear-equations

A small graphical-user interface based program is also available as a sub-part of this project. The GUI version of linear-equations has a dependency on this module, `linear_equations`. \
*Date of creation:* `April 20, 2021`

## Features

- class `Symbol`
    > symbols to use in Linear Equations, for example: Symbol("x") -> x
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

## Edit the logging settings

To modify the level of the `logger`, modify:

```python
logging.basicConfig(
    filename="linear-equations.log", level=logging.INFO, format=LOG_FORMAT
)
```

 on [Line 102](https://github.com/divyajeettt/linear-equations/blob/15c664e4bbe0d2c0eeba964eeaed4b1ac658c3b2/gui_linear_equations.py#L102) of `gui_linear_equations.py` to:
 
 ```python
logging.basicConfig(
    filename="linear-equations.log", level=LEVEL, format=LOG_FORMAT
)
 ```
 
 where `LEVEL` can be one of:
 - `logging.INFO`
 - `logging.DEBUG`
 - `logging.WARNING`
 - `logging.ERROR`
 - `logging.CRITICAL`

## Update History

### Update (0.0.5)

Added graphing and visualization of 2-dimensional equations. \
Added function `graph(eqn1, eqn2)` which graphs the given `LinearEquation2D` objects on a 2D mathematical plot along with their solution (if any)

### Update (0.0.6)

Minor bug fixes:
- Fixed issues with plotting linear equations
- Improved legend on graphs

Added function `graph_many(eqn1, eqn2, ..., eqn, show_legend=True)` which graphs more than two `LinearEquation2D` objects on the same plot along with each of their solutions (if any)

### Updates (0.0.7)
Minor bug fixes

## Footnotes

'gui_linear_equations.py' makes use of global variables.

## Run

To use, execute:

```
pip3 install linear-equations
```

Import this file in your project, wherever needed, using:

```python
import linear_equations as le
```

To use the graphical-user interface, clone the repository on your device, navigate to the folder, and execute:

```
python3 gui_linear_equations.py
```
