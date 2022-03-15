import pyqrcode

link = 'https://www.instagram.com/lewismerinto/'

img = pyqrcode.create(link)

img.png("insta.png",scale=6)