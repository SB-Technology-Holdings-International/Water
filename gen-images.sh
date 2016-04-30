cd ~/Code/Water
rm app/images/touch/*
cp -f logo.svg app/images/logo.svg
convert -background transparent -resize 192x192 logo.svg app/images/touch/chrome-splashscreen-icon-384x384.png
convert logo.svg -resize 152x152 app/images/touch/apple-touch-icon.png
convert -background transparent -resize 192x192 logo.svg app/images/touch/chrome-touch-icon-192x192.png
convert -background transparent -resize 128x128 logo.svg app/images/touch/icon-128x128.png
convert -background transparent -resize 144x144 logo.svg app/images/touch/ms-icon-144x144.png
convert -background transparent -resize 144x144 logo.svg app/images/touch/ms-touch-icon-144x144-precomposed.png
convert -background transparent -resize 16x16 logo.svg app/favicon.ico.png
convert -background transparent -resize 16x16 logo.svg app/favicon.ico
convert -background transparent -resize 1024x1024 logo.svg app/images/touch/video-large-1024x1024.png
convert -background transparent -resize 120x120 logo.svg app/images/touch/oauth-120x120.png
