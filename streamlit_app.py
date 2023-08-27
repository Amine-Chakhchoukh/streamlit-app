import streamlit as st

# ################################################################
st.set_page_config(page_title="IAG.ai Risk Assessment - Demo", 
                   page_icon='🎉')

htp5= 'https://photos.app.goo.gl/Wq9LJx1FNaNAWv9J6'
st.image(htp5, caption= '80-day sale data', width=300)

st.image(image, width=400)

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
        
