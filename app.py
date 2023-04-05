from audio_recorder_streamlit import audio_recorder
import streamlit as st 
import librosa
import os 
import io

def main():
    menu = ['Diagnoser', 'About']
    choice = st.sidebar.selectbox("Menu", menu)
    st.sidebar.header('Cookie Theft Helper')
    st.sidebar.write('Who are in the picture')
    st.sidebar.write('what are they doing')
    
    if choice == 'Diagnoser':
        if 'audio' not in st.session_state:
            st.session_state['audio'] = None
        if 'sr' not in st.session_state:
            st.session_state['sr'] = None
        if 'name' not in st.session_state:
            st.session_state['name'] = None
        if 'age' not in st.session_state:
            st.session_state['age'] = None
        if 'gender' not in st.session_state:
            st.session_state['gender'] = None
            
        img_path = os.path.join('assets', 'cookie_thieft.png')
        st.image(img_path, 'Cookie Theft stimulus photo')
        audio_bytes = audio_recorder()
        if audio_bytes:
            st.audio(audio_bytes, format="audio/wav")
            with io.BytesIO(audio_bytes) as f:
                audio, sr = librosa.load(f)
                st.session_state['audio'] = audio
                st.session_state['sr']  = sr
                
            name = st.text_input('Name')
            age  = st.number_input('Age')
            gender = st.radio('Gender', ['Male', 'Female'])
            st.session_state['name'] = name
            st.session_state['age'] = age
            st.session_state['gender'] = gender
            
            btn = st.button('Diagnose')
        
    elif choice == 'About':
        st.title('Cookie Theft stimulus photo')
        st.write('''
Participants are asked to describe this picture. The Cookie Theft stimulus photo is a widely used visual stimulus in neuropsychological assessments, particularly in the evaluation of language and communication abilities in individuals with brain damage. The photo depicts a scene of a kitchen where a young girl is standing on a chair by the counter, reaching for cookies that are on a plate. The kitchen sink is overflowing with water and dishes, and there is a window in the background. Meanwhile, her younger brother is standing on a chair on the other side of the counter, trying to reach a jar of cookies that is also on the counter. There are scattered crumbs on the counter, and a broken teacup and saucer on the floor. The photo was originally taken by Arnold Gesell and Catherine Amatruda in the 1930s as part of their research on child development. It was later popularized by Elizabeth K. Warrington and Lawrence Weiskrantz in the 1970s as a tool to assess language and communication abilities in individuals with brain damage, particularly those with aphasia. The photo is often used as a basis for storytelling or description tasks, where the individual is asked to describe the scene or narrate a story based on the information presented in the photo. The tasks are designed to assess various aspects of language and communication abilities, such as narrative coherence, lexical and grammatical abilities, and pragmatic skills.
                 ''')
        
if __name__ == '__main__':
    main()