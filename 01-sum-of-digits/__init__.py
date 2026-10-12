import check50

@check50.check()
def compiles():
    """sum_digits.c compiles"""
    check50.run(
        "gcc -std=c11 -Wall -Wextra -Werror "
        "sum_digits.c -o program"
    ).exit(0)

def verify(value, expected):
    output = check50.run("./program").stdin(
        str(value) + "\n"
    ).stdout().strip()

    if output != str(expected):
        raise check50.Failure(
            f"Input: {value}; expected: {expected}; "
            f"received: {output!r}"
        )

@check50.check(compiles)
def test_5729():
    """5729 gives 23"""
    verify(5729, 23)

@check50.check(compiles)
def test_10005():
    """10005 gives 6"""
    verify(10005, 6)

@check50.check(compiles)
def test_large():
    """123456789 gives 45"""
    verify(123456789, 45)

@check50.check(compiles)
def test_single():
    """7 gives 7"""
    verify(7, 7)

@check50.check(compiles)
def test_zeros():
    """9090 gives 18"""
    verify(9090, 18)
