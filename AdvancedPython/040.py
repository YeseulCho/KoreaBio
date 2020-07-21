#! /usr/bin/env python

import readtxt

l = readtxt.read_tsv("read_sample.tsv")
l

readtxt.to_json(l)
