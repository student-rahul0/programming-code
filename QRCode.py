import qrcode

# Taking UPI ID As a input
upi_id = input("Enter your UPI ID = ")

# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Defining the payment URL based on the UPI ID and the payment app
# You can modify these URLs based on the payment apps you want to support

google_pay_url = f'upi://pay?pa={upi_id}&pn=Recient%20Name&mc=1234'

# Create QR Codes for each payment app
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR code to image file(optional)
google_pay_qr.save('google_pay_qr.png')

# Display the QR codes (you may need to install PIL/Pillow Library)
google_pay_qr.show()
