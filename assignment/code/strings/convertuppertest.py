import convertupper, unittest, sys, io

class convertupper_test(unittest.TestCase):
    
    def test_convert_upper(self):
        self.assertEqual("KH", convertupper.convert_upper("81kh"), "number + lower")
        self.assertEqual("KH", convertupper.convert_upper("81KH"), "number + upper")
        self.assertEqual("KH", convertupper.convert_upper("kh"), "lower")
        self.assertEqual("KH", convertupper.convert_upper("KH"), "upper")
        self.assertEqual("\n", convertupper.convert_upper("8166"), "number")

    def testIO_convert_upper(self):
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("81kh\n")
        convertupper.IOconvert_upper()
        self.assertEqual("KH", capout.getvalue(), "number + lower")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("81KH\n")
        convertupper.IOconvert_upper()
        self.assertEqual("KH", capout.getvalue(), "number + upper")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("kh\n")
        convertupper.IOconvert_upper()
        self.assertEqual("KH", capout.getvalue(), "lower")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("KH\n")
        convertupper.IOconvert_upper()
        self.assertEqual("KH", capout.getvalue(), "upper")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("8166\n")
        convertupper.IOconvert_upper()
        self.assertEqual("\n", capout.getvalue(), "number")

    def testIOfile_convert_upper(self):
        convertupper.fileIOconvert_upper("strings.txt", 4)
        with open("strings.txt") as outputfile:
            lines = outputfile.readlines()
            self.assertEqual("KH", lines[19], "number + lower")
        convertupper.fileIOconvert_upper("strings.txt", 3)
        with open("strings.txt") as outputfile:
            self.assertEqual("KH", lines[20], "number + upper")
        convertupper.fileIOconvert_upper("strings.txt", 5)
        with open("strings.txt") as outputfile:
            self.assertEqual("KH", lines[21], "lower")
            convertupper.fileIOconvert_upper("strings.txt", 6)
        with open("strings.txt") as outputfile:
            self.assertEqual("KH", lines[22], "upper")
            convertupper.fileIOconvert_upper("strings.txt", 2)
        with open("strings.txt") as outputfile:
            self.assertEqual("\n", lines[23], "number")