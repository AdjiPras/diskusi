from flask import Flask, request, jsonify, render_template, json, redirect, redirect, url_for, session, make_response
# from flask_mongoengine import MongoEngine #ModuleNotFoundError: No module named 'flask_mongoengine' = (venv) C:\flaskmyproject>pip install flask-mongoengine
from datetime import date, datetime
from models import MModel
from time import sleep
from database import dbBrainly
from pymongo import MongoClient

import pymongo
import datetime 
import config2

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["brainlydb"]

application = Flask(__name__)
application.config['SECRET_KEY'] = 'sfh7^erw9*(%sadHGw%R'

# today = datetime.today()
model = MModel()
html_source = ''
 
# app = Flask(__name__)
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'brainlydb',
#     'host': 'localhost',
#     'port': 27017
# }
# db = MongoEngine()
# db.init_app(app)

# ======================================================================================================= 
# Index
@application.route('/')
def index():
	if 'data_nama' in session:
		data_nama = session['data_nama']
		return render_template('index_diskusi.html', data_nama=data_nama)
	return render_template('form_login.html')

# login	
@application.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if model.authenticate(username, password):
			data_nama = model.getUserForSession(username)
			session['data_nama'] = data_nama
			return redirect(url_for('index'))
		msg = 'Username/Password salah.'
		return render_template('form_login.html', msg=msg)
	return render_template('form_login.html')

# Logout	
@application.route('/logout')
def logout():
	session.pop('data_nama', '')
	return redirect(url_for('index'))

# SOP
@application.route('/sop')
def sop():
	if 'data_nama' in session:
		data_nama = session['data_nama']
		return render_template('sop.html', data_nama=data_nama)
	return render_template('form_login.html')

# TEAM
@application.route('/team')
def team():
	if 'data_nama' in session:
		data_nama = session['data_nama']
		return render_template('team.html', data_nama=data_nama)
	return render_template('form_login.html')

# ========================== PERTANYAAN ==========================

@application.route('/pertanyaan')
def pertanyaan():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        data_nama = data_nama[1]
        container_pertanyaan = [] 
        container_pertanyaan = model.selectPertanyaan()
        return render_template('pertanyaan.html', container_pertanyaan=container_pertanyaan, data_nama=data_nama)
    return render_template('form_login.html')

@application.route('/insert_pertanyaan', methods=['GET', 'POST'])
def insert_pertanyaan():
	if 'data_nama' in session:
		if request.method == 'POST':
			no = request.form['no']
			username = request.form['username']
			kategori = request.form['kategori']
			pertanyaan = request.form['pertanyaan']
			penjawab = '-'
			jawaban = '-'
			tanggal_jawab = request.form['tanggal_jawab']
			ranking = '-'
			keterangan = '-'
			data_p = (no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan)
			model.insertPertanyaan(data_p)
			return redirect(url_for('semua'))
		else:
			data_nama = session['data_nama']
			return render_template('insert_pertanyaan.html', data_nama=data_nama)
	return render_template('form_login.html')

@application.route('/answer_pr', methods=['GET', 'POST'])
def answer_pr():
    if 'data_nama' in session:
        no = request.form['no']
        username = request.form['username']
        kategori = request.form['kategori']
        pertanyaan = request.form['pertanyaan']
        penjawab = request.form['penjawab']
        jawaban = request.form['jawaban']
        tanggal_jawab = request.form['tanggal_jawab']
        ranking = "-"
        keterangan = "-"
        data_pr = (username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan, no)
        model.updatePertanyaan(data_pr)
        return redirect(url_for('semua'))
    return render_template('form_login.html')

@application.route('/answer/<no>')
def answer(no):
    if 'data_nama' in session:
        data_pr = model.getPertanyaanbyNo(no)
        data_nama = session['data_nama']
        return render_template('edit_pertanyaan.html', data_pr=data_pr, data_nama=data_nama)
    return render_template('form_login.html') 

# KOREKSI
@application.route('/koreksi_pr', methods=['GET', 'POST'])
def koreksi_pr():
    if 'data_nama' in session:
        no = request.form['no']
        username = request.form['username']
        kategori = request.form['kategori']
        pertanyaan = request.form['pertanyaan']
        penjawab = request.form['penjawab']
        jawaban = request.form['jawaban']
        tanggal_jawab = request.form['tanggal_jawab']
        ranking = request.form['ranking']
        keterangan = request.form['keterangan']
        data_pr = (username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan, no)
        model.koreksiPertanyaan(data_pr)
        return redirect(url_for('semua'))
    return render_template('form_login.html')

@application.route('/koreksi_pertanyaan/<no>')
def koreksi_pertanyaan(no):
    if 'data_nama' in session:
        data_pr = model.getPertanyaanbyNo(no)
        data_nama = session['data_nama']
        return render_template('koreksi.html', data_pr=data_pr, data_nama=data_nama)
    return render_template('form_login.html') 

@application.route('/delete_pertanyaan/<no>')
def delete_pertanyaan(no):
    if 'data_nama' in session:
        model.deletePertanyaan(no)
        return redirect(url_for('semua'))
    return render_template('form_login.html')

# =================================  REKAP  ==========================================
# REKAP
@application.route('/rekap')
def rekap():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_rekap = [] 
        container_rekap = model.selectRekap()
        return render_template('rekap.html', container_rekap=container_rekap, data_nama=data_nama)
    return render_template('form_login.html')

# ================================ KATEGORI ============================================
# SEMUA
@application.route('/semua')
def semua():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_semua = [] 
        container_semua = model.selectSemua()
        return render_template('semua.html', container_semua=container_semua, data_nama=data_nama)
    return render_template('form_login.html')

# MAKANAN
@application.route('/makanan')
def makanan():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_makanan = [] 
        container_makanan = model.selectMakanan()
        return render_template('makanan.html', container_makanan=container_makanan, data_nama=data_nama)
    return render_template('form_login.html')

# MINUMAN
@application.route('/minuman')
def minuman():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_minuman = [] 
        container_minuman = model.selectMinuman()
        return render_template('minuman.html', container_minuman=container_minuman, data_nama=data_nama)
    return render_template('form_login.html')

# PAKAIAN
@application.route('/pakaian')
def pakaian():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_pakaian = [] 
        container_pakaian = model.selectPakaian()
        return render_template('pakaian.html', container_pakaian=container_pakaian, data_nama=data_nama)
    return render_template('form_login.html')

# DESAIN
@application.route('/desain')
def desain():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_desain = [] 
        container_desain = model.selectDesain()
        return render_template('desain.html', container_desain=container_desain, data_nama=data_nama)
    return render_template('form_login.html')

# MANUFAKTUR
@application.route('/manufaktur')
def manufaktur():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_manufaktur = [] 
        container_manufaktur = model.selectManufaktur()
        return render_template('manufaktur.html', container_manufaktur=container_manufaktur, data_nama=data_nama)
    return render_template('form_login.html')

# TEKNOLOGI
@application.route('/teknologi')
def teknologi():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_teknologi = [] 
        container_teknologi = model.selectTeknologi()
        return render_template('teknologi.html', container_teknologi=container_teknologi, data_nama=data_nama)
    return render_template('form_login.html')

# PARIWISATA
@application.route('/pariwisata')
def pariwisata():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_pariwisata = [] 
        container_pariwisata = model.selectPariwisata()
        return render_template('pariwisata.html', container_pariwisata=container_pariwisata, data_nama=data_nama)
    return render_template('form_login.html')

# TRANSPORT
@application.route('/transport')
def transport():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_transport = [] 
        container_transport = model.selectTransport()
        return render_template('transport.html', container_transport=container_transport, data_nama=data_nama)
    return render_template('form_login.html')

# ONLINE SHOP
@application.route('/onlineshop')
def onlineshop():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_onlineshop = [] 
        container_onlineshop = model.selectOnlineShop()
        return render_template('onlineshop.html', container_onlineshop=container_onlineshop, data_nama=data_nama)
    return render_template('form_login.html')

# PERIKLANAN
@application.route('/periklanan')
def periklanan():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_periklanan = [] 
        container_periklanan = model.selectPeriklanan()
        return render_template('periklanan.html', container_periklanan=container_periklanan, data_nama=data_nama)
    return render_template('form_login.html')

# ARTIKEL SEO
@application.route('/artikelseo')
def artikelseo():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_artikel_seo = [] 
        container_artikel_seo = model.selectArtikelSeo()
        return render_template('artikel_seo.html', container_artikel_seo=container_artikel_seo, data_nama=data_nama)
    return render_template('form_login.html')

# ============================ DATA FREELANCER ===================================================
# SIGN UP
@application.route('/insert_signup', methods=['GET', 'POST'])
def insert_signup():
    if request.method == 'POST':
        id_freelancer = request.form['id_freelancer']
        username = request.form['username']
        password = request.form['password']
        nama = request.form['nama']
        tipe_akses = request.form['tipe_akses']
        data_signup = (id_freelancer, username, password, nama, tipe_akses)
        model.insertSignUp(data_signup)
        return redirect(url_for('freelancer'))
    else:
        return render_template('form_signup.html')

@application.route('/freelancer')
def freelancer():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        data_nama = data_nama[1]
        container_freelancer = [] 
        container_freelancer = model.selectFreelancer()
        return render_template('freelancer.html', container_freelancer=container_freelancer, data_nama=data_nama)
    return render_template('form_login.html')

@application.route('/insert_freelancer', methods=['GET', 'POST'])
def insert_freelancer():
	if 'data_nama' in session:
		if request.method == 'POST':
			id_freelancer = request.form['id_freelancer']
			username = request.form['username']
			password = request.form['password']
			nama = request.form['nama']
			tipe_akses = request.form['tipe_akses']
			data_f = (id_freelancer, username, password, nama, tipe_akses)
			model.insertFreelancer(data_f)
			return redirect(url_for('freelancer'))
		else:
			data_nama = session['data_nama']
			return render_template('insert_freelancer.html', data_nama=data_nama)
	return render_template('form_login.html')

@application.route('/update_fr', methods=['GET', 'POST'])
def update_fr():
    if 'data_nama' in session:
        id_freelancer = request.form['id_freelancer']
        username = request.form['username']
        password = request.form['password']
        nama = request.form['nama']
        tipe_akses = request.form['tipe_akses']
        data_fr = (username, password, nama, tipe_akses, id_freelancer)
        model.updateFreelancer(data_fr)
        return redirect(url_for('freelancer'))
    return render_template('form_login.html')

@application.route('/update_freelancer/<id_freelancer>')
def update_freelancer(id_freelancer):
	if 'data_nama' in session:
		data_fr = model.getFreelancerbyNo(id_freelancer)
		data_nama = session['data_nama']
		return render_template('edit_freelancer.html', data_fr=data_fr, data_nama=data_nama)
	return redirect(url_for('login')) 

@application.route('/delete_freelancer/<id_freelancer>')
def delete_freelancer(id_freelancer):
    if 'data_nama' in session:
        model.deleteFreelancer(id_freelancer)
        return redirect(url_for('freelancer'))
    return render_template('form_login.html')

# ============================ LAPORAN ===================================================
@application.route('/laporan')
def laporan():
    if 'data_nama' in session:
        container_lp = []
        container_lp = model.selectLaporan()
        data_nama = session['data_nama']
        return render_template('laporan.html', container_lp=container_lp, data_nama=data_nama)
    return render_template('form_login.html')

# tambah laporan.
@application.route('/insert_laporan', methods=['GET', 'POST'])
def insert_laporan():
    if 'data_nama' in session:
        if request.method == 'POST':
            no = request.form['no']
            username = request.form['username']
            text_laporan = request.form['text_laporan']
            tanggal_lapor = request.form['tanggal_lapor']
            status = '-'
            data_lp = (no, username, text_laporan, tanggal_lapor, status)
            model.insertLaporan(data_lp)
            return redirect(url_for('laporan'))
        else:
            data_nama = session['data_nama']
            return render_template('insert_laporan.html', data_nama=data_nama)
    return render_template('form_login.html')

# proses edit / update data laporan.
@application.route('/update_lp', methods=['GET', 'POST'])
def update_lp():
    if 'data_nama' in session:
        no = request.form['no']
        username = request.form['username']
        text_laporan = request.form['text_laporan']
        tanggal_lapor = request.form['tanggal_lapor']
        status = ""
        data_lp = (username, text_laporan, tanggal_lapor, status, no)
        model.updateLaporan(data_lp)
        return redirect(url_for('laporan'))
    return render_template('form_login.html')

# edit / update data laporan.
@application.route('/update_laporan/<no>')
def update_laporan(no):
    if 'data_nama' in session:
        data_lp = model.getLaporbyNo(no)
        data_nama = session['data_nama']
        return render_template('edit_laporan.html', data_lp=data_lp, data_nama=data_nama)
    return render_template('form_login.html')

@application.route('/delete_laporan/<no>')
def delete_laporan(no):
    if 'data_nama' in session:
        model.deleteLaporan(no)
        return redirect(url_for('laporan'))
    return render_template('form_login.html')

if __name__ == '__main__':
    application.run(debug=True)