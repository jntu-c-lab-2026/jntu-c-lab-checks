import check50, re, math
@check50.check()
def exists():
    """series_sum.c exists"""
    check50.exists("series_sum.c")
@check50.check(exists)
def compiles():
    """compiles with gcc and math library"""
    check50.run("gcc -std=c11 -Wall -Wextra -Werror series_sum.c -o program -lm").exit(0)
def val(x):
    y=check50.run("./program").stdin(str(x)).stdout()
    m=re.findall(r"[-+]?(?:\d+\.\d*|\d*\.\d+|\d+)(?:[eE][-+]?\d+)?", y)
    if not m: raise check50.Failure("no numeric result found")
    return float(m[-1])
def expected(x):
    return 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8)-x**10/math.factorial(10)
@check50.check(compiles)
def x0():
    """x=0 gives 1"""
    if abs(val(0)-1.0)>1e-9: raise check50.Failure("expected 1.0")
@check50.check(compiles)
def x1():
    """x=1 gives approximately 0.4596976941"""
    if abs(val(1)-expected(1))>1e-6: raise check50.Failure("series value is incorrect")
@check50.check(compiles)
def x2():
    """x=2 gives approximately -0.1736507937"""
    if abs(val(2)-expected(2))>1e-6: raise check50.Failure("series value is incorrect")
@check50.check(compiles)
def x3():
    """x=3 gives approximately -0.5484953704"""
    if abs(val(3)-expected(3))>1e-6: raise check50.Failure("series value is incorrect")
