import check50, re
@check50.check()
def exists():
    """fibonacci.c exists"""
    check50.exists("fibonacci.c")
@check50.check(exists)
def compiles():
    """compiles with gcc"""
    check50.run("gcc -std=c11 -Wall -Wextra -Werror fibonacci.c -o program").exit(0)
def ints(s): return [int(x) for x in re.findall(r"(?<![A-Za-z])-?\d+", s)]
def check_seq(inp, exp):
    out=check50.run("./program").stdin(str(inp)).stdout()
    got=ints(out)
    if got[-len(exp):] != exp:
        raise check50.Failure(f"expected final sequence {exp}, got {got[-len(exp):]}")
@check50.check(compiles)
def n1(): """n=1 gives 0"""; check_seq(1,[0])
@check50.check(compiles)
def n5(): """n=5 gives 0 1 1 2 3"""; check_seq(5,[0,1,1,2,3])
@check50.check(compiles)
def n10(): """n=10 gives first ten terms"""; check_seq(10,[0,1,1,2,3,5,8,13,21,34])
