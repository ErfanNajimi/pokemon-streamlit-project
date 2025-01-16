import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pokemon.csv')

st.markdown('''   
# Pokemon Profiler
Find out more about your favourite pokemons with our app!
''')

user_input, icon = st.columns(2)
with icon:
    st.markdown('''
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/1200px-Pok%C3%A9_Ball_icon.svg.png" alt="pokeball-icon" width="100" style="display: block; margin: auto;">
    ''', unsafe_allow_html=True)

with user_input:
    pokedex_num = st.number_input('Pokedex Number: ', min_value=1 , max_value=898, step=1)

selected_pokemon = df[df['pokedex_number'] == int(pokedex_num)].iloc[0]

details, image = st.columns(2)
with details:
    st.table(selected_pokemon[['name', 'species', 'height_m', 'weight_kg', 'catch_rate']])

if pokedex_num  < 899:
    image_url_id = "0" * (3 - len(str(pokedex_num))) + str(pokedex_num) + ".png"
else:
    st.warning('Not a valid pokedex number!')

with image:
    st.markdown(f"""
        <div style="text-align: center;">
            <h2>{selected_pokemon['name']}</h2>
            <img src="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/{image_url_id}" alt="{selected_pokemon['name']}" style="width: 300px;">
            <p style="font-size: 12px; color: gray;">Image credits: <a href="https://www.pokemon.com/" target="_blank">https://www.pokemon.com/</a></p>
        </div>
    """, unsafe_allow_html=True)

# Pie Chart
labels = 'Hp', 'Attack', 'Defense', 'SP Attack', 'SP Defense', 'Speed'
sizes = selected_pokemon[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']]

fig2, ax = plt.subplots()
ax.pie(sizes, labels=labels)

st.subheader('Stats Pie Chart')
st.caption("Find out more about this pokemon's strength and weaknesses!")
st.pyplot(fig2)

st.markdown('''---''')

# Scatter Plot
sample_pokemon = df.sample(5)

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

fig,ax = plt.subplots()

for i, row in sample_pokemon.iterrows(): 
    plt.scatter(row['height_m'], row['weight_kg'], color='blue')
    plt.text(row['height_m'], row['weight_kg'], '    ' + str(row['name']))
plt.scatter(selected_pokemon['height_m'], selected_pokemon['weight_kg'], color='red')
plt.text(selected_pokemon['height_m'], selected_pokemon['weight_kg'], '   '+str(selected_pokemon['name']))

plt.xlabel('Weight / kg')
plt.ylabel('Height / m')

st.subheader('Pokemon Height vs Weight')
st.caption('See how your chosen pokemon compares with a random selection of others!')
st.pyplot(fig)
