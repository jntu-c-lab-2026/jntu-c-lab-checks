import check50, re
@check50.check()
def exists():
    """gcd.c exists"""
    check50.exists("gcd.c")
@check50.check(exists)
def compiles():
    """compiles with gcc"""
    check50.run("gcc -std=c11 -Wall -Wextra -Werror gcd.c -o program").exit(0)
def check_pair(a,b,expected):
    out=check50.run("./program").stdin(f"{a} {b}").stdout()
    vals=[int(x) for x in re.findall(r"(?<![A-Za-z])-?\d+",out)]
    if vals[-2:] != [expected,expected]:
        raise check50.Failure(f"both GCD results should be {expected}; output: {out}")
@check50.check(compiles)
def pair48_18(): """gcd(48,18) is 6"""; check_pair(48,18,6)
@check50.check(compiles)
def pair100_25(): """gcd(100,25) is 25"""; check_pair(100,25,25)
@check50.check(compiles)
def pair17_31(): """gcd(17,31) is 1"""; check_pair(17,31,1)
@check50.check(compiles)
def recursive_source():
    """gcd_recursive contains a recursive Euclid step"""
    src=open("gcd.c").read().replace(" ","")
    if "gcd_recursive(b,a%b)" not in src:
        raise check50.Failure("gcd_recursive should recursively call gcd_recursive(b, a % b)")
