#!/bin/bash
port=8081

. .venv/bin/activate
set -a && . ./.env && set +a

if hostname -I 2>/dev/null; then
  # display URL for access to the local server.
  host_name="http://$(uname -n).local:$port"
  ip_addr="http://$(hostname -I | awk -F' ' '{print $1}'):$port"

  # 表示の整形のためのコード
  # 最も長い文字列の長さを取得
  max_len=${#ip_addr}
  if [ ${#host_name} -gt $max_len ]; then
    max_len=${#host_name}
  fi

  border_len=$(($max_len + 2))

  # 上部の枠
  printf "+"
  printf "%0.s-" $(seq 1 $border_len)
  echo "+"

  # host_name の出力部分
  printf "| %-${max_len}s |\n" "$host_name"

  # ip_addr の出力部分
  printf "| %-${max_len}s |\n" "$ip_addr"

  # 下部の枠
  printf "+"
  printf "%0.s-" $(seq 1 $border_len)
  echo "+"
else
  # on some systems, hostname -I doesn't work. show below message instead.
  echo "failed to get host address. perhaps, http://hostname:$port is host address."
fi

python -m http.server $port
