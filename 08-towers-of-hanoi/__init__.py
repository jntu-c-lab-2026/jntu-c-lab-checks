import check50, re
@check50.check()
def exists():
    """hanoi.c exists"""
    check50.exists("hanoi.c")
@check50.check(exists)
def compiles():
    """compiles with gcc"""
    check50.run("gcc -std=c11 -Wall -Wextra -Werror hanoi.c -o program").exit(0)
def lines(out):
    return [x.strip() for x in out.splitlines() if "Move disk" in x]
@check50.check(compiles)
def one_disk():
    """one disk moves A to C"""
    out=check50.run("./program").stdin("1").stdout()
    if lines(out) != ["Move disk 1 from A to C"]:
        raise check50.Failure("expected exactly one move: Move disk 1 from A to C")
@check50.check(compiles)
def two_disks():
    """two disks use the optimal three moves"""
    out=check50.run("./program").stdin("2").stdout()
    expected=["Move disk 1 from A to B","Move disk 2 from A to C","Move disk 1 from B to C"]
    if lines(out) != expected:
        raise check50.Failure("incorrect move sequence for two disks")
@check50.check(compiles)
def three_disks_count():
    """three disks require exactly seven moves"""
    out=check50.run("./program").stdin("3").stdout()
    if len(lines(out)) != 7:
        raise check50.Failure("three disks require exactly 7 moves")
@check50.check(compiles)
def recursive_source():
    """hanoi function calls itself"""
    src=open("hanoi.c").read().replace(" ","")
    if "hanoi(n-1" not in src:
        raise check50.Failure("hanoi should recursively call itself with n-1")
