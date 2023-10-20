#!/bin/bash
. ./.venv/bin/activate
set -a && . ./.env && set +a
uvicorn app.main:app --reload & \
cloudflared tunnel run ubuntu-server-1 &
