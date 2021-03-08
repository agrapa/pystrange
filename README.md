Experiment 1: try to run as is from the root directory by typing "python3 foo/bar.py" from the command line. You get an error.

Experiment 2:

mv foo/foo.py foo/foo2.py

try "python3 foo/bar.py" again

Experiment 3:

rename foo/foo2.py back to its original name: "mv foo/foo.py foo/foo2.py"

now uncomment lines 2&3 from foo/bar.py and try again "python3 foo/bar.py"

Does this follow what https://www.python.org/dev/peps/pep-0420/ explains?
