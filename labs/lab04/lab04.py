HW_SOURCE_FILE = __file__


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n <= 1: 
        return term(n)
    return term(n) + summation(n-1, term)

def find_path(x, y, m, n):
    if x > m or y > n :
        return 0
    if x == m and y == n :
        return 1
    return find_path(x + 1, y, m, n) + find_path(x, y + 1, m, n)

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    x = 1
    y = 1
    return find_path(x,y,m,n)


def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
    m = n = 10
    nextLine = "\n"
    test = [[0 for i in range(m)] for j in range(n)]
    test[0][0] = 1
    for i in range(1, row+1) :
        for j in range(0, i + 1) :
            if j == 0 or j == i + 1:
                test[i][j] = 1
            else :
                test[i][j] = test[i-1][j-1] + test[i-1][j]
        # print(test[i])
    return test[row][column]

def double_eight(pre_status, n) :
    temp = False
    if n % 10 == 8 :
        temp = True
    if temp == True and pre_status == True :
        return True
    if n < 1 :
        return False 
    n = n // 10
    return double_eight(temp,n)
def double_eights(n):
    """ Returns whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    return double_eight(False,n)

