#!/bin/bash
# displays the body of the response
curl -s -X POST "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
