**You:**

I would like to use m4 to replace text using a macro.  However, the text to replace is part of a string that contains an underscore, and I only want to replace the part of the string that comes after the underscore.
For instance, the M4 tempale would contain 'test_SOMETING' and that should become 'test_14'.
What is the syntax to use in the template to achieve this?

------------------

**ChatGPT:**

In the M4 macro processor, you can use the `changequote` and `define` directives to replace specific parts of text strings. However, note that M4 isn't really optimized for partial string replacements like regular expression engines are. Therefore, a straightforward solution for replacing a part of a string that comes after an underscore isn't readily available.

Nonetheless, a workaround could be to break the string into parts, replace the relevant part, and then concatenate the string again. Here's a basic example:


- First, let's change the quote marks, just to be safe:

```scss
Copy code
changequote([,])

```
- Next, define a macro to do the replacement:

```css
Copy code
define([replace_suffix], [  define([prefix], translit($1, [_], [ ]))
  define([suffix], $2)
  prefix`_'suffix
])

```
- Use the macro to replace the suffix part after the underscore:

```css
Copy code
replace_suffix([test_SOMETHING], [14])

```

When you run this, the `replace_suffix` macro will break `test_SOMETHING` into `test` and `SOMETHING`, replace `SOMETHING` with `14`, and then concatenate it back to `test_14`.

Please note that the `translit` function is used just to split the original string based on the underscore; it's a bit of a hack. The `translit` function replaces the underscore with a space, effectively splitting the string into two parts that M4 can handle separately. Then, the suffix is replaced and the string is reconstructed.

This example assumes you know the structure of the string and you can provide it as an argument to the `replace_suffix` macro. For more dynamic scenarios, things could get a bit more complex.



------------------

**You:**

In step one, when the quotes are changed, does that mean that a subsitution variable would be indicacted as [TOREPLACE]?

------------------

**ChatGPT:**

In M4, the `changequote` directive changes the characters used for quoting strings in M4 macros and expansions. By default, the quote characters are the backtick (`) for the beginning of a quoted string and the single quote (') for the end of a quoted string. Changing the quote characters to square brackets, as in `changequote([,])`, allows you to use square brackets for quoting instead.

However, changing the quote characters doesn't directly affect how you indicate substitution variables or placeholders in your macros. The purpose of changing the quote characters is mainly to avoid conflicts when the default quote characters appear in the text you are working with.

In the example given, the `define` directive was used to create a macro named `replace_suffix`, and `$1` and `$2` were used as placeholders for the arguments passed into that macro.

So, to clarify, changing the quote character wouldn't change how you indicate a substitution variable like `TOREPLACE`. You'd still use M4's standard `$1`, `$2`, etc., to refer to positional parameters when defining macros.



------------------

**You:**

How can I indicate a word boundary before and after an M4 macro?

------------------

**ChatGPT:**

In M4, the concept of a "word boundary" isn't as explicit as it is in regular expressions. M4 macros are replaced as-is, without regard for whether they are adjacent to other letters, numbers, or characters. That said, you can work around this limitation to ensure that a macro expands only when it appears as a standalone word.

One approach is to wrap your macro name in special characters when you define and invoke it. These special characters act as makeshift "word boundaries." Later, you can remove these special characters after all macro expansions have taken place.

Here's an example:


- Change the quote marks (optional but often helpful):

```scss
Copy code
changequote([, ])

```
- Define your macro with special characters (let's say `#`):

```css
Copy code
define([#my_macro#], [replacement_text])

```
- In your text, use the special characters to indicate where the macro should be expanded:

```bash
Copy code
This is a test: #my_macro#.

```
- Remove the special characters post-expansion (if needed):

```css
Copy code
define([remove_special], [translit($1, [#], [])])

```
Then use:

```bash
Copy code
remove_special(This is a test: #my_macro#.)

```

Note that in the last step, the `translit` function is used to remove the `#` characters. If you know that no other `#` characters should appear in the text, you can apply this function to the entire document after all macro expansions have taken place.

By using special characters to signify word boundaries, you're manually enforcing the boundary conditions. You would need to make sure that you consistently use these special characters when you want the macro to expand as a standalone word.



------------------

**You:**

What should I do when 14 is passed in via the command line when invoking m4?

------------------

**ChatGPT:**

If you want to pass a value like `14` from the command line when invoking M4, you can use the `-D` option to define a macro. This way, you can make the replacement more dynamic. Here's how you could approach it:


- Define your macros in your M4 file, e.g., `my_template.m4`. Let's say you have a placeholder macro called `SOMETHING`:

```m4
Copy code
changequote([, ])

define([replace_suffix], [
  define([prefix], translit($1, [_], [ ]))
  define([suffix], SOMETHING)
  prefix`_'suffix
])

```
- In your shell command, invoke M4 and pass in `14` as the definition for `SOMETHING`:

```bash
Copy code
m4 -DSOMETHING=14 my_template.m4

```
- Now, when `replace_suffix([test_SOMETHING], [14])` is invoked in your M4 template, the `SOMETHING` macro will be replaced by `14`, and you'll get `test_14`.

In this example, the `-D` flag defines a macro named `SOMETHING` with the value `14`. When M4 processes the file, it replaces `SOMETHING` with `14`. You can adapt this example to fit more complex scenarios or templates.

This allows you to pass values into your M4 templates from the command line, making the replacement process much more dynamic.



------------------

**You:**

Could you achieve the same with the format macro?

------------------

**ChatGPT:**

The `format` built-in function in M4 can be used to produce formatted strings, similar to printf-style formatting in languages like C. However, it may not be suitable for replacing specific portions of a string after a certain character like the underscore (`_`). The `format` function is more about specifying how individual variables should be converted into string representations.

That said, if you want to pass a value like `14` from the command line and incorporate it into your M4 templates, you could use `format` to assemble the strings in a controlled way, although it would likely be overkill for simple replacements.

Here's how you might use `format` for this scenario, assuming you've passed in `14` as a definition for `SOMETHING` from the command line:


- In your M4 file, say `my_template.m4`:

```m4
Copy code
define([replace_suffix_format], [
  define([prefix], translit($1, [_], [ ]))
  define([formatted_string], format([%s_%d], prefix, SOMETHING))
  formatted_string
])

```
- In your shell command, define `SOMETHING` as `14`:

```bash
Copy code
m4 -DSOMETHING=14 my_template.m4

```
- In your M4 template, you can then use:

```m4
Copy code
replace_suffix_format([test_SOMETHING])

```

This would also produce `test_14`. Here, the `format` function takes a format string and a list of expressions, formatting the expressions according to the format string. `%s` will be replaced by the string value of `prefix`, and `%d` will be replaced by the integer value of `SOMETHING`.

While this can be an interesting exercise, using `format` in this way is not its typical use-case and might be considered a bit of overengineering for simple text replacements.



------------------

