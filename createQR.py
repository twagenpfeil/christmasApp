import qrcode

website_url = "http://localhost:5000/"

qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10, 
    border=4,  
)

qr.add_data(website_url)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white")

qr_img.save("website_qr_code.png")