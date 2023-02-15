# Python - Test-driven development

![img](https://lewandowski.io/images/tdd_flow.gif)

## Resources
### Read or Watch:
- [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html) (until “26.2.3.7. Warnings” included)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)

## Requirements
### Python Scripts
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)`
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

-------------------------
## Summary of tasks
- [0. Integers addition]
- [1. Divide a matrix]
- [2. Say my name]
- [3. Print square]
- [4. Text indentation]
- [5. Max integer - Unittest]
