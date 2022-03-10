import pymysql
import config2

db = cursor = None

class MModel:
	def __init__ (self, no=None, nama=None, no_telp=None):
		self.no = no
		self.nama = nama
		self.no_telp = no_telp
		
	def openDB(self):
		global db, cursor
		db = pymysql.connect(
			host=config2.DB_HOST,
			user=config2.DB_USER,
			password=config2.DB_PASSWORD,
			database=config2.DB_NAME)
		cursor = db.cursor()

	def closeDB(self):
		global db, cursor
		db.close()

	# validasi login .
	def authenticate(self, username=None, password=None):
		self.openDB()
		cursor.execute("SELECT COUNT(*) FROM data_freelancer WHERE username = '%s' AND password = '%s'" % (username, password))
		count_account = (cursor.fetchone())[0]
		self.closeDB()
		return True if count_account>0 else False

# ========================= DATA PERTANYAAN ================================
	# Pertanyaan
	def selectPertanyaan(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` ORDER BY tanggal_jawab DESC")
		container_pertanyaan = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_pertanyaan.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_pertanyaan

	def insertPertanyaan(self, data_p):
		self.openDB()
		cursor.execute("INSERT INTO data_pertanyaan (no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan) VALUES ('%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s')" % data_p)
		db.commit()
		self.closeDB()
	
	def updatePertanyaan(self, data_pr):
		self.openDB()
		cursor.execute("UPDATE data_pertanyaan SET username='%s', kategori='%s', pertanyaan='%s', penjawab='%s', jawaban='%s', tanggal_jawab='%s', ranking='%s', keterangan='%s' WHERE no='%s'" % data_pr)
		db.commit()
		self.closeDB()

	def getPertanyaanbyNo(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no=%s" % no)
		data_pr = cursor.fetchone()
		return data_pr
		
	# KOREKSI
	def koreksiPertanyaan(self, data_pr):
		self.openDB()
		cursor.execute("UPDATE data_pertanyaan SET username='%s', kategori='%s', pertanyaan='%s', penjawab='%s', jawaban='%s', tanggal_jawab='%s', ranking='%s', keterangan='%s' WHERE no='%s'" % data_pr)
		db.commit()
		self.closeDB()

	def deletePertanyaan(self, no):
		self.openDB()
		cursor.execute("DELETE FROM data_pertanyaan WHERE no='%s'" % no)
		db.commit()
		self.closeDB()
		
	# REKAP
	def selectRekap(self):
		self.openDB()
		cursor.execute("SELECT no, penjawab, ranking, jawaban FROM `data_pertanyaan` WHERE ranking='Jawaban Terverifikasi' ORDER BY penjawab ASC")
		container_rekap = []
		for no, penjawab, ranking, jawaban in cursor.fetchall():
			container_rekap.append((no, penjawab, ranking, jawaban))
		self.closeDB()
		return container_rekap
	
	def getRekapForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, penjawab, ranking FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama

# ========================= KATEGORI ================================
	# SEMUA
	def selectSemua(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` ORDER BY tanggal_jawab DESC")
		container_semua = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_semua.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_semua

	def getSemuaForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama

	# MAKANAN
	def selectMakanan(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` WHERE kategori='makanan' ORDER BY tanggal_jawab DESC")
		container_makanan = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_makanan.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_makanan

	def getMakananForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama

	# MINUMAN
	def selectMinuman(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` WHERE kategori='minuman' ORDER BY tanggal_jawab DESC")
		container_minuman = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_minuman.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_minuman

	def getMinumanForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama

	# PAKAIAN
	def selectPakaian(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` WHERE kategori='pakaian' ORDER BY tanggal_jawab DESC")
		container_pakaian = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_pakaian.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_pakaian

	def getPakaianForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama

	# DESAIN
	def selectDesain(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` WHERE kategori='desain' ORDER BY tanggal_jawab DESC")
		container_desain = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_desain.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_desain

	def getDesainForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama

	# MANUFAKTUR
	def selectManufaktur(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` WHERE kategori='manufaktur' ORDER BY tanggal_jawab DESC")
		container_manufaktur = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_manufaktur.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_manufaktur

	def getManufakturForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama

	# TEKNOLOGI
	def selectTeknologi(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` WHERE kategori='teknologi' ORDER BY tanggal_jawab DESC")
		container_teknologi = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_teknologi.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_teknologi

	def getTeknologiForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama

	# PARIWISATA
	def selectPariwisata(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` WHERE kategori='pariwisata' ORDER BY tanggal_jawab DESC")
		container_pariwisata = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_pariwisata.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_pariwisata

	def getPariwisataForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama

	# TRANSPORT
	def selectTransport(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` WHERE kategori='transport' ORDER BY tanggal_jawab DESC")
		container_transport = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_transport.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_transport

	def getTransportForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama

	# ONLINE SHOP
	def selectOnlineShop(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` WHERE kategori='online shop' ORDER BY tanggal_jawab DESC")
		container_onlineshop = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_onlineshop.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_onlineshop

	def getOnlineShopForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama

	# PERIKLANAN
	def selectPeriklanan(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` WHERE kategori='periklanan' ORDER BY tanggal_jawab DESC")
		container_periklanan = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_periklanan.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_periklanan

	def getPeriklananForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama
	
	# ARTIKEL SEO
	def selectArtikelSeo(self):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM `data_pertanyaan` WHERE kategori='artikel seo' ORDER BY tanggal_jawab DESC")
		container_artikel_seo = []
		for no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan in cursor.fetchall():
			container_artikel_seo.append((no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan))
		self.closeDB()
		return container_artikel_seo

	def getArtikelSeoForSession(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan FROM data_pertanyaan WHERE no='%s'" % no)
		data_nama = cursor.fetchone()
		return data_nama
	

	# ==============================  SIGN UP ========================
	def selectSignUp(self):
		self.openDB()
		cursor.execute("SELECT id_freelancer, username, password, nama, tipe_akses FROM `data_freelancer` ORDER BY id_freelancer ASC")
		container_signup = []
		for id_freelancer, username, password, nama, tipe_akses in cursor.fetchall():
			container_signup.append((id_freelancer, username, password, nama, tipe_akses))
		self.closeDB()
		return container_signup

	def insertSignUp(self, data_signup):
		self.openDB()
		cursor.execute("INSERT INTO data_freelancer (id_freelancer, username, password, nama, tipe_akses) VALUES('%s', '%s', '%s', '%s', '%s')" % data_signup)
		db.commit()
		self.closeDB()


# ========================= DATA FREELANCER ================================
	def selectFreelancer(self):
		self.openDB()
		cursor.execute("SELECT id_freelancer, username, password, nama, tipe_akses FROM `data_freelancer` ORDER BY id_freelancer ASC")
		container_freelancer = []
		for id_freelancer, username, password, nama, tipe_akses in cursor.fetchall():
			container_freelancer.append((id_freelancer, username, password, nama, tipe_akses))
		self.closeDB()
		return container_freelancer

	# Untuk Hak Akses
	def getUserForSession(self, username):
		self.openDB()
		cursor.execute("SELECT username, nama, tipe_akses FROM data_freelancer WHERE username='%s'" % username)
		data_nama = cursor.fetchone()
		return data_nama

	def insertFreelancer(self, data_f):
		self.openDB()
		cursor.execute("INSERT INTO data_freelancer (id_freelancer, username, password, nama, tipe_akses) VALUES('%s', '%s', '%s', '%s', '%s')" % data_f)
		db.commit()
		self.closeDB()

	def updateFreelancer(self, data_fr):
		self.openDB()
		cursor.execute("UPDATE data_freelancer SET username='%s', password='%s', nama='%s', tipe_akses='%s' WHERE id_freelancer='%s'" % data_fr)
		db.commit()
		self.closeDB()

	def getFreelancerbyNo(self, id_freelancer):
		self.openDB()
		cursor.execute("SELECT id_freelancer, username, password, nama, tipe_akses FROM data_freelancer WHERE id_freelancer='%s'" % id_freelancer)
		data_fr = cursor.fetchone()
		return data_fr

	def deleteFreelancer(self, id_freelancer):
		self.openDB()
		cursor.execute("DELETE FROM data_freelancer WHERE id_freelancer='%s'" % id_freelancer)
		db.commit()
		self.closeDB()

# ========================================= LAPORAN ============================================
	# menampilkan laporan.
	def selectLaporan(self):
		self.openDB()
		cursor.execute("SELECT no, username, text_laporan, tanggal_lapor, status FROM data_lapor2 ORDER BY tanggal_lapor DESC")
		container_lp = []
		for no, username, text_laporan, tanggal_lapor, status in cursor.fetchall():
			container_lp.append((no, username, text_laporan, tanggal_lapor, status))
		self.closeDB()
		return container_lp

	# tambah data laporan.
	def insertLaporan(self, data_lp):
		self.openDB()
		cursor.execute("INSERT INTO data_lapor2 (no, username, text_laporan, tanggal_lapor, status) VALUES ('%s', '%s', '%s', '%s', '%s')" % data_lp)
		db.commit()
		self.closeDB()

	# edit / update data laporan.
	def updateLaporan(self, data_lp):
		self.openDB()
		cursor.execute("UPDATE data_lapor2 SET username='%s', text_laporan='%s', tanggal_lapor='%s', status='%s' WHERE no=%s" % data_lp)
		db.commit()
		self.closeDB()

	def getLaporbyNo(self, no):
		self.openDB()
		cursor.execute("SELECT no, username, text_laporan, tanggal_lapor, status FROM data_lapor2 WHERE no=%s" % no)
		data_lp = cursor.fetchone()
		return data_lp

	def deleteLaporan(self, no):
		self.openDB()
		cursor.execute("DELETE FROM data_lapor2 WHERE no='%s'" % no)
		db.commit()
		self.closeDB()



