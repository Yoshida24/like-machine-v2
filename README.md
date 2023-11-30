# like-machine-v2

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=686856069&skip_quickstart=true)

Auto Like and Notify LINE.

## Usage

depends on:
- Python: 3.11.2
- pip: 22.3.1
- GNU Make: 3.81

supported OS:
- M1 Macbook Air Ventura 13.4.1
- Ubuntu 22.04.3 on Raspberry Pi 4 Model B Rev 1.2 (2GB)

```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.3 LTS
Release:	22.04
Codename:	jammy
```

## Getting Started

### Install API on Ubuntu Server
First of all, `update` apt and `pip`

```bash
apt update && apt upgrade -y && apt autoremove -y && apt autoclean -y
pip install --upgrade pip
```

install VSCode recommended extensions. This includes Linter, Formatter, and so on. Recommendation settings is written on `.vscode/extensions.json`.

Then, install dependencies:

```bash
make setup
```

Now you can run script:

```bash
make run
```

> **Note**
This project *does not* depends on `dotenv-python`. Instead, using below script.
> `set -a && source ./.env && set +a`


## Develop App
On usual develop, first you activate `venv` first like below.

```bash
source .venv/bin/activate
```

Save requirements:

```bash
pip freeze > requirements.txt
```

Deactivate venv:

```bash
deactivate
```
