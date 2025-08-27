# İçe Aktarma
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Elektrikli cihazların enerji tüketimini hesaplamaya olanak tanıyan değişkenler
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# İlk sayfa
@app.route('/')
def index():
    return render_template('index.html')
# İkinci sayfa
@app.route('/atik_turu')
def atik():
    return render_template(
                            'atik.html'
                           )

# Üçüncü sayfa
@app.route('/atik_turu/plastik')
def plastikler():
    return render_template(
                            'plastik.html',                                                     
                           )
@app.route('/atik_turu/karton')
def karton():
    return render_template('karton.html')

# Hesaplama
@app.route('/atik_turu/kagit')
def kagitlar():
    return render_template('kagit.html')
                        
# Form
@app.route('/form')
def form():
    return render_template('form.html')

#Formun sonuçları
@app.route('/submit', methods=['POST'])
def submit_form():
    # Veri toplama için değişkenleri tanımlayın
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

      # Verileri bir dosyaya yazma
    with open('form.txt', 'a', encoding='utf-8') as f:
        f.write(f"Name: {name}\nEmail: {email}\nAddress: {address}\nDate: {date}\n\n")
   

    # Verilerinizi kaydedebilir veya e-posta ile gönderebilirsiniz
    return render_template('form_result.html', 
                           # Değişkenleri buraya yerleştirin
                           name=name,
                           email=email,
                           address=address,
                           date=date,
                           )

app.run(debug=True)
