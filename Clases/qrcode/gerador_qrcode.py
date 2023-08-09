import qrcode
import os

class QRCodeGenerator:
    def generate_qrcode(self, data):
        qr_code = qrcode.make(data)
        return qr_code

    def save_qrcode(self, qr_code, filename):
        save_dir = os.path.join(os.getcwd(), "img2")
        os.makedirs(save_dir, exist_ok=True)
        full_path = os.path.join(save_dir, filename)
        qr_code.save(full_path)



