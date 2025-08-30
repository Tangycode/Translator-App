import streamlit as st
from deep_translator import GoogleTranslator as gt
st.title("Translator💎💎💎💎")
st.subheader("A translator app")
st.divider()
translator = gt()
lan = translator.get_supported_languages()
text = st.text_area("Enter any text: ",height=150)
c1,c2 = st.columns(2)
with c1:
    src = st.selectbox("Source language: ",options=lan)
with c2:
    trgt = st.selectbox("Target Language: ", options=lan)
if st.button("translate"):
    t = gt(source=src, target=trgt)
    result = t.translate(text)
    st.success(f'Translated text {result}')
