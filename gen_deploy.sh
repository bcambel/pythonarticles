#!/bin/bash
python generate.py
echo "==========Git Add & Commit======="
git add .
git commit -m "$1"
git push
