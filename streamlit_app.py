import streamlit as st

# ################################################################
st.set_page_config(page_title="IAG.ai Risk Assessment - Demo", 
                   page_icon='🎉')

htp5="https://photos.google.com/share/AF1QipNcph17VlTonE22W43wP7Lu27dftetGqU9l9XvWfyFxo_xTyKHvGP9ibL7EjJpoAw/photo/AF1QipP6LJ7kYWEegDATC7_MswmW1cXiBM97tO6_nLvI?key=dTFuZEFpdi1ZeTFPZlloS21qdlR2SzNwcU1PRFVn"
st.image(htp5, caption="DArio & Amine", width=300)

st.title("Dario!! I did it! We have an app!")
# ################################################################

placeholder = st.empty()

def callback():
    st.session_state["input_form_clicked"] = True

if "input_form_clicked" not in st.session_state:
    st.session_state["input_form_clicked"] = False
    
if not st.session_state["input_form_clicked"]:
    with placeholder.form("input_form"):
        
        response_dropdown = ('Yay!', 'Fantastic!')
        
        a1 = st.selectbox('Can you believe it!',
                            response_dropdown)
    
        submitted = st.form_submit_button("So cool!", on_click=callback)
       
        st.write("Made with 💚 by Amine in the living room!")
        
        if st.session_state["input_form_clicked"]:
            placeholder.empty()
            
if st.session_state["input_form_clicked"]:
    # with placeholder.form("new_form"):
    st.write("Yaaaaay :D")
        
