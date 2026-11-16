# Data sources

Public GSS data as packaged by the `gssr` R data package (Kieran Healy), GitHub `kjhealy/gssr`,
commit `769d48c53df87e8c7bc3eecbb0432e92d5684cf1` (2026-03-12), GSS Cumulative 1972–2024 release 3.
Original source: NORC at the University of Chicago, General Social Survey.

Fetch (no account needed):

    GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/kjhealy/gssr && git -C gssr checkout 769d48c

SHA-256 of the files used:

    38712b98fe23598856f757c096e5d4be908f6a9f644f695fce62ba0db4e4627f  data/gss_all.rda
    83eafebbdfe13df25e901fceb4d8e29cd08c8f373d0b451cb6d57760f105e7f4  data/gss_panel06_long.rda
    8aab3a12faa93703422f6b15288c34572e60ae2585861272c2f9afcfb767f871  data/gss_panel08_long.rda
e3f0a3120194fb3b59a12be2eafd61eab3ea85ec1266ca2a5b07a5c57eb2c1ea      data/gss_panel10_long.rda
