import number, unittest, sys, io

class number_test(unittest.TestCase):
    
    def test_is_number(self):
        self.assertEqual(True, number.is_number("8166"), "number")
        self.assertEqual(False, number.is_number("81KH"), "partially number")
        self.assertEqual(False, number.is_numeric("khant"), "!numeric")

    def testIO_is_number(self):
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("8166\n")
        number.IOis_number()
        self.assertEqual("True", capout.getvalue(), "numeric")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("81KH\n")
        number.IOis_number()
        self.assertEqual("False", capout.getvalue(), "partially numeric")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("khant\n")
        number.IOis_number()
        self.assertEqual("False", capout.getvalue(), "!numeric")

    def testIOfile_is_number(self):
        number.fileIOis_number("strings.txt", 2)
        with open("strings.txt") as outputfile:
            lines = outputfile.readlines()
            self.assertEqual("True", lines[16], "numeric")
        number.fileIOis_number("strings.txt", 3)
        with open("strings.txt") as outputfile:
            self.assertEqual("False", lines[17], "partially numeric")
        number.fileIOis_number("strings.txt", 0)
        with open("strings.txt") as outputfile:
            self.assertEqual("False", lines[18], "!numeric")