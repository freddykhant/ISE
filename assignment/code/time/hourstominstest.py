import hourstomins, unittest, sys, io

class test_hours_to_mins(unittest.TestCase):

    def test_hours_to_mins(self):
        self.assertEqual(489960, hourstomins.hours_to_mins(8166), "n > 0")
        self.assertEqual("Invalid time", hourstomins.hours_to_mins(-8166), "n < 0")

    def testIO_hours_to_mins(self):
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("8166\n")
        hourstomins.IOhours_to_mins()
        self.assertEqual("489960", capout.getvalue(), "n > 0")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("-8166\n")
        hourstomins.IOhours_to_mins()
        self.assertEqual("Invalid time", capout.getvalue(), "n < 0")
    
    def testIOfile_hours_to_mins(self):
        hourstomins.file_hours_to_mins("time.txt", 0)
        with open("time.txt") as file:
            lines = file.readlines()
            self.assertEqual("489960", lines[2], "n > 0")
        hourstomins.file_hours_to_mins("time.txt", 1)
        with open("time.txt") as file:
            lines = file.readlines()
            self.assertEqual("Invalid time", lines[3], "n > 0")