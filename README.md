try to run via foo/bar.py from the command line

now try:

mv foo/foo.py foo/foo2.py

try again


My results:

-> % foo/bar.py


Traceback (most recent call last):
  File "foo/bar.py", line 2, in <module>
    from foo.pie import add
  File "/Users/ariegrapa/dev/pystrange/foo/foo.py", line 1, in <module>
    from foo.pie import add
ModuleNotFoundError: No module named 'foo.pie'; 'foo' is not a package


ariegrapa@16inchArieMacBookPro [18:48:08] [~/dev/pystrange] [main *]


-> % mv foo/foo.py foo/foo2.py


ariegrapa@16inchArieMacBookPro [18:48:16] [~/dev/pystrange] [main *]


-> % foo/bar.py


adding
