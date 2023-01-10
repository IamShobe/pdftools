# Scripts - day to day useful scripts
## Installing
```bash
poetry install
```

## Run
```bash
poetry shell
```

## Install locally
```bash
pipx install git+https://github.com/IamShobe/scripts.git
```
this will install scripts package and install all the tools in this repo.

## Available scripts

### pdftools
All commands support `-o` flag (output) - if not specified - it will output into `out.pdf` file in 
current working directory.

- `unlock` - unlocks a pdf using password.
  ```bash
  pdftools unlock <source> -p <password> [-o <dest>]
  ```
- `extract-page` - extract a single page.
  ```bash
  pdftools extract-page <source> <page_number> [-o <dest>] [-p <password>]
  ```
- `merge` - merge multiple pdfs.
  ```bash
  pdftools merge <pdf> <pdfs>... [-o <dest>]
  ```
