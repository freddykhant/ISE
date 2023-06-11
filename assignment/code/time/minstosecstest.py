import minstosecs, unittest, sys, io

class test_mins_to_seconds(unittest.TestCase):

    def test_mins_to_seconds(self):
        self.assertEqual(489960, minstosecs.mins_to_seconds(8166), "n > 0")
        self.assertEqual("Invalid time", minstosecs.mins_to_seconds(-8166), "n < 0")
    
    def testIO_mins_to_seconds(self):
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("8166\n")
        minstosecs.IOmins_to_seconds()
        self.assertEqual("489960", capout.getvalue(), "n > 0")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("-8166\n")
        minstosecs.IOmins_to_seconds()
        self.assertEqual("Invalid time", capout.getvalue(), "n < 0")

    def testIOfile_mins_to_seconds(self):
        minstosecs.file_mins_to_seconds("time.txt", 0)
        with open("time.txt") as file:
            lines = file.readlines()
            self.assertEqual("489960", lines[6], "n > 0")
        minstosecs.file_mins_to_seconds("time.txt", 1)
        with open("time.txt") as file:
            lines = file.readlines()
            self.assertEqual("Invalid time", lines[7], "n > 0")