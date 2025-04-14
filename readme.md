# ⚡Vibe debugging - for when "your" vibe-programs don't work

> Debugging is twice as hard as writing the code in the first
> place. Therefore, if you write the code as cleverly as possible, you
> are, by definition, not smart enough to debug it.

A dumb prototype of interactive debugging with LLMs 🤢. (Yes, this
demo was inspired purely based off the name).  Implements a live web
interface for LLDB, plus a ChatGPT-style chat that sees your stack,
source, and frames.

![example of what it looks like](https://raw.githubusercontent.com/kiranandcode/vibe-debugging/main/example/vibe-debugging.png)

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
