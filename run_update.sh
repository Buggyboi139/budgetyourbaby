#!/bin/bash

cd ~/budgetyourbaby || exit

python3 update_prices.py

if [[ -n $(git status --porcelain) ]]; then
    echo "Changes detected. Committing and pushing..."
    git add .
    git commit -m "Automated Amazon price/image update: $(date +'%Y-%m-%d %H:%M')"
    git push origin main
else
    echo "No price or image changes detected. Skipping push."
fi
