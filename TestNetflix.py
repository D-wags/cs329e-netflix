#!/usr/bin/env python3

# -------
# imports
# -------
from Netflix import netflix_eval
from unittest import main, TestCase
from math import sqrt
from io import StringIO
from numpy import sqrt, square, mean, subtract

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase):

    # ----
    # eval
    # ----

    def test_eval_1(self):
        r = StringIO("8067:\n1945990\n2099932\n1649003\n1044020\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "8067:\n4.2\n3.8\n3.5\n5.0\n0.85\n")

    def test_eval_2(self):
        r = StringIO("16306:\n200235\n300286\n527248\n1785862\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "16306:\n4.2\n3.8\n3.8\n4.3\n0.67\n")

    def test_eval_3(self):
        r = StringIO("5022:\n339062\n805853\n2496212\n820006\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "5022:\n4.4\n3.0\n3.9\n1.8\n1.18\n")

    def test_eval_4(self):
        r = StringIO("17750:\n755373\n1146458\n1640708\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "17750:\n3.1\n3.9\n2.6\n0.57\n")

# ----
# main
# ----			
if __name__ == '__main__':
    main()

""" #pragma: no cover
% coverage3 run --branch TestNetflix.py >  TestNetflix.out 2>&1



% coverage3 report -m                   >> TestNetflix.out



% cat TestNetflix.out
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Netflix.py          27      0      4      0   100%
TestNetflix.py      13      0      0      0   100%
------------------------------------------------------------
TOTAL               40      0      4      0   100%

"""
