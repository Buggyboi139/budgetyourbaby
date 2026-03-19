#!/bin/bash

cd ~/budgetyourbaby || exit

~/budgetyourbaby/scraper_env/bin/python update_prices.py

if [[ -n $(git status --porcelain products.json) ]]; then
    echo "Changes detected in products.json. Committing and pushing..."
    
    git add products.json
    
    git commit -m "Automated Amazon price/image update: $(date +'%Y-%m-%d %H:%M')"
    git push origin main
else
    echo "No price or image changes detected. Skipping push."
fi
