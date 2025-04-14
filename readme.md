# Vibe debugging - A really really dumb prototype

Usage:

```
$ clang -g ./example/test_program.c -O0 -o a.out
$ python3 ./vibe_debugging.py ./a.out
```

## Requirements

You'll need flask to run this:
```
pip install flask flask_socketio
```
Also an OpenRouter API key (uses a free model, so no money needed, but you'll need to register).

```
export OPENROUTER_API_KEY="<your-api-key-goes-here>"
```
