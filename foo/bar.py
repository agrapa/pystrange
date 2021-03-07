#!/usr/bin/env python3
#import pkg_resources
#pkg_resources.declare_namespace('foo')
import foo.pie
from foo.pie import add


if __name__ == "__main__":
    add()
