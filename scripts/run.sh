#!/bin/bash
set -a && source ./.env && set +a
source ./.venv/bin/activate && \
uvicorn app.main:app --reload & \
cloudflared tunnel run ubuntu-server-1 &
