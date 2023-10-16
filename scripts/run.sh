#!/bin/bash
sh ./.venv/bin/activate
set -a && sh ./.env && set +a
uvicorn app.main:app --reload & \
cloudflared tunnel run ubuntu-server-1 &
