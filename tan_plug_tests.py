
import unittest
import tan_plug

class SemitanPlugTest(unittest.TestCase):

    def testGap(self):
        schedules = [[10, 1430], [20, 540], [1425, 528]]
        expectedResults = [20, 920, 897]
        ii = 0
        for element in schedules:

            result = tan_plug.getGap(element[0], element[1])
            self.assertEqual(result, expectedResults[ii])
            ii += 1

unittest.main()
