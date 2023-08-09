from Clases.qrcode.gerador_qrcode import qrcode,QRCodeGenerator,os
if __name__ == "__main__":
    qr_generator = QRCodeGenerator()

    while True:
        user_choice = input("Digite 'sair' para sair ou qualquer outra coisa para criar um QR Code: ")
        
        if user_choice.lower() == 'sair':
            break

        link = input("Digite o link para criar o QR Code: ")
        qr_code = qr_generator.generate_qrcode(link)
        
        filename = f"qrcode_{len(os.listdir('img2')) + 1}.png"
        qr_generator.save_qrcode(qr_code, filename)
        print("QR Code criado e salvo.")

print("Programa encerrado.")