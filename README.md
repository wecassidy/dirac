Abuse operator overloading to implement Dirac (bra-ket) notation in
Python with [sympy](https://sympy.org/).

# Example
```python
>>> from sympy import *
>>> import dirac
>>> x, y = symbols("x y")
>>> I = Integer(1) # Use as identity operator
>>> I | x >> I # Need ones on either side because | and > are binary operators
|x>
>>> I << y | x >> I
<y|x>
```

# Limitations
Since `<<`, `>>`, and `|` are binary operators, there needs to be
something on either side. That makes the syntax a bit less elegant
than it could be.

Obviously, this is incredibly delicate. There's no kind of error
handling for malformed expressions, for example. Testing was very
limited.
