import check50, re
@check50.check()
def exists():
    """primes.c exists"""
    check50.exists("primes.c")
@check50.check(exists)
def compiles():
    """compiles with gcc"""
    check50.run("gcc -std=c11 -Wall -Wextra -Werror primes.c -o program").exit(0)
def ints(s): return [int(x) for x in re.findall(r"(?<![A-Za-z])-?\d+", s)]
def check_primes(n, exp):
    out=check50.run("./program").stdin(str(n)).stdout()
    got=ints(out)
    if got[-len(exp):] != exp if exp else got:
        raise check50.Failure(f"expected primes {exp}, got {got}")
@check50.check(compiles)
def n10(): """primes through 10"""; check_primes(10,[2,3,5,7])
@check50.check(compiles)
def n20(): """primes through 20"""; check_primes(20,[2,3,5,7,11,13,17,19])
@check50.check(compiles)
def n50(): """primes through 50"""; check_primes(50,[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])
