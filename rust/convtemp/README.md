# convtemp
This is a simple program / exrocise that will convert Celcius to Fahrenheit and vice versa.

The suggestion for this came from reading the Rust Book at the end of ["Chapter 3.5"](https://rust-book.cs.brown.edu/ch03-05-control-flow.html).

For managing command line arguments I did fine clap and a few others mentioned but 
for now I am going to keep it simple and just use std::env::args directly. 


## Thoughts:
This was interesting.  Couple of things I hit was apparently a `String` is not the same 
as a string literal (`&str`).  When trying to setup the `match` statement.  This led me 
to find the `to_str` method/function/call.

Another thing I encountered was when calculating the tempurature. No explicit conversion
from int to float (i32 to f64).  This led me to learn about `as f64` as well as when 
converting from Farhenheit to Celsius. Specifically converting the `5/9` to float. I feel
that the way I currently have it is not the best:
```
fn f_to_c (fahrenheit: i32) {
    let conv_ratio: f64 = 5.0 / 9.0;
    let ctemp = (fahrenheit as f64 - 32.0) * conv_ratio;
```
In fact I could just used the `5.0 / 9.0` directly instead of creating a variable with it.

## Next:
As I go learning things I may come back and rework this. Next I will create this in python.
