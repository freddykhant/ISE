import upper, unittest, sys, io

class upper_test(unittest.TestCase):

    def test_to_upper(self):
        self.assertEqual("KHANT", upper.to_upper("khant"), "lower")
        self.assertEqual("KHANT", upper.to_upper("KHANT"), "upper")
        self.assertEqual("8166", upper.to_upper("8166"), "numeric")
        
    def testIO_to_upper(self):
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("khant\n")
        upper.IOto_upper()
        self.assertEqual("KHANT", capout.getvalue(), "lower")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("KHANT\n")
        upper.IOto_upper()
        self.assertEqual("KHANT", capout.getvalue(), "upper")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("8166\n")
        upper.IOto_upper()
        self.assertEqual("8166", capout.getvalue(), "numeric")

    def testIOfile_to_upper(self):
        upper.fileIOto_upper("strings.txt", 0)
        with open("strings.txt") as outputfile:
            lines = outputfile.readlines()
            self.assertEqual("KHANT", lines[7], "lower")
        upper.fileIOto_upper("strings.txt", 1)
        with open("strings.txt") as outputfile:
            self.assertEqual("KHANT", lines[8], "upper")
        upper.fileIOto_upper("strings.txt", 2)
        with open("strings.txt") as outputfile:
            self.assertEqual("8166", lines[9], "numeric")