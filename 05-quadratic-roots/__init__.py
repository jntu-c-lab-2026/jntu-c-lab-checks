import check50, re, math
@check50.check()
def exists():
    """quadratic.c exists"""
    check50.exists("quadratic.c")
@check50.check(exists)
def compiles():
    """compiles with math library"""
    check50.run("gcc -std=c11 -Wall -Wextra -Werror quadratic.c -o program -lm").exit(0)
def nums(s): return [float(x) for x in re.findall(r"(?<![A-Za-z])[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?", s)]
def roots(a,b,c):
    d=b*b-4*a*c
    if d<0: return []
    r=math.sqrt(d)
    return sorted([(-b-r)/(2*a),(-b+r)/(2*a)])
def check_real(a,b,c,expected):
    out=check50.run("./program").stdin(f"{a} {b} {c}").stdout()
    ns=nums(out)
    # ignore coefficients if the program echoes input: compare every expected root to some output number
    for e in expected:
        if not any(abs(v-e)<1e-5 for v in ns):
            raise check50.Failure(f"expected root near {e}; output was: {out}")
@check50.check(compiles)
def roots12():
    """x^2-3x+2 has roots 1 and 2"""
    check_real(1,-3,2,[1,2])
@check50.check(compiles)
def double_root():
    """x^2+2x+1 has root -1"""
    check_real(1,2,1,[-1,-1])
@check50.check(compiles)
def roots_pm2():
    """x^2-4 has roots -2 and 2"""
    check_real(1,0,-4,[-2,2])
