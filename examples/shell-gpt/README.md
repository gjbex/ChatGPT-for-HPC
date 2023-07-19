# shell-gpt

shell-gpt allows you to interact with ChatGPT from the command line.

  * The `src` directory contains source code used in these experiments.
  * The `output` directory contains the responses to the queries generated
    by ChatGPT 3.5 turbo.


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
1. `translate_code.txt`: translate a documented Python class into a
   C++ class.
1. `improve_code_quality.txt`: ask ChatGPT for suggestion on how to improve
   the code for a C++ class according to best practices and coding
   guidelines.
1. `improve_code_performance.txt`: ask ChatGPT to improve the performance
   of a Python function.
1. `refactor_code.txt`: ask ChatGPT to convert a Python AoS into a SoA.
1. `convert_makefile_to_cmakelists.txt`: ask ChatGPT to convert a Makefile
   into a CMakeLists.txt file.

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


## Conversations

You can also use shell-gpt to chat with ChatGPT.


### What is it?

1. `openmp_exercises_conversation.txt`: conversation with ChatGPT on
   a set of exercises on OpenMP programming.


### How to use it?

Each conversation has an identifier so that you can refer to it later.  To
start a conversation named "`openmp_exercises`" you can use the following.

```bash
$ sgpt --chat openmp_exercises "Can you suggest..."
```

Calling `sgpt` with the same identifier will continue the conversation for,
e.g., followup questions.
