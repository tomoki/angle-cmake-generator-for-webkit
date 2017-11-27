#!/usr/bin/env python
#coding:utf-8

import ast
import sys

# gypi file is JSON with following extensions;
# - Python style comments
# - Trailing comma
def read_gypi_string(s):
    return ast.literal_eval(s)

def make_cmake_definition(name, sources):
    ret = ""
    ret += "set(" + name + "\n"
    for s in sources:
        ret += "    " + s + "\n"
    ret += ")"
    return ret

def main():
    with open(sys.argv[1], "r") as f:
        js   = read_gypi_string(f.read())
        vars = js["variables"]
        for key in vars:
            print(make_cmake_definition(key, vars[key]))

# Usage: python main.py libGLESv2.gypi
if __name__ == "__main__":
    main()