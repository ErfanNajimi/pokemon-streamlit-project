import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# search_history = {}
# search_counter = 0
# def save_search(value):
#     search_counter += 1
#     search_history[str(search_counter)] = {
#         'pokedex_num' : pokedex_num, 
#         'image_url_id' : image_url_id,
#     }
    
df = pd.read_csv('pokemon.csv')
# df

# Cleaning df - remove Mega Pokemon NOT needed!
search_num = 0

# text_input restrict to numbers - later

st.markdown('''   
# Pokemon Profiler
''')
##### Enter the pokedex number of the pokemon you would like to look up below.
user_input, icon = st.columns(2)
with icon: 
    st.markdown('''
        ![pokeball-icon](https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/1200px-Pok%C3%A9_Ball_icon.svg.png)
    ''')

# with user_input:
#     pokedex_num = st.text_input('Pokedex Number: ', placeholder="Enter Pokedex Number", on_change=None)

with user_input:
    pokedex_num = st.number_input('Pokedex Number: ', min_value=1 , max_value=898, step=1)

selected_pokemon = df[df['pokedex_number'] == int(pokedex_num)].iloc[0]

details, image = st.columns(2)
with details:
    st.table(selected_pokemon[['name', 'species', 'height_m', 'weight_kg', 'catch_rate']])

if pokedex_num  < 899:
    image_url_id = "0" * (3 - pokedex_num) + str(pokedex_num) + ".png"
else:
    st.warning('Not a valid pokedex number!')

with image:
    st.markdown(f"""
        ## {selected_pokemon['name']}
        ![pokemon-image-url](https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/{image_url_id})
    """)
    st.caption('Image credits: https://www.pokemon.com')
    

sample_pokemon = df.sample(5)
sample_pokemon = pd.concat([sample_pokemon, selected_pokemon])

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

# Scatter Plot
# plot = plt.scatter(sample_pokemon['weight_kg'], sample_pokemon['height_m'])
# plt.figure(figsize=(10, 6))
# plt.title("Pokemon Height vs. Weight")
# plt.xlabel("Weight")
# plt.ylabel("Height")

# st.pyplot(plot)

fig,ax = plt.subplots()
# ax.scatter(sample_pokemon['weight_kg'], sample_pokemon['height_m'])
# plt.xlabel('Weight / kg')
# plt.ylabel('Height / m')

# for i in range(len(sample_pokemon)):
#     plt.text(sample_pokemon.loc[[i]], sample_pokemon.loc[[i]], sample_pokemon.loc[[i]])

for i, row in sample_pokemon.iterrows(): 

    if i == 6:
        plt.scatter(row['height_m'], row['weight_kg'], color='red')
    else:
        plt.scatter(row['height_m'], row['weight_kg'], color='blue')

    plt.text(row['height_m'], row['weight_kg'], '  ' + row['name'])


plt.xlabel('Weight / kg')
plt.ylabel('Height / m')
st.pyplot(fig)

# ------- SIDEBAR ---------

with st.sidebar:
    # History of Pokedex Searchs
    st.write('Searching History:')
    for key in search_history.keys():
        st.write(f'search_history{[key]}')