from mechanize import Browser
from bs4 import BeautifulSoup
import argparse

class linkdln:
	def __init__(self):
		self.br=Browser()
		self.br.set_handle_robots(False)

	def login(self, username, password):
		self.br.open("https://www.linkedin.com/login")
		self.br._factory.is_html=True
		self.br.select_form(nr=0)
		self.br.form["session_key"]=username
		self.br.form["session_password"]=password
		self.br.method="POST"
		soup=BeautifulSoup(self.br.submit().read(), features="html5lib")
		find=soup.find("code", attrs={"id":"i18nErrorGoogleOneTapGeneralErrorMessage"})
		if find==None:
			print("Halo, Selamat datang di linkdln")
		else:
			print("Login failed")


main=linkdln()
main.login("","") #username dan password disini
