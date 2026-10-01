# Mini URL Shortener

A simple program that turns long URLs into short codes and looks them up again.

It only uses the `random` module. No installs needed.

## How to run

```bash
python main.py
```

> Use `python3` on Mac/Linux if needed.

A menu appears. Type a number and press Enter.

## Menu

| Option | What it does |
|---|---|
| 1 | Shorten a URL (it asks you to type the URL) |
| 2 | Get the original URL from a short code |
| 3 | List all saved URLs |
| 4 | Quit |

## Sample session

```text
1. Shorten a URL
2. Get original URL from a code
3. List all URLs
4. Quit
Choose (1-4): 1
Enter URL:
https://example.com/a/very/long/page
Short code: g6vUwe
Choose (1-4): 2
Enter short code: g6vUwe
Original URL:
https://example.com/a/very/long/page
Choose (1-4): 3
g6vUwe ->
https://example.com/a/very/long/page
Choose (1-4): 1
Enter URL: hello
Invalid URL. It must start with http:// or https://
Choose (1-4): 2
Enter short code: abc123
Code not found.
```

## How it works

### Short codes

6 random letters/digits. If a code is already used, a new one is picked, so two URLs never share a code.

### Saving

Every URL is saved in `urls.txt` (one line per URL: `code url`), so data is still there next time you run the program.

### Errors

URLs must start with `http://` or `https://` and have no spaces. Unknown codes print `"Code not found."`

## Files

- `main.py` : the program
- `urls.txt` : created automatically the first time you run the program
