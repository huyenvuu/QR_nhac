import qrcode  # pyright: ignore[reportMissingModuleSource]

# WEBSITE URL (Thay link Netlify của bạn vào đây)
URL = 'https://huyenvuu.github.io/QR_nhac/'

# CREATE QR
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Mức H chịu lỗi cao, thích hợp in kèm logo hoặc dán nhỏ
    box_size=20,
    border=4
)

qr.add_data(URL)
qr.make(fit=True)

# GENERATE IMAGE
image = qr.make_image()
image.save("random_song_qr.png")

print("QR created successfully!")