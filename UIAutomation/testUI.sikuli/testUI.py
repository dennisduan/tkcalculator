import unittest
import os,sys
import subprocess
from sikuli.Sikuli import *

productdir = '/Users/dennis/work/experimental/python/tkcal'
sys.path.insert(0,productdir)

class TestClickButton(unittest.TestCase):
    def setUp(self):
        sleep(2)
        self.p = subprocess.Popen(['python', productdir + '/startMockUI.py'], stdout=subprocess.PIPE)
          
    def testClickButton_0(self):
        click("1414393313522.png")
        r = self.p.communicate()
        self.assertEqual('0', r[0].strip())

    def testClickButton_1(self):
        click("1414393320556.png")
        r = self.p.communicate()
        self.assertEqual('1', r[0].strip())

    def testClickButton_2(self):
        click("1414393329054.png")
        r = self.p.communicate()
        self.assertEqual('2', r[0].strip())

    def testClickButton_3(self):
        click("1414393335828.png")
        r = self.p.communicate()
        self.assertEqual('3', r[0].strip())

    def testClickButton_4(self):
        click("1414393343180.png")
        r = self.p.communicate()
        self.assertEqual('4', r[0].strip())

    def testClickButton_5(self):
        click("1414393350518.png")
        r = self.p.communicate()
        self.assertEqual('5', r[0].strip())

    def testClickButton_6(self):
        click("1414393357876.png")
        r = self.p.communicate()
        self.assertEqual('6', r[0].strip())

    def testClickButton_7(self):
        click("1414393367553.png")
        r = self.p.communicate()
        self.assertEqual('7', r[0].strip())

    def testClickButton_8(self):
        click("1414393376775.png")
        r = self.p.communicate()
        self.assertEqual('8', r[0].strip())

    def testClickButton_9(self):
        click("1414393386419.png")
        r = self.p.communicate()
        self.assertEqual('9', r[0].strip())

    def testClickButton_add(self):
        click("1414393410261.png")
        r = self.p.communicate()
        self.assertEqual('+', r[0].strip())

    def testClickButton_sub(self):
        click("1414393417967.png")
        r = self.p.communicate()
        self.assertEqual('-', r[0].strip())

    def testClickButton_mul(self):
        click("1414393424831.png")
        r = self.p.communicate()
        self.assertEqual('*', r[0].strip())

    def testClickButton_div(self):
        click("1414393467627.png")
        r = self.p.communicate()
        self.assertEqual('/', r[0].strip())

    def testClickButton_equal(self):
        click("1414393473997.png")
        r = self.p.communicate()
        self.assertEqual('=', r[0].strip())

    def testClickButton_clear(self):
        click("1414393481188.png")
        r = self.p.communicate()
        self.assertEqual('C', r[0].strip())

# Sikuli settings (no logs)
Settings.ActionLogs = False
Settings.InfoLogs = False
Settings.DebugLogs = False
 
suite = unittest.TestLoader().loadTestsFromTestCase(TestClickButton)
unittest.TextTestRunner(verbosity=2).run(suite)
