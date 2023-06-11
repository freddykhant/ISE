import secstomins, unittest, sys, io

class test_seconds_to_mins(unittest.TestCase):

    def test_seconds_to_mins(self):
        self.assertEqual(136.1, secstomins.seconds_to_mins(8166), "n > 0")
        self.assertEqual("Invalid time", secstomins.seconds_to_mins(-8166), "n < 0")
    
    def testIO_seconds_to_mins(self):
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("8166\n")
        secstomins.IOseconds_to_mins()
        self.assertEqual("136.1", capout.getvalue(), "n > 0")
        capout = io.StringIO()
        sys.stdout = capout
        sys.stdin = io.StringIO("-8166\n")
        secstomins.IOseconds_to_mins()
        self.assertEqual("Invalid time", capout.getvalue(), "n < 0")

    def testIOfile_seconds_to_mins(self):
        secstomins.file_seconds_to_mins("time.txt", 0)
        with open("time.txt") as file:
            lines = file.readlines()
            self.assertEqual("136.1", lines[8], "n > 0")
        secstomins.file_seconds_to_mins("time.txt", 1)
        with open("time.txt") as file:
            lines = file.readlines()
            self.assertEqual("Invalid time", lines[9], "n > 0")