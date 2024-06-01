from flask import Flask, request,jsonify,render_template
import time

app = Flask(__name__)

data = False

@app.route('/set', methods=['GET'])
def set_close_flag():
    # Simpan flag untuk menutup WinForm
    global data
    data = True
    time.sleep(5)
    # Simulasikan proses yang lama
    # Periksa flag
    if data:
        # Tutup WinForm
        print("Menutup WinForm...")
        # Replace with actual WinForm closing code
    else:
        print("Penutupan WinForm dibatalkan")

    time.sleep(5)
    data = False

    html ='''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pembayaran Berhasil</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            position: relative;
            overflow: hidden;
        }

        .background-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('https://media.canva.com/v2/image-resize/format:PNG/height:550/quality:100/uri:s3%3A%2F%2Fmedia-private.canva.com%2FYCI4A%2FMAGG69YCI4A%2F1%2Fp.png/watermark:F/width:388?csig=AAAAAAAAAAAAAAAAAAAAAOdn6APfhd_tAI44ufr0uJssQ5N3OGojleNb3r7o-UFe&exp=1717285179&osig=AAAAAAAAAAAAAAAAAAAAAKPe2ztqdTLv2rbt5r2dPou_mhbT2QzehOiMhI_uOAFj&signer=media-rpc&x-canva-quality=thumbnail_large'); /* Replace with your image URL */
            background-size: cover;
            background-position: center;
            opacity: 0.5; /* Adjust the opacity as needed */
            z-index: -1;
        }

        .container {
            width: 90%;
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.9); /* Slightly transparent white background */
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            border-radius: 20px;
            text-align: center;
            z-index: 1;
            position: relative;
        }

        .header {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .header img {
            width: 200px;
            height: 100px;
        }
        
        .header h1 {
            font-size: 24px;
            color: #4CAF50;
        }

        .content {
            padding: 20px 0;
        }

        .buttons button {
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .buttons button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="background-overlay"></div>
    <div class="container">
        <div class="header">
            <img src="https://media.canva.com/v2/image-resize/format:PNG/height:97/quality:100/uri:s3%3A%2F%2Fmedia-private.canva.com%2FvVUXU%2FMAGG6xvVUXU%2F1%2Fp.png/watermark:F/width:200?csig=AAAAAAAAAAAAAAAAAAAAAJBKYIRcEW0E3k0mfprsRTVY12OM_grnmqOja7qQHta6&exp=1717285088&osig=AAAAAAAAAAAAAAAAAAAAAKZCedbOWfjjbXbhamgglm4eDUB98KPM-I61M6GvGXap&signer=media-rpc&x-canva-quality=thumbnail" alt="Logo CoffeeSharp">
            <h1>Pembayaran Berhasil</h1>
            <img src="https://www.e2pay.co.id/static/media/imgFooter.03070f48b1868f2252f5.gif" alt="gif bayar">
        </div>
        <div class="content">
            <p>Pembayaran Anda telah diproses dan berhasil pada tanggal <b id="tanggal"></b> jam <b id="waktu"></b>.</p>
            <p>Sampai Jumpa Kakak... Belanja Lagi ya :D</p>
            <div class="buttons">
                <button onclick="window.close()">Tutup Tab</button>
            </div>
        </div>
    </div>
    <script>
        const tanggal = new Date();
        document.getElementById('tanggal').innerText = tanggal.toLocaleDateString('id-ID', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
        document.getElementById('waktu').innerText = tanggal.toLocaleTimeString('id-ID', {
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        });
    </script>
</body>
</html>


'''
    # Kembalikan respons JSON
    # return jsonify({'status': 'PEMBAYARAN BERHASIL'})
    # return render_template("index.html")
    return html

@app.route('/check', methods=['GET'])
def check_close_flag():
    # Periksa flag
    close_flag = data # Simpan flag untuk menutup WinForm

    # Kembalikan status flag dalam respons JSON
    return jsonify({'close_flag': close_flag})

if __name__ == '__main__':
    app.run(debug=True)