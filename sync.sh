DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
rsync -avz -e ssh $DIR/esp8266/ pi@192.168.0.106:/opt/Espressif/source-code/water
