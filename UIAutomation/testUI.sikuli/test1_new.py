import os,sys
import subprocess
from sikuli import *

productdir = '/Users/dennis/work/experimental/python/tkcal'
sys.path.insert(0,productdir)

p = None

def setUp():
    print 'wait for 5 seconds'
    sleep(5)
    print 'starting startMockUI.py'
    p = subprocess.Popen(['python', productdir + '/startMockUI.py'], stdout=subprocess.PIPE)
      
def testClickButton_0():
    click("1414393313522.png")
    r = p.communicate()
    assert('0' == r[0].strip())

def testClickButton_1():
    click("1414393320556.png")
    r = p.communicate()
    assert('1' == r[0].strip())

def testClickButton_2():
    click("1414393329054.png")
    r = p.communicate()
    assert('2' == r[0].strip())

def testClickButton_3():
    click("1414393335828.png")
    r = p.communicate()
    assert('3' == r[0].strip())

def testClickButton_4():
    click("1414393343180.png")
    r = p.communicate()
    assert('4' == r[0].strip())

def testClickButton_5():
    click("1414393350518.png")
    r = p.communicate()
    assert('5' == r[0].strip())

def testClickButton_6():
    click("1414393357876.png")
    r = p.communicate()
    assert('6' == r[0].strip())

def testClickButton_7():
    click("1414393367553.png")
    r = p.communicate()
    assert('7' == r[0].strip())

def testClickButton_8():
    click("1414393376775.png")
    r = p.communicate()
    assert('8' == r[0].strip())

def testClickButton_9():
    click("1414393386419.png")
    r = p.communicate()
    assert('9' == r[0].strip())

def testClickButton_add():
    click("1414393410261.png")
    r = p.communicate()
    assert('+' == r[0].strip())

def testClickButton_sub():
    click("1414393417967.png")
    r = p.communicate()
    assert('-' == r[0].strip())

def testClickButton_mul():
    click("1414393424831.png")
    r = p.communicate()
    assert('*' == r[0].strip())

def testClickButton_div():
    click("1414393467627.png")
    r = p.communicate()
    assert('/' == r[0].strip())

def testClickButton_equal():
    click("1414393473997.png")
    r = p.communicate()
    assert('=' == r[0].strip())

def testClickButton_clear():
    click("1414393481188.png")
    r = p.communicate()
    assert('C' == r[0].strip())

