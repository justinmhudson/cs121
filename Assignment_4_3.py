#!/usr/bin/env python
# coding: utf-8

################################

# Student: Justin Hudson
# Instructor: Kaleab Gorfu
# CS 121: Python for DS and ML
# Date: 19/04/2026

################################

#   i.
import random
get_ipython().run_line_magic('timeit', 'rolls_list = [random.randrange(1, 7) for i in range(0, 6_000_000)]')


#   ii.
import numpy as np
get_ipython().run_line_magic('timeit', 'rolls_array = np.random.randint(1, 7, 6_000_000)')

