import os
import sys


"""
Load root project directory to PYTHONPATH and make sub directory package could import.
"""
curr = os.path.abspath(__file__)
currdir = os.path.dirname(curr)
parentdir = os.path.dirname(currdir)
sys.path.insert(0, parentdir)
