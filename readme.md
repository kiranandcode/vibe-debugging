# ⚡Vibe debugging - for when "your" vibe-programs don't work

> Vibe-programmed a bit too hard and now "your" code doesn't work?
> Sounds like it's time for some ✨vibe✨ debugging~

A dumb prototype of interactive debugging with LLMs 🤢. (Yes, this
demo was inspired purely based off the name).  You get a **live web
interface** for LLDB, plus ChatGPT-style chat that sees your stack,
source, and frames. 

![example of what it looks like](https://raw.githubusercontent.com/kiranandcode/vibe-debugging/main/examples/vibe-debugging.png)

## 🚀 Quickstart
Usage:

```
$ clang -g ./example/test_program.c -O0 -o a.out
$ python3 ./vibe_debugging.py ./a.out
```

## 📦 Requirements

You'll need flask to run this:
```
pip install flask flask_socketio
```
You'll also an OpenRouter API key -- it's free (uses open models), but you'll need to register.
```
export OPENROUTER_API_KEY="<your-api-key-goes-here>"
```

## 🧪 Example program to test
```c
// example/test_program.c
#include <stdio.h>

int main() {
    int *x = NULL;
    printf("x = %d\n", *x); // crash: NULL dereference
    return 0;
}
```
Compile with:
```
clang -g ./example/test_program.c -O0 -o a.out
```
Then:
```
python3 vibe_debugging.py ./a.out
```
