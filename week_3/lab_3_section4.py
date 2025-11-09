

import pyotp
import qrcode

#(one-time setup for a user)
issuer = "GoldAuth"
account = "student01@example.com"

secret = pyotp.random_base32()        
totp = pyotp.TOTP(secret)             #TOTP generator
uri = totp.provisioning_uri(name=account, issuer_name=issuer)

# saving a QR so you can scan it in your authenticator app
qrcode.make(uri).save("totp_qr.png")

print("Secret (store on server):", secret)
print("QR saved as totp_qr.png. Open it and scan with your Authenticator app.")

# Login (user enters code from phone) 
code = input("Enter the 6-digit code from your app: ").strip()
ok = totp.verify(code, valid_window=1)   #  small clock drift
print("Code valid?", ok)
