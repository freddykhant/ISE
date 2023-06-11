import numeric, unittest, sys, io

class numeric_test(unittest.TestCase):
    
    def test_is_numeric(self):
        self.assertEqual(True, numeric.is_numeric("8166"), "numeric")
        self.assertEqual(True, numeric.is_numeric("81KH"), "partially numeric")
        self.assertEqual(False, numeric.is_numeric("khant"), "!numeric")

    def testIO_is_numeric(self):
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("8166\n")
        numeric.IOis_numeric()
        self.assertEqual("True", capout.getvalue(), "numeric")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("81KH\n")
        numeric.IOis_numeric()
        self.assertEqual("True", capout.getvalue(), "partially numeric")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("khant\n")
        numeric.IOis_numeric()
        self.assertEqual("False", capout.getvalue(), "!numeric")

    def testIOfile_is_numeric(self):
        numeric.fileIOis_numeric("strings.txt", 2)
        with open("strings.txt") as outputfile:
            lines = outputfile.readlines()
            self.assertEqual("True", lines[13], "numeric")
        numeric.fileIOis_numeric("strings.txt", 3)
        with open("strings.txt") as outputfile:
            self.assertEqual("True", lines[14], "partially numeric")
        numeric.fileIOis_numeric("strings.txt", 0)
        with open("strings.txt") as outputfile:
            self.assertEqual("False", lines[15], "!numeric")