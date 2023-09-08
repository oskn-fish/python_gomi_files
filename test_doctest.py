
class TestClass:
    def testfunc(self, a, b):
        """
        returns the sum of the inputs
        >>> testclass = TestClass()
        >>> testclass.testfunc(1, 2)
        3
        >>> testclass.testfunc(-1, 3)
        2
        """
        return a+b
    
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
        