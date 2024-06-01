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
            background-color: #ffa500;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            width: 90%;
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            text-align: center;
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
    <div class="container">
        <div class="header">
            <h1>Pembayaran Berhasil</h1>
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