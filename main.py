import streamlit as st
from c3po import *
from estruturas import *

st.set_page_config(page_icon="./MiguelSarraf.png", page_title="Miguel Sarraf") 

try:
	lgg
except:
	lgg="pt"

__current_work__="na Stefanini Scala"
__current_segment__="no time de Analytics"
__current_position__="programador sênior"

bandeiras= {"pt": "🇧🇷",
			"en": "🇬🇧"}
			# "tl": "🖖"}

def format_lgg(label):
	global bandeiras
	return bandeiras[label]

def ad_conteudo(col, tipo, caminho=None, nome=None, imagem=None, titulo=None, texto=None):
	if tipo=="pdf":
		arquivo=texto.replace(" ", "_")+".pdf"
		col.download_button(texto, data=open(caminho, "rb"), file_name=arquivo, help=message[nome][lgg])
	elif tipo=="link":
		col.write(html_clickable_image.format(caminho, imagem, titulo), unsafe_allow_html=True)
		if nome:
			col.write(html_centered_text.format(message[nome][lgg]), unsafe_allow_html=True)
	elif tipo=="imagem":
		col.image(caminho)
		col.write(html_centered_text.format(message[nome][lgg]), unsafe_allow_html=True)

if "page" not in st.session_state:
	st.session_state.page="inicio"

if st.session_state.page=="inicio":

	cols=st.columns([8,1])
	with cols[1]:
		lgg=st.selectbox("", ("pt", "en"), format_func=format_lgg, index=0)

	cols=st.columns(2)
	cols[0].image("ano_novo.png")
	cols[1].write(message["oi"][lgg])
	cols[1].write(message["filme"][lgg])
	cols[1].write(message["livro"][lgg])
	cols[1].write(message["personagem"][lgg])
	cols[1].write(message["musica"][lgg])
	cols[1].write(message["compositor"][lgg])
	cols[1].write(message["banda"][lgg])
	st.write(message["citacao"][lgg])
	st.write(message["animal"][lgg])
	st.write(message["hp"][lgg])
	st.write(message["trabalho"][lgg])

	st.download_button(message["curriculo"][lgg], data=open("./CV_pt.pdf", "rb"), file_name="CV_Miguel_Sarraf.pdf")

	abas=[st.sidebar.button(message["links"][lgg]),
		  st.sidebar.button(message["trabs"][lgg]),
		  st.sidebar.button(message["certs"][lgg])]

	if any(abas):
		if abas[0]:
			st.session_state.page="links"
		elif abas[1]:
			st.session_state.page="trabs"
		elif abas[2]:
			st.session_state.page="certs"
		else:
			raise ValueError("Something weird happened. Reload page.")
		st.experimental_rerun()

if st.session_state.page=="links":

	cols=st.columns([8,1])
	with cols[1]:
		lgg=st.selectbox("", ("pt", "en"), format_func=format_lgg, index=0)

	for secao in fontes:

		st.header(message[secao][lgg])
		links=fontes[secao]
		col=0
		cols=st.columns(5)

		for link in links:
			tipo, link, imagem, nome, titulo=link
			ad_conteudo(cols[col], tipo, caminho=link, imagem=imagem, titulo=titulo, nome=nome)
			if col==4:
				col=0
				cols=st.columns(3)
			else:
				col+=1

	abas=[st.sidebar.button(message["inicio"][lgg]),
		  st.sidebar.button(message["trabs"][lgg]),
		  st.sidebar.button(message["certs"][lgg])]

	if any(abas):
		if abas[0]:
			st.session_state.page="inicio"
		elif abas[1]:
			st.session_state.page="trabs"
		elif abas[2]:
			st.session_state.page="certs"
		else:
			raise ValueError("Something weird happened. Reload page.")
		st.experimental_rerun()

if st.session_state.page=="trabs":

	cols=st.columns([8,1])
	with cols[1]:
		lgg=st.selectbox("", ("pt", "en"), format_func=format_lgg, index=0)

	for secao in trabalhos:

		st.header(message[secao][lgg] if secao in message else secao)
		trabs=trabalhos[secao]
		col=0
		cols=st.columns(3)

		for trab in trabs:
			try:
				tipo, link, imagem, titulo, nome=trab
				ad_conteudo(cols[col], tipo, caminho=link, imagem=imagem, titulo=titulo, nome=nome)
			except:
				tipo, caminho, nome, texto=trab
				ad_conteudo(cols[col], tipo, caminho=caminho, nome=nome, texto=texto)

			if col==2:
				col=0
				cols=st.columns(3)
			else:
				col+=1

	abas=[st.sidebar.button(message["links"][lgg]),
		  st.sidebar.button(message["inicio"][lgg]),
		  st.sidebar.button(message["certs"][lgg])]

	if any(abas):
		if abas[0]:
			st.session_state.page="links"
		elif abas[1]:
			st.session_state.page="inicio"
		elif abas[2]:
			st.session_state.page="certs"
		else:
			raise ValueError("Something weird happened. Reload page.")
		st.experimental_rerun()

if st.session_state.page=="certs":

	cols=st.columns([8,1])
	with cols[1]:
		lgg=st.selectbox("", ("pt", "en"), format_func=format_lgg, index=0)

	for secao in certificados:

		st.header(message[secao][lgg])
		certs=certificados[secao]
		col=0
		cols=st.columns(3)

		for cert in certs:
			tipo, caminho, nome=cert
			ad_conteudo(cols[col], tipo, caminho=caminho, nome=nome)

			if col==2:
				col=0
				cols=st.columns(3)
			else:
				col+=1

	abas=[st.sidebar.button(message["links"][lgg]),
		  st.sidebar.button(message["trabs"][lgg]),
		  st.sidebar.button(message["inicio"][lgg])]

	if any(abas):
		if abas[0]:
			st.session_state.page="links"
		elif abas[1]:
			st.session_state.page="trabs"
		elif abas[2]:
			st.session_state.page="inicio"
		else:
			raise ValueError("Something weird happened. Reload page.")
		st.experimental_rerun()