# convtemp
Figured I would do this in python as well. I have just completed a ["rust version"](https://github.com/aaronplagge/playground/blob/master/rust/convtemp/src/main.rs). 
I know here I will have access to `argparse`. Also while this should be simple
I will still setup a class just because. I am working on learning rust for my
own enlightenment and have been using python on some level for years now. I will
say that type conversions should be a lot easier than what I encountered with the
rust version

## Script versions

### simple
Tried to make this as simple as possible. No functions, classes, argparse or other 
extra things. Simple script from top to bottom.

### simple2
Simple changes. Added in functions. Also an additional function to check if a 
string can be converted to a float.

### with_argparse
This version has been modified to use `argparse`. Things I like about this version
is that using argparse take care of checking the arguments. This means that two 
functions were reduced to one and ensures the correct data type for input.
