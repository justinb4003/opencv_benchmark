## OpenCV Bencnmarking 

Comparing Python and C++ implementations of OpenCV for performance.  The idea
is to expose a possible pitfal of doing it one way in Python that works but
subtely performs slower than the C++ counterpart.  In the end the hope is to
show how to properly handle things in Python so that you get the same
performance that C++ offers.

I'll be running these tests on amd64 and arm64 architectures, or in other words
on some common desktop computers and a Raspberry Pi or two.
