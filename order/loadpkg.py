import os
import sys

"""
Load root project directory to PYTHONPATH and make sub directory package could import.
"""
curr = os.path.abspath(__file__)
curr_dir = os.path.dirname(curr)
parentdir = os.path.dirname(curr_dir)
sys.path.insert(0, parentdir)
