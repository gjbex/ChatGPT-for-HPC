# GitHub Copilot

GitHub Copilot can be a huge help when writing code.
It will monitor what you do, and adapt to your coding style.

Here you can find a number of [asciinema](https://asciinema.org/)
screencast that show GitHub Copilot in action in the neovim editor.


## What is it?

1. `brownian_motion.cast`: [screencast](https://asciinema.org/a/Qn86ge2bxYLnn8cUFF7uumq1f)
   of writing a C++ application to simulate diffusion and compute the
   average distance the particle moved.
1. `counting_nucleotides.cast`: [screencast](https://asciinema.org/a/598907)
   of writing a C++ application to count nucleotides in a text file that contains a
   DNA sequence.
1. `command_line_arguments.cast`: [screencast](https://asciinema.org/a/613753) of writing
   a C++ function to handle command line arguments, as well as the corresponding header
   file.

## How to use?

You can view the screencast in your web browser by clicking the links above or
you can play asciinema casts on the command line as follows.

```bash
$ asciinema play brownian_motion.cast
```

To limit the idle time, use `-i`, to speedup the playback, use `-s`, e.g.,
```bash
$ asciinema play -i 1 -s 1.5 brownian_motion
```

Note that you may have to install asciinema on your system first.
