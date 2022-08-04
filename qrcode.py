import qrcode
from PIL import Image

img = qrcode.make("https://open.spotify.com/album/7wbzi5MgYL57QS4OXTcxGS?si=d5bb554e2c144dcd")

img.save("qr.png")
