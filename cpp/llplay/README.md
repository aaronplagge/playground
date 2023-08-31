#llplay.cpp

So for some reason I got it in my head to play with pointers and create a basic linked list.

I was watching a video about data stuctures [here](https://youtu.be/wv90D4dZUA0). Watching this video and thinking over how things would be organized I decided to play with linked lists.  

I have had previous classes in C++ a long time ago so I am somewhat familiar with basic syntax and even pointers.  Though I still wanted to refresh my memory so I started watching [this playlist](https://youtube.com/playlist?list=PL43pGnjiVwgSSRlwfahAuIqoJ8TfDIlHq) on Youtube. As expected I was already familiar with basic pointer creation and usage.  Though when I got to the video on smart pointers I found that part was new to me.  

Initially for what I was experimenting with I was using the old style pointers:

```
struct node n1{NULL, 3};
struct node* head = &n1;
```

I read somewhere that while you can use the old style pointers it is better to use the smart pointers.  Seeing as I was creating a basic linked list I new I had to use the `shared_ptr` as it was possible that multiple things would be pointed to one node.  So I started working with and learning how to use the `shared_ptr`'s.  I got to the point of creating multiple nodes and then cycling through the linked list printing out the number for each node.  So this `llplay.cpp` file is the result.

One other node is that for compiling I wanted to enable some warnings to help point out possible issues.  So after some research I ended up with the following `g++` command:

```
g++ -Wall -Wextra -Wpedantic -Wcast-align -Wcast-qual -Wdisabled-optimization -Wduplicated-branches -Wduplicated-cond -Wformat=2 -Wlogical-op -Wmissing-include-dirs -Wnull-dereference -Woverloaded-virtual -Wpointer-arith -Wshadow -Wswitch-enum -Wvla -o out llplay.cpp
```

Now I am thinking I should do this and create a binary tree from the random numbers then print out the sorted numbers.  Or maybe a min heap or max heap. 
