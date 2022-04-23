import streamlit as st
from PIL import Image

def app():
    # Title of the main page
    display = Image.open('static/Culture2.jpeg')
    col1, col2 = st.columns(2)
    col1.image(display, width = 450)
    col2.title('CulturEd')
    col2.write('An educational platform built to inform the public on various cultures through food and local events')
    
    st.title('Quiz')

    placeholder = st.empty()

    with placeholder.container():
        q1 = st.radio('Pho, which contains meat, herbs, rice noodles, and broth, is a traditional dish in which Asian country?',
                        ('Malaysia', 'Thailand', 'Indonesia', 'Vietnam'), key='q1')
        
        q2 = st.radio('In Italy, mums and roses are the favored flowers to take when invited to dinner. True or False? ',
                        ('True', 'False'), key='q2')
            
        q3 = st.radio('In what country is it considered a compliment to slurp loudly while eating soup?',
                        ('Iceland', 'Russia', 'Japan', 'Colombia'), key='q3')

        q4 = st.radio("In India, you are invited to a friend's house to share a meal of rice and curry. What is the best way to eat?",
                        ('Using a spoon', 'Using your left hand only', 'Using your right hand only', 'Using both hands'), key='q4')

        q5 = st.radio('In which country would you expect to see students knock on their desks after a particularly good lecture or presentation?',
                        ('Brazil', 'Uganda', 'Thailand', 'Germany'), key='q5')

        q6 = st.radio('In France, what food is very important and eaten with most meals?',
                        ('Tea', 'Bread', 'Oatmeal', 'Cheese'), key='q6')

        q7 = st.radio('Which food is from Mexico?',
                        ('Molletes', 'Injera', 'Banga', 'Pastilla'), key='q7')
            
        q8 = st.radio('Which Filipino tradition uses bamboo sticks and fast paced music to dance to?',
                        ('Kuratsa', 'Tinikling', 'Flamenco', 'Tarantella'), key='q8')

        q9 = st.radio("Which of these is a symbol of Argentina's culture?",
                        ('Tango', 'Hip-hop', 'Salsa', 'Samba'), key='q9')

        q10 = st.radio("What dish is shown in the photo below?",
                        ('Congee', 'Lugaw', 'Harees', 'Pozole'), key='q10')

        st.image('static/dishes/UnitedArabEmirates-Harees.jpeg', width=350)

        submitted = st.button("Submit")
    
    if submitted:
        with placeholder.container():
            options = ('Malaysia', 'Thailand', 'Indonesia', 'Vietnam')
            ans1 = st.radio('Pho, which contains meat, herbs, rice noodles, and broth, is a traditional dish in which Asian country?',
                        options, index=options.index(q1), key='ans1')
            if ans1 == 'Vietnam':
                resp = '<p style="font-family:Courier; color:Blue; font-size: 14px;">Correct! Pho is a traditional Vietnamese soup often eaten at breakfast.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            else:
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. Pho is a traditional Vietnamese soup often eaten at breakfast.</p>'
                st.markdown(resp, unsafe_allow_html=True)
        
            options = ('True', 'False')
            ans2 = st.radio('In Italy, mums and roses are the favored flowers to take when invited to dinner. True or False? ',
                            options, index=options.index(q2), key='ans2')
            if ans2 == 'False':
                resp = '<p style="font-family:Courier; color:Blue; font-size: 14px;">Correct! In Italy, mums and roses are funeral flowers. Colors, numbers, and types of flowers can be a minefield in different cultures.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            else:
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. In Italy, mums and roses are funeral flowers. Colors, numbers, and types of flowers can be a minefield in different cultures.</p>'
                st.markdown(resp, unsafe_allow_html=True)

            options = ('Iceland', 'Russia', 'Japan', 'Colombia')
            ans3 = st.radio('In what country is it considered a compliment to slurp loudly while eating soup?',
                            options, index=options.index(q3), key='ans3')
            if ans3 == 'Japan':
                resp = '<p style="font-family:Courier; color:Blue; font-size: 14px;">Correct! In many Asian cultures, slurping is a sign you appreciate the food.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            else:
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. In many Asian cultures, slurping is a sign you appreciate the food.</p>'
                st.markdown(resp, unsafe_allow_html=True)

            options = ('Using a spoon', 'Using your left hand only', 'Using your right hand only', 'Using both hands')
            ans4 = st.radio("In India, you are invited to a friend's house to share a meal of rice and curry. What is the best way to eat?",
                            options, index=options.index(q4), key='ans4')
            if ans4 == 'Using your right hand only':
                resp = '<p style="font-family:Courier; color:Blue; font-size: 14px;">Correct! Using your left hand to eat is taboo in India--only the right hand may be used for eating. The left hand is considered unclean.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            else:
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. Using your left hand to eat is taboo in India--only the right hand may be used for eating. The left hand is considered unclean.</p>'
                st.markdown(resp, unsafe_allow_html=True)

            options = ('Brazil', 'Uganda', 'Thailand', 'Germany')
            ans5 = st.radio('In which country would you expect to see students knock on their desks after a particularly good lecture or presentation?',
                            options, index=options.index(q5), key='ans5')
            if ans5 == 'Germany':
                resp = '<p style="font-family:Courier; color:Blue; font-size: 14px;">Correct! In Germany and Austria, many students would knock on their desks or a table to show appreciation for a good lecture or presentation. In these cultures, this action serves as a form of applause in academic settings.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            else:
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. In Germany and Austria, many students would knock on their desks or a table to show appreciation for a good lecture or presentation. In these cultures, this action serves as a form of applause in academic settings.</p>'
                st.markdown(resp, unsafe_allow_html=True)

            options = ('Tea', 'Bread', 'Oatmeal', 'Cheese')
            ans6 = st.radio('In France, what food is very important and eaten with most meals?',
                            options, index=options.index(q6), key='ans6')
            if ans6 == 'Bread':
                resp = '<p style="font-family:Courier; color:Blue; font-size: 14px;">Correct! France is considered the cultural home of quality bread. French classics such as baguette, brioche and pain au levain (sourdough) are recognized across the world.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            else:
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. France is considered the cultural home of quality bread. French classics such as baguette, brioche and pain au levain (sourdough) are recognized across the world.</p>'
                st.markdown(resp, unsafe_allow_html=True)

            options = ('Molletes', 'Injera', 'Banga', 'Pastilla')
            ans7 = st.radio('Which food is from Mexico?',
                            options, index=options.index(q7), key='ans7')
            if ans7 == 'Molletes':
                resp = '<p style="font-family:Courier; color:Blue; font-size: 14px;">Correct! A mollete is an open-faced sandwich with beans and cheese in Mexican cuisine.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            elif ans7 == 'Injera':
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. Correct answer is molletes. <br></br>Injera is a staple in Ethiopia, Eritrea, and some parts of Sudan. It is a sour fermented flatbread with a slightly spongy texture, traditionally made of teff flour.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            elif ans7 == 'Banga':
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. Correct answer is molletes. <br></br>Banga is a soup made from palm nut fruit, an assortment of spices, and a variety of meat and fish. It is a popular soup in the Niger Delta part of Nigeria, particularly the Urhobo ethnic group.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            else:
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. Correct answer is molletes. <br></br>Pastilla is a North African meat or seafood pie made with warqa dough, which is similar to filo. It is a specialty of Morocco and Algeria.</p>'
                st.markdown(resp, unsafe_allow_html=True)

            options = ('Kuratsa', 'Tinikling', 'Flamenco', 'Tarantella')    
            ans8 = st.radio('Which Filipino tradition uses bamboo sticks and fast paced music to dance to?',
                            options, index=options.index(q8), key='ans8')
            if ans8 == 'Tinikling':
                resp = '<p style="font-family:Courier; color:Blue; font-size: 14px;">Correct! Tinikling is a traditional Philippine folk dance which originated during the Spanish colonial era. The dance involves two people beating, tapping, and sliding bamboo poles on the ground and against each other in coordination with one or more dancers who step over and in between the poles in a dance.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            elif ans8 == 'Kuratsa':
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. Correct answer is tinikling. <br></br>Kuratsa is a Filipino dance of flirtation and courtship, designed to be danced with a partner. Its movements mimic the mating ritual of a rooster and hen.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            elif ans8 == 'Flamenco':
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. Correct answer is tinikling. <br></br>Flamenco is a highly-expressive, Spanish dance form. The flamenco is a solo dance characterized by hand clapping, percussive footwork, and intricate hand, arm, and body movements.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            else:
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. Correct answer is tinikling. <br></br>Tarantella is a group of various folk dances characterized by a fast upbeat tempo, usually in time, accompanied by tambourines. It is among the most recognized forms of traditional southern Italian music.</p>'
                st.markdown(resp, unsafe_allow_html=True)

            options = ('Tango', 'Hip-hop', 'Salsa', 'Samba')
            ans9 = st.radio("Which of these is a symbol of Argentina's culture?",
                            options, index=options.index(q9), key='ans9')
            if ans9 == 'Tango':
                resp = '<p style="font-family:Courier; color:Blue; font-size: 14px;">Correct! Originating in Buenos Aires in the 18th century, tango brought together working class European immigrants, indigenous Argentinians and former slaves. As a result, tango has shaped Argentinian culture and society</p>'
                st.markdown(resp, unsafe_allow_html=True)
            elif ans9 == 'Hip-hop':
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. Correct answer is tango. <br></br>Hip-hop is a culture and art movement that was created by African Americans, Latino Americans and Caribbean Americans in the Bronx, New York City.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            elif ans9 == 'Salsa':
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. Correct answer is tango. <br></br>Salsa is an amalgamation of Cuban dances, such as mambo, pachanga, and rumba as well as American dances, such as swing and tap. It was primarily developed by Puerto Ricans and Cubans living in New York in the late 1960s and early 1970s.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            else:
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. Correct answer is tango. <br></br>Samba is a Brazilian musical genre and dance style, with its roots in Africa via the West African slave trade and African religious traditions</p>'
                st.markdown(resp, unsafe_allow_html=True)

            options = ('Congee', 'Lugaw', 'Harees', 'Pozole')
            ans10 = st.radio("What dish is shown in the photo below?",
                            options, index=options.index(q10), key='ans10')

            st.image('static/dishes/UnitedArabEmirates-Harees.jpeg', width=350)
            if ans10 == 'Harees':
                resp = '<p style="font-family:Courier; color:Blue; font-size: 14px;">Correct! Harees is a dish of boiled, cracked, or coarsely-ground wheat, mixed with meat and seasoned. Its consistency varies between a porridge and a gruel. Harees is a popular dish known in Arab states of the Persian Gulf, especially in the month of Ramadan.</p>'
                st.markdown(resp, unsafe_allow_html=True)
            else:
                resp = '<p style="font-family:Courier; color:Red; font-size: 14px;">Incorrect. Correct answer is harees. <br></br>Harees is a dish of boiled, cracked, or coarsely-ground wheat, mixed with meat and seasoned. Its consistency varies between a porridge and a gruel. Harees is a popular dish known in Arab states of the Persian Gulf, especially in the month of Ramadan.</p>'
                st.markdown(resp, unsafe_allow_html=True)