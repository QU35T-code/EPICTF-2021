#!/bin/bash

curl -s http://ctf.intraside.xyz:3000/ | jq . | grep "guid" | cut -d '"' -f 4 | cut -c 1 | tr -d '\n'
