import streamlit as st
PAGE_CONFIG = {"page_title":"StColab.io","page_icon":":smiley:","layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)


def main():
	st.title("The highest F1 score is: ")
	st.subheader("0.938 of KNN classification")


	menu = ["Home","About"]
	choice = st.sidebar.selectbox('Menu',menu)
	if choice == 'Home':
		st.subheader("ML Major Project by Suryaansh Jaiswal")	



if __name__ == '__main__':
	main()
