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
    # Kembalikan respons JSON
    # return jsonify({'status': 'PEMBAYARAN BERHASIL'})
    return render_template("index.html")

@app.route('/check', methods=['GET'])
def check_close_flag():
    # Periksa flag
    close_flag = data # Simpan flag untuk menutup WinForm

    # Kembalikan status flag dalam respons JSON
    return jsonify({'close_flag': close_flag})

if __name__ == '__main__':
    app.run(debug=True)
