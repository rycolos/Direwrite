#!/bin/bash

ps -ef | grep direwolf | grep -v grep | awk '{print $2}' | xargs kill