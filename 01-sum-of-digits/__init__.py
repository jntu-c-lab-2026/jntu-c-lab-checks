import check50, re
@check50.check()
def exists():
    """sum_digits.c exists"""
    check50.exists("sum_digits.c")
@check50.check(exists)
def compiles():
    """compiles with gcc"""
    check50.run("gcc -std=c11 -Wall -Wextra -Werror sum_digits.c -o program").exit(0)
def nums(s): return [int(x) for x in re.findall(r"(?<![A-Za-z])[-+]?\d+", s)]
@check50.check(compiles)
def test_5729():
    """5729 gives 23"""
    out=check50.run("./program").stdin("5729").stdout()
    if 23 not in nums(out): raise check50.Failure("expected digit sum 23")
@check50.check(compiles)
def test_10005():
    """10005 gives 6"""
    out=check50.run("./program").stdin("10005").stdout()
    if 6 not in nums(out): raise check50.Failure("expected digit sum 6")
@check50.check(compiles)
def test_large():
    """123456789 gives 45"""
    out=check50.run("./program").stdin("123456789").stdout()
    if 45 not in nums(out): raise check50.Failure("expected digit sum 45")
