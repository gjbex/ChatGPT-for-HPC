# bard-rs

[bard-rs](https://lib.rs/crates/bard-rs) is a command line client for
Google Bard that will save your conversation as a markdown file.

You have to provide a cookie to authenticate.  The procedure to get
that is explained in the documentation on the web site.

This can be stored in a `.env` file in your home directory.

Note that your conversation may be analyzed to improve Bard's
performance, so take care not to include any sensitive information.


## How use use it?

You can run the application as follows.

```bash
$ bard-rs -p ./
```

This will save the conversation in the current working directory.


## What is it?

1. [`slurm_jobscript.md`](slurm_jobscript.md): ask Bard to generate
   a slurm job script for a hybrid MPI/OpenMP application.  Some
   iterations were required to get it right.
