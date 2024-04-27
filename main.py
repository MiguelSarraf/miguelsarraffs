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
__current_position__="analista de dados pleno"

bandeiras= {"pt": "🇧🇷",
			"en": "🇬🇧"}
			# "tl": "🖖"}

def format_lgg(label):
	global bandeiras
	return bandeiras[label]

def ad_conteudo(col, tipo, args):
	if tipo=="pdf":
		caminho, nome, texto=args
		arquivo=texto.replace(" ", "_")+".pdf"
		col.download_button(texto, data=open(caminho, "rb"), file_name=arquivo, help=message[nome][lgg])
	elif tipo=="link":
		caminho, imagem, titulo, nome=args
		col.write(html_clickable_image.format(caminho, imagem, titulo), unsafe_allow_html=True)
		if nome:
			col.write(html_centered_text.format(message[nome][lgg]), unsafe_allow_html=True)
	elif tipo=="imagem":
		caminho, nome=args
		col.image(caminho)
		col.write(html_centered_text.format(message[nome][lgg]), unsafe_allow_html=True)

if "page" not in st.session_state:
	st.session_state.page="inicio"

if st.session_state.page=="inicio":

	cols=st.columns([8,1])
	with cols[1]:
		lgg=st.selectbox("language", ("pt", "en"), format_func=format_lgg, index=0, label_visibility="collapsed")

	cols=st.columns(2)
	cols[0].image("perfil_jedi.jpeg")
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

	st.download_button(message["curriculo"][lgg], data=open("./"+message["curriculo_path"][lgg], "rb"), file_name=message["curriculo_path"][lgg])

	abas=[st.sidebar.button(message["inicio"][lgg]),
		  st.sidebar.button(message["links"][lgg]),
		  st.sidebar.button(message["trabs"][lgg]),
		  st.sidebar.button(message["certs"][lgg])]

	if any(abas):
		if abas[0]:
			pass
		elif abas[1]:
			st.session_state.page="links"
		elif abas[2]:
			st.session_state.page="trabs"
		elif abas[3]:
			st.session_state.page="certs"
		else:
			raise ValueError("Something weird happened. Reload page.")
		st.rerun()

if st.session_state.page=="links":

	cols=st.columns([8,1])
	with cols[1]:
		lgg=st.selectbox("language", ("pt", "en"), format_func=format_lgg, index=0, label_visibility="collapsed")

	for secao in fontes:

		st.header(message[secao][lgg])
		links=fontes[secao]
		col=0
		cols=st.columns(5)

		for link in links:
			tipo, args=link
			ad_conteudo(cols[col], tipo, args)
			if col==4:
				col=0
				cols=st.columns(3)
			else:
				col+=1

	abas=[st.sidebar.button(message["inicio"][lgg]),
		  st.sidebar.button(message["links"][lgg]),
		  st.sidebar.button(message["trabs"][lgg]),
		  st.sidebar.button(message["certs"][lgg])]

	if any(abas):
		if abas[0]:
			st.session_state.page="inicio"
		elif abas[1]:
			pass
		elif abas[2]:
			st.session_state.page="trabs"
		elif abas[3]:
			st.session_state.page="certs"
		else:
			raise ValueError("Something weird happened. Reload page.")
		st.rerun()

if st.session_state.page=="trabs":

	cols=st.columns([8,1])
	with cols[1]:
		lgg=st.selectbox("language", ("pt", "en"), format_func=format_lgg, index=0, label_visibility="collapsed")

	for secao in trabalhos:

		st.header(message[secao][lgg] if secao in message else secao)
		trabs=trabalhos[secao]
		col=0
		cols=st.columns(3)

		for trab in trabs:
			tipo, args=trab
			ad_conteudo(cols[col], tipo, args)

			if col==2:
				col=0
				cols=st.columns(3)
			else:
				col+=1

	abas=[st.sidebar.button(message["inicio"][lgg]),
		  st.sidebar.button(message["links"][lgg]),
		  st.sidebar.button(message["trabs"][lgg]),
		  st.sidebar.button(message["certs"][lgg])]

	if any(abas):
		if abas[0]:
			st.session_state.page="inicio"
		elif abas[1]:
			st.session_state.page="links"
		elif abas[2]:
			pass
		elif abas[3]:
			st.session_state.page="certs"
		else:
			raise ValueError("Something weird happened. Reload page.")
		st.rerun()

if st.session_state.page=="certs":

	cols=st.columns([8,1])
	with cols[1]:
		lgg=st.selectbox("language", ("pt", "en"), format_func=format_lgg, index=0, label_visibility="collapsed")

	for secao in certificados:

		st.header(message[secao][lgg])
		certs=certificados[secao]
		col=0
		cols=st.columns(3)

		for cert in certs:
			tipo, args=cert
			ad_conteudo(cols[col], tipo, args)

			if col==2:
				col=0
				cols=st.columns(3)
			else:
				col+=1

	abas=[st.sidebar.button(message["inicio"][lgg]),
		  st.sidebar.button(message["links"][lgg]),
		  st.sidebar.button(message["trabs"][lgg]),
		  st.sidebar.button(message["certs"][lgg])]

	if any(abas):
		if abas[0]:
			st.session_state.page="inicio"
		elif abas[1]:
			st.session_state.page="links"
		elif abas[2]:
			st.session_state.page="trabs"
		elif abas[3]:
			pass
		else:
			raise ValueError("Something weird happened. Reload page.")
		st.rerun()