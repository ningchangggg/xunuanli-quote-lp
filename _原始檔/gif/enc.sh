#!/bin/zsh
# usage: enc.sh sec fps
cd "$(dirname $0)"; s=$1; f=${2:-15}
ffmpeg -v error -y -framerate $f -i secframes/$s/%03d.png -vf "crop=iw:ih-4:0:0,fps=10,scale=600:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=160[p];[b][p]paletteuse=dither=bayer:bayer_scale=3" enc/$s.gif
ffmpeg -v error -y -framerate $f -i secframes/$s/%03d.png -vf "crop=iw:ih-4:0:0,scale=1080:-2:flags=lanczos,format=yuv420p" -c:v libx264 -crf 20 -movflags +faststart enc/$s.mp4
ls -la enc/$s.gif | awk '{print $5}'
