import convertlower, unittest, sys, io

class convertlower_test(unittest.TestCase):

    def test_convert_lower(self):
        self.assertEqual("kh", convertlower.convert_lower("81kh"), "number + lower")
        self.assertEqual("kh", convertlower.convert_lower("81KH"), "number + upper")
        self.assertEqual("kh", convertlower.convert_lower("kh"), "lower")
        self.assertEqual("kh", convertlower.convert_lower("KH"), "upper")
        self.assertEqual("\n", convertlower.convert_lower("8166"), "number")

    def testIO_convert_lower(self):
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("81kh\n")
        convertlower.IOconvert_lower()
        self.assertEqual("kh", capout.getvalue(), "number + lower")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("81KH\n")
        convertlower.IOconvert_lower()
        self.assertEqual("kh", capout.getvalue(), "number + upper")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("kh\n")
        convertlower.IOconvert_lower()
        self.assertEqual("kh", capout.getvalue(), "lower")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("KH\n")
        convertlower.IOconvert_lower()
        self.assertEqual("kh", capout.getvalue(), "upper")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("8166\n")
        convertlower.IOconvert_lower()
        self.assertEqual("\n", capout.getvalue(), "number")

    def testIOfile_convert_lower(self):
        convertlower.fileIOconvert_lower("strings.txt", 4)
        with open("strings.txt") as outputfile:
            lines = outputfile.readlines()
            self.assertEqual("kh", lines[24], "number + lower")
        convertlower.fileIOconvert_lower("strings.txt", 3)
        with open("strings.txt") as outputfile:
            self.assertEqual("kh", lines[25], "number + upper")
        convertlower.fileIOconvert_lower("strings.txt", 5)
        with open("strings.txt") as outputfile:
            self.assertEqual("kh", lines[26], "lower")
        convertlower.fileIOconvert_lower("strings.txt", 6)
        with open("strings.txt") as outputfile:
            self.assertEqual("kh", lines[27], "upper")
        convertlower.fileIOconvert_lower("strings.txt", 2)
        with open("strings.txt") as outputfile:
            self.assertEqual("\n", lines[28], "number")