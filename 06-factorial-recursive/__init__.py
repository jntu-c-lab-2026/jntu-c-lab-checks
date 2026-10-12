import check50, re
@check50.check()
def exists():
    """factorial.c exists"""
    check50.exists("factorial.c")
@check50.check(exists)
def compiles():
    """compiles with gcc"""
    check50.run("gcc -std=c11 -Wall -Wextra -Werror factorial.c -o program").exit(0)
def check_n(n, expected):
    out=check50.run("./program").stdin(str(n)).stdout()
    vals=[int(x) for x in re.findall(r"-?\d+",out)]
    if vals[-2:] != [expected,expected]:
        raise check50.Failure(f"recursive and iterative results should both be {expected}; output: {out}")
@check50.check(compiles)
def n0(): """factorial(0) is 1"""; check_n(0,1)
@check50.check(compiles)
def n5(): """factorial(5) is 120"""; check_n(5,120)
@check50.check(compiles)
def n10(): """factorial(10) is 3628800"""; check_n(10,3628800)
@check50.check(compiles)
def recursive_source():
    """factorial_recursive contains a recursive self-call"""
    src=open("factorial.c").read().replace(" ","")
    if "factorial_recursive(n-1)" not in src:
        raise check50.Failure("factorial_recursive should call itself with n-1")
