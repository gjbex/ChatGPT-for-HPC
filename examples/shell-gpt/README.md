# shell-gpt

shell-gpt allows you to interact with ChatGPT from the command line.


## Code generation

Examples of code generation using ChatGPT.


### What is it?

1. `generate_documentation.txt`: ask ChatGPT to suggest a docstring
   for a Python function in scipy-format.
1. `add_error_handling.txt`: ask ChatGPT to add error handling to
   a Python function taking into account the semantics of the
   function's parameters.
1. `generate_unit_tests.txt`: ask ChatGPT to generate unit tests
   for edge and corner cases for use with pytest.
1. `generate_documentation_distance.txt`: ask ChatGPT to suggest a
   docstring for a Python function in scipy-format.
1. `output`: directory containing the output of the queries.


### How to use?

You can pass the contents of a file as a command line parameter to
an application as a string using the following syntax:
```bash
$ sgpt  --code  "$(<generate_documentation.txt)"
```


## Shell commands

Examples of generating shell commands.


### What is it?

1. `find_functions_shell.txt`: find the names of Python functions
   in scripts and modules in the current working directory.


### How to use?

You can pass the contents of a file as a command line parameter to
an application as a string using the following syntax:
```bash
$ sgpt  --shell  "$(<generate_documentation.txt)"
```
Note that you are prompted what to do with the command, where executing
it is an option.  Do so at your own peril.
