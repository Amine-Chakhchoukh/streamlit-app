import streamlit as st

# ################################################################
st.set_page_config(page_title="IAG.ai Risk Assessment - Demo", 
                   page_icon='🎉')

htp5= href="https://drive.google.com/uc?export=view&id=1VllN4T1vaTS6VTBSeY_Nf5HMTfs7qwJG"><img src="https://drive.google.com/uc?export=view&id=1VllN4T1vaTS6VTBSeY_Nf5HMTfs7qwJG" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture"
st.image(htp5, width=300)

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
        
