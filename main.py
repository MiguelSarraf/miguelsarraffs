import streamlit as st
from c3po import *

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

def format_lgg(label):
	global bandeiras
	return bandeiras[label]

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

	abas=[st.sidebar.button("Perfis"),
		  st.sidebar.button("Trabalhos"),
		  st.sidebar.button("Certificados")]

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

	st.header("Perfis")
	st.subheader("Desenvolvimento")
	desenvolvimento=st.columns(5)
	desenvolvimento[0].markdown('''
	<a href="https://github.com/MiguelSarraf" style="text-align: center" target="_blank">
    	<img src="data:image/png;base64,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" width=125px height=125px title="GitHub"/>
	</a>''',
    unsafe_allow_html=True
	)
	desenvolvimento[0].write(f"<p style='text-align: center'> {message['pessoal'][lgg]} </p>", unsafe_allow_html=True)
	desenvolvimento[1].markdown('''
	<a href="https://github.com/orgs/PCS-Poli-USP/teams/mvn" target="_blank">
    	<img src="data:image/png;base64,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" width=125px height=125px title="GitHub"/>
	</a>''',
    unsafe_allow_html=True
	)
	desenvolvimento[1].write(f"<p style='text-align: center'> {message['poli'][lgg]} </p>", unsafe_allow_html=True)


	st.subheader("Formação acadêmica, certificados e insígnias")
	cursos=st.columns(5)
	cursos[0].markdown('''
	<a href="http://lattes.cnpq.br/2053096155107400" target="_blank">
    	<img src="http://exercicioepostura.com.br/wp-content/uploads/2015/03/lattes-logo-teste-249x300.png" width=104px height=125px title="Lattes"/>
	</a>''',
    unsafe_allow_html=True
	)
	cursos[1].markdown('''
	<a href="https://www.coursera.org/user/4273951c189eb6ace564428544db3e77" target="_blank">
    	<img src="https://www.langoly.com/wp-content/uploads/2021/09/coursera-logo-1024x1024.png" width=125px height=125px title="Coursera"/>
	</a>''',
    unsafe_allow_html=True
	)
	cursos[2].markdown('''
	<a href="https://www.credly.com/users/miguel-sarraf-ferreira-santucci" target="_blank">
    	<img src="https://images.credly.com/images/b685de69-03cf-402c-b8e3-62ecd0e2e949/blob.png" width=125px height=125px title="Credly"/>
	</a>''',
    unsafe_allow_html=True
	)


	st.subheader("Contato")
	contato=st.columns(5)
	contato[0].markdown('''
	<a href="linkedin.com/in/miguel-sarraf-ferreira-santucci-6163b251" target="_blank">
    	<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAdVBMVEUqZrz////+/v4AV7f6/P4fYbomZLtMfMVCd8SDotVZgsd/n9Qwab1+m9EiYruMptXx9PoRXLjM2O29zeiww+Ps8fkKWrhii8sAU7a7zOi0xuSWsNovbcDa4/F0l9DS3e86ccGnvN9skM3k6/Wcs9zQ2+5dhcjAG3elAAAFi0lEQVR4nO3db3uaPBQGcKLmWFcGhH9WRae1D9//Iz5g28tZE0zospzDzv1iL7Z047cECEkIkZh6otAH4D0spB8W0g8L6YeF9MNC+mEh/bCQflhIPyykHxZ+yQJD/AizIl03ao4jqlmnm+xPCrPtWtUyidAEEqlUW1ohLYTZLlYJhEbdBRIV7yyMj4UlqNAYYyScvi2s2hpf9V0DdVt9T5jHMjTiQWScf0dYKMwV+B5Qm/HC4gU/sCO+FGOFOYEa7ANqqKEOCKuYBrAjxgOXmwFhi/0ic41sxwjLOvRxO6Qu3YUZUGmjfQCMvRujcIe3J6OL2rkKszj0MTsmNlWiSVjSqsKuEreOwjWiZyWrJGs3YUbkZn8NKEMzNQgLao20u2EY+m4GYUrnbv8ZmToJyZ2G5hPRIGxCH697oHES0jsNu/uFk3Ae+nBHZO4iXJAU6oeKWUgoLGQh/rCQhfjDQhbij19hAuGHV/0JQdbNsv1xVIHHdrwJVZTus4WYZefTU1CjJyHU6eUvnl1+bgsBRz/8CJN+jnn2GSGyZbghLE91uL/6LsbFMlgtehHW+S2wI4abV/UhlD+/AjviJtQolgchqEojFMtAlehBKA/3wI4YatrKg1BttcJzoMupD+FZJ5yJQJOrf17Yr/HQCn+EORE91GGT6YWBpnX+Zh1ORRjVhvMwmkwrVaX+Wjqdu0XyqhWepiPUNlOxeJpOnyaSmkoMVoWeni3uejXiHGzAxosQ5JfHJ5E1wQYyPD0B94utrj6xb8INY3gbp/l57n+i54nsLeSLNd7G2iQcih5Z5WkzxbG2qD8ZlQS4/Ort6G3id8wbJj3mjSUsZCH+sJCF+MPCUULQxbnMpUP0GTm66+BFGOviVqbDQdMeduV2U2y2p91hGalxr477mJl50v7wzTp/WGrLrD7KgDqu8i8vDy72p9dYuT+k+BHqRqJWt8KFppB4vpSBeln0h/XlD7tUm7Z2NSIUymR7x7sq9+3cra3iE6rXhcH3gcyPTrNY6IQqHfJdSi1WLo/U2IT9K5HDwL4aSwciMmF9eAzsCxb2m1YgE4Lut7VE61rEJTxs7IBd0TfbMXRcwp1lFfbnou10JC6hfm5VTzxbbgyASjizB/ZN2u62iEvoErG3q0S6wpmwWw1IWfhm1UzRCt//xcES/1k1U5zC/t/a5/mvbLAPXlk9EWMUdqxtC5exi3VuNlouDUAoFLNTVL9XDyTz1niPFDOrdWT4hKJqf++QyfiXsWRLUiiq5vYSmcDeVJSkUGR3U/5JbCpLsZVqN9pSmnXjdIXatdKmNbkEhUJoh7blajpC/XJ3OGoX5ZIUGl5ZUNrLKUGhqAzzL4YlqwSFuWHwRaZTEZqGl+TzVISmfah0b1LRFD6zkIUsZCELWchCFrKQhSxkIQtZyEIWspCFLGQhC1nIQhaykIUsZCELWchCFjoLdXF5D/hO+KwtHmx9aZPqcrOgC46Py9z8h+x0xY+BhBFIXcC5zPjivoW4wkIW4g8LWYg/LGQh/rCQhfjjJJz+t2T/ge8BT/+bztP/Lvf0v61eWO6Ygih14STMAn8Hzz2gMichvRPRdBoahaE+2jQ6/fb3TsIs0CeNRic2NFKjUOxoVWK/wZ2jMAu/ybpDAExVaBaKktINoy6NDrNQt60D1sjWzBgQhvtWo2ugqcyMAaHIidz2QeUDiiGhKF4oEOHF0F+zEDpsPBkuoAaBD4Qij7FfbmQ81EQfC0XV2m+RGiBQtwMXGSthd18EvL0bBaeHx/9YKLK3eNwm6X4DiYp3xp6Mk7AzbteqloiUkEil1qWFz1LYI4t03ag5jqhmnW6seA7CjywwxO2QHYUEw0L6YSH9sJB+WEg/LKQfFtIPC+mHhfTDQvphIf38Dy3IvxZLImNDAAAAAElFTkSuQmCC" width=125px height=125px title="LinkedIn"/>
	</a>''',
    unsafe_allow_html=True
	)
	contato[1].markdown('''
	<a href="mailto: miguel.sarraf@hotmail.com">
    	<img src="https://seeklogo.com/images/O/outlook-logo-7117D18788-seeklogo.com.png" width=125px height=125px title="e-mail"/>
	</a>''',
    unsafe_allow_html=True
	)
	contato[1].write(f"<p style='text-align: center'> {message['pessoal'][lgg]} </p>", unsafe_allow_html=True)
	contato[2].markdown('''
	<a href="mailto: mssantucci@stefanini.com">
    	<img src="https://seeklogo.com/images/O/outlook-logo-7117D18788-seeklogo.com.png" width=125px height=125px title="e-mail"/>
	</a>''',
    unsafe_allow_html=True
	)
	contato[2].write(f"<p style='text-align: center'> {message['corporativo'][lgg]} </p>", unsafe_allow_html=True)
	contato[3].markdown('''
	<a href="mailto: miguel.sarra@usp.br">
    	<img src="https://logodownload.org/wp-content/uploads/2018/03/gmail-logo-2-1.png" width=125px height=94px style="margin:16px 15px;" title="e-mail"/>
	</a>''',
    unsafe_allow_html=True
	)
	contato[3].write(f"<p style='text-align: center; margin:0px 0px 0px 25px'> {message['academico'][lgg]} </p>", unsafe_allow_html=True)


	st.subheader("Miscelânea")
	misc=st.columns(5)
	misc[0].markdown('''
	<a href="https://www.16personalities.com/profiles/15d00765b9bd2" target="_blank">
    	<img src="https://static.neris-assets.com/images/AMP/logo_simple.png" width=125px height=125px title="MBTI (Myer-Briggs Type Indicator)"/>
	</a>''',
    unsafe_allow_html=True
	)
	misc[1].markdown('''
	<a href="https://www.duolingo.com/profile/Miguel689806?via=share_profile" target="_blank">
    	<img src="https://requisitos-duolingo.github.io/duolingo/images/logo.png" width=125px height=114px title="Duolingo" style="margin:6px 5px;"/>
	</a>''',
    unsafe_allow_html=True
	)

	abas=[st.sidebar.button("Início"),
		  st.sidebar.button("Trabalhos"),
		  st.sidebar.button("Certificados")]

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

	st.header("2021")

	cols=st.columns(3)
	cols[0].download_button("Uma Proposta para Aprendizado Computacional Inspirada no Aprendizado e Desenvolvimento Humano", data=open("./trabalhos/TCC_Miguel_RR.pdf", "rb"), file_name="uma_proposta_para_aprendizado_computacional_inspirada_no_aprendizado_e_desenvolvimento_humano.pdf", help=message['tcc'][lgg])

	abas=[st.sidebar.button("Perfis"),
		  st.sidebar.button("Início"),
		  st.sidebar.button("Certificados")]

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

	st.header("Computação")

	cols=st.columns(3)
	cols[0].image("./certificados/TCC_mencao_honrosa_corrigido.png")
	cols[0].write(f"<p style='text-align: center'> {message['mencao'][lgg]} </p>", unsafe_allow_html=True)
	cols[1].image("./certificados/AZ-900_certificate.png")
	cols[1].write(f"<p style='text-align: center'> {message['az900'][lgg]} </p>", unsafe_allow_html=True)
	cols[2].image("./certificados/fundamentals_of_data_visualization.png")
	cols[2].write(f"<p style='text-align: center'> {message['datavis'][lgg]} </p>", unsafe_allow_html=True)

	cols=st.columns(3)
	cols[0].image("./certificados/data_science_math_skills.png")
	cols[0].write(f"<p style='text-align: center'> {message['matdata'][lgg]} </p>", unsafe_allow_html=True)

	st.header("Escrita")

	cols=st.columns(3)
	cols[0].image("./certificados/craft_of_a_plot.png")
	cols[0].write(f"<p style='text-align: center'> {message['plot'][lgg]} </p>", unsafe_allow_html=True)
	cols[1].image("./certificados/craft_of_a_character.png")
	cols[1].write(f"<p style='text-align: center'> {message['character'][lgg]} </p>", unsafe_allow_html=True)

	st.header("Miscelânea")

	cols=st.columns(3)
	cols[0].image("./certificados/Cenopoesia.png")
	cols[0].write(f"<p style='text-align: center'> {message['cenopoesia'][lgg]} </p>", unsafe_allow_html=True)
	cols[1].image("./certificados/murilo_mendes.png")
	cols[1].write(f"<p style='text-align: center'> {message['murilomendes'][lgg]} </p>", unsafe_allow_html=True)
	cols[2].image("./certificados/Semana_de_arte_moderna_2021.png")
	cols[2].write(f"<p style='text-align: center'> {message['semanaartemoderna'][lgg]} </p>", unsafe_allow_html=True)

	abas=[st.sidebar.button("Perfis"),
		  st.sidebar.button("Trabalhos"),
		  st.sidebar.button("Início")]

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