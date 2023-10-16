#!/bin/bash
python -m venv .venv && sh .venv/bin/activate
pip install -r requirements.txt
playwright install
playwright install-deps
cp .env.sample .env
echo '.env is created. please set env.'
