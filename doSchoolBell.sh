#!/bin/sh

PATH=/usr/local/bin:${PATH}
AUDIO_FILE=${1}
CHANNEL_ID=${2}
SCRIPT_DIR=$(cd $(dirname $0); pwd)

nohup python3 ${SCRIPT_DIR}/discordbot.py ${AUDIO_FILE} ${CHANNEL_ID} >${SCRIPT_DIR}/bot_start.log 2>&1 &
