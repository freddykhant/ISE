import minstohours, unittest, sys, io

class test_mins_to_hours(unittest.TestCase):

    def test_mins_to_hours(self):
        self.assertEqual(136.1, minstohours.mins_to_hours(8166), "n > 0")
        self.assertEqual("Invalid time", minstohours.mins_to_hours(-8166), "n < 0")
    
    def testIO_mins_to_hours(self):
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("8166\n")
        minstohours.IOmins_to_hours()
        self.assertEqual("136.1", capout.getvalue(), "n > 0")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("-8166\n")
        minstohours.IOmins_to_hours()
        self.assertEqual("Invalid time", capout.getvalue(), "n < 0")
    
    def testIOfile_mins_to_hours(self):
        minstohours.file_mins_to_hours("time.txt", 0)
        with open("time.txt") as file:
            lines = file.readlines()
            self.assertEqual("136.1", lines[4], "n > 0")
        minstohours.file_mins_to_hours("time.txt", 1)
        with open("time.txt") as file:
            lines = file.readlines()
            self.assertEqual("Invalid time", lines[5], "n > 0")