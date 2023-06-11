import upper, unittest, sys, io

class lower_test(unittest.TestCase):
    
    def test_to_lower(self):
        self.assertEqual("khant", upper.to_lower("khant"), "lower")
        self.assertEqual("khant", upper.to_lower("KHANT"), "upper")
        self.assertEqual("8166", upper.to_lower("8166"), "numeric")
    
    def testIO_to_lower(self):
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("khant\n")
        upper.IOto_lower()
        self.assertEqual("khant", capout.getvalue(), "lower")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("KHANT\n")
        upper.IOto_lower()
        self.assertEqual("khant", capout.getvalue(), "upper")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("8166\n")
        upper.IOto_lower()
        self.assertEqual("8166", capout.getvalue(), "numeric")
    
    def testIOfile_to_lower(self):
        upper.fileIOto_lower("strings.txt", 0)
        with open("strings.txt") as outputfile:
            lines = outputfile.readlines()
            self.assertEqual("khant", lines[10], "lower")
        upper.fileIOto_lower("strings.txt", 1)
        with open("strings.txt") as outputfile:
            self.assertEqual("khant", lines[11], "upper")
        upper.fileIOto_lower("strings.txt", 2)
        with open("strings.txt") as outputfile:
            self.assertEqual("8166", lines[12], "numeric")