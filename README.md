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
- `unlock_pdf` - unlocks a pdf using password.
  ```bash
  pdftools unlock <source> <dest> -p <password>
  ```
- `extract_page` - extract a single page.
  ```bash
  pdftools extract-page <source> <dest> <page_number> [-p <password>]
  ```
