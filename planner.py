import streamlit as st
from datetime import datetime

# 1. SETUP PAGE
st.set_page_config(page_title="Goji Travel Planner", page_icon="✈️", layout="wide")

# 2. THE ULTIMATE CSS (CLEAN PRE-TRAVEL UI)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Inter:wght@400;600&display=swap');
    
    .stApp { background-color: #0b0e14; }

    /* Font Global */
    .stMarkdown p, .stMarkdown li, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, 
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"], .stCheckbox label {
        font-family: 'Inter', sans-serif !important;
        color: #ffffff !important;
    }

    /* Tajuk Header */
    h1 { 
        font-family: 'Montserrat', sans-serif !important; 
        color: #f1c40f !important; 
        font-size: 48px !important; 
        text-align: center;
        text-shadow: 2px 2px #000000;
        margin-bottom: 20px;
    }

    /* Pagar Besi - Prevent Glitch */
    button, [data-testid="stHeader"], [data-testid="stIcon"], svg, 
    [data-testid="collapsedControl"], .st-emotion-cache-6qob1r {
        font-family: inherit !important;
    }

    /* Card Metrics */
    div[data-testid="stMetricContainer"] {
        background-color: #1a1f29; 
        border: 1px solid #3498db; 
        border-radius: 12px; 
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] { 
        background-color: #161b22 !important; 
        border-right: 1px solid #3498db; 
    }
    
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #1a1f29;
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR & LOGIC
with st.sidebar:
    st.title("🗺️ MISSION CONTROL")
    st.write("📍 Base: **Kuching, Sarawak**")
    st.divider()
    
    destinasi = st.selectbox("SELECT DESTINATION:", 
        ["Bangkok", "Phuket", "Danang", "Sabah", "Sarawak", "China (Beijing)", "South Korea", "Japan (Tokyo)"])
    
    # DATABASE UTAMA
    db = {
        "Bangkok": {"rate": 7.50, "curr": "THB", "weather": "32°C Hot", "cloth": "Cotton", "sos": "1155 (Tourist Police)", "food": ["Volcanic Ribs", "Mango Sticky Rice", "Yaowarat Toasted Bread"]},
        "Phuket": {"rate": 7.50, "curr": "THB", "weather": "30°C Tropical", "cloth": "Beachwear", "sos": "1155", "food": ["Grilled Lobster", "Pad Thai", "Cashew Nuts"]},
        "Danang": {"rate": 5200.0, "curr": "VND", "weather": "28°C Windy", "cloth": "Casual", "sos": "113", "food": ["Banh Mi Phuong", "Seafood BBQ", "Vietnamese Coffee"]},
        "Sabah": {"rate": 1.0, "curr": "MYR", "weather": "27°C Fresh", "cloth": "Outdoor", "sos": "999", "food": ["Sinalau Bakas", "Tuaran Mee", "Desa Milk"]},
        "Sarawak": {"rate": 1.0, "curr": "MYR", "weather": "29°C Humid", "cloth": "Casual", "sos": "999", "food": ["Laksa Sarawak", "Kolo Mee", "Gula Apong Ice Cream"]},
        "China (Beijing)": {"rate": 1.55, "curr": "CNY", "weather": "15°C Cold", "cloth": "Jacket", "sos": "110", "food": ["Peking Duck", "Hutong Snacks", "Dumplings"]},
        "South Korea": {"rate": 285.0, "curr": "KRW", "weather": "12°C Chilly", "cloth": "Coat", "sos": "1330", "food": ["Tteokbokki", "Korean Fried Chicken", "K-BBQ"]},
        "Japan (Tokyo)": {"rate": 32.0, "curr": "JPY", "weather": "14°C Refresh", "cloth": "Sneakers", "sos": "110", "food": ["Tsukiji Sushi", "Ichiran Ramen", "Wagyu Beef"]}
    }
    
    info = db[destinasi]
    amount_myr = st.number_input("CONVERT MYR:", value=100)
    st.success(f"Est: {amount_myr * info['rate']:,.2f} {info['curr']}")
    
    st.divider()
    tarikh_fly = st.date_input("FLIGHT DATE:", datetime.now())
    days_left = (tarikh_fly - datetime.now().date()).days
    st.info(f"{max(0, days_left)} Days Remaining!")

# 4. DASHBOARD HEADER
st.title("GOJI TRAVEL ENGINE")
c1, c2, c3, c4 = st.columns(4)
c1.metric("EXCHANGE RATE", f"1 MYR = {info['rate']} {info['curr']}")
c2.metric("LOCAL TIME", datetime.now().strftime("%H:%M"))
c3.metric("WEATHER", info['weather'])
c4.metric("DRESS CODE", info['cloth'])

st.divider()

# 5. ITINERARY DATABASE (FULL KNOWLEDGE - NO TRIMMING)
itineraries = {
    "Bangkok": """
    * **Day 1: Arrival & Night Street Food** - Check-in and head to Jodd Fairs. Must try: Volcanic Pork Ribs & Fruit Shakes.
    * **Day 2: Royal Heritage** - Grand Palace & Wat Pho. Take a cross-river boat (5 THB) to Wat Arun for sunset views.
    * **Day 3: Shopping Marathon** - Siam Paragon for brands, MBK for gadgets, and CentralWorld. Dinner at Yaowarat (Chinatown).
    * **Day 4: Cafe Hopping Ari** - Explore Ari's hidden cafes. Great vibe for relaxing and planning your next move.
    * **Day 5: Floating Market** - Day trip to Maeklong Railway Market (train passes through stalls) & Damnoen Saduak.
    * **Day 6: Chatuchak Quest** - Full day at the world's largest weekend market. Buy home decor & cheap clothes.
    * **Day 7: Last Massage & Fly** - Foot massage at Let's Relax, grab snacks at Big C Supercenter, and head to airport.
    """,
    "Phuket": """
    * **Day 1: Patong Vibe** - Check-in and enjoy Patong Beach. Explore Bangla Road's neon lights at night.
    * **Day 2: Phi Phi Islands** - Speedboat tour to Maya Bay, Pileh Lagoon, and Viking Cave. Snorkeling is a must!
    * **Day 3: Old Town History** - Walk through Thalang Road. Beautiful Sino-Portuguese architecture & Sunday Market.
    * **Day 4: Big Buddha & Viewpoints** - Visit the 45m tall Big Buddha and catch sunset at Promthep Cape.
    * **Day 5: Elephant Sanctuary** - Ethical interaction with rescued elephants. Learn about their conservation.
    * **Day 6: James Bond Island** - Kayaking through limestone caves in Phang Nga Bay (Ao Phang Nga National Park).
    * **Day 7: Chill & Fly** - Relax at Kata or Karon Beach. Buy cashew nut snacks before heading to HKT airport.
    """,
    "Danang": """
    * **Day 1: City of Bridges** - Arrival and check-in near My Khe Beach. Watch Dragon Bridge spit fire (Weekends 9PM).
    * **Day 2: Ba Na Hills** - Take the world's longest cable car to Golden Bridge and the French Village.
    * **Day 3: Marble Mountains & Hoi An** - Explore caves and pagodas in Marble Mountains. Evening in Hoi An Ancient Town.
    * **Day 4: Hoi An Immersion** - Take a lantern boat ride and try Banh Mi Phuong (World's best sandwich).
    * **Day 5: My Son Sanctuary** - Visit the UNESCO Champa ruins. Afternoon back to Danang for seafood.
    * **Day 6: Son Tra Peninsula** - Visit Lady Buddha and drive up the Monkey Mountain for coastal views.
    * **Day 7: Han Market Shopping** - Buy Vietnamese coffee (Trung Nguyen) and dried fruits before flying home.
    """,
    "Sabah": """
    * **Day 1: KK Waterfront** - Arrive in KK, dinner at Todak Waterfront (fresh seafood). Watch sunset at Tanjung Aru.
    * **Day 2: Kundasang Trip** - Drive to Kundasang. Visit Desa Dairy Farm (New Zealand vibes) & Alpaca Farm.
    * **Day 3: Nature & Springs** - Poring Hot Spring, Canopy Walk, and find the Rafflesia flower if in season.
    * **Day 4: Kinabalu Park** - Botanical Garden tour at the base of Mt. Kinabalu. Fresh mountain air!
    * **Day 5: Island Hopping** - Take a boat from Jesselton Point to Manukan and Sapi Island. Crystal clear water!
    * **Day 6: Cultural Village** - Mari Mari Cultural Village to learn about the 5 main tribes of Sabah.
    * **Day 7: Gaya Street Market** - (Sunday only) Shopping for local souvenirs and head to KKIA.
    """,
    "Sarawak": """
    * **Day 1: Kuching Waterfront** - Stroll along the Sarawak River. Try Kek Lapis India and Gula Apong ice cream.
    * **Day 2: Bako National Park** - Boat ride to see Proboscis Monkeys, wild boars, and sea stacks.
    * **Day 3: Cultural Heritage** - Sarawak Cultural Village (Living Museum). Watch the multi-cultural dance show.
    * **Day 4: Wildlife Encounter** - Semenggoh Wildlife Centre to see Orangutans during feeding time.
    * **Day 5: Caves & Heritage** - Visit Fairy Cave and Wind Cave in Bau. Evening at Siniawan Night Market.
    * **Day 6: Food Quest** - Hunting for the best Laksa Sarawak (Choon Hui Cafe) and Kolo Mee. Visit Borneo Cultures Museum.
    * **Day 7: Main Bazaar Shopping** - Buy Sarawak Pepper and beads. Last walk at the Waterfront before KCH airport.
    """,
    "China (Beijing)": """
    * **Day 1: Arrival & Roast Duck** - Arrival in Beijing. Dinner with authentic Peking Duck at Quanjude.
    * **Day 2: The Great Wall** - Hike the Mutianyu section (less crowded). Take the toboggan slide down!
    * **Day 3: Imperial History** - Forbidden City (book early!) and Tiananmen Square. Jingshan Park for bird's eye view.
    * **Day 4: Summer Palace** - Huge royal garden and Kunming Lake. Beautiful boat rides and ancient bridges.
    * **Day 5: Temple of Heaven** - Watch locals do Tai Chi. Afternoon shopping at Hongqiao Pearl Market.
    * **Day 6: Modern Beijing** - Visit Olympic Park (Bird's Nest) and the 798 Art District for contemporary vibes.
    * **Day 7: Hutong Tour** - Rickshaw ride through old alleys. Tea ceremony experience before heading to airport.
    """,
    "South Korea": """
    * **Day 1: Myeongdong Seoul** - Arrival and check-in. Street food heaven in Myeongdong and skincare shopping.
    * **Day 2: Royal Palaces** - Gyeongbokgung Palace in a Hanbok (Free entry!). Walk to Bukchon Hanok Village.
    * **Day 3: Nami Island** - Romantic day trip to Nami Island and Petite France (Garden of Morning Calm).
    * **Day 4: N Seoul Tower** - Panoramic views of Seoul. Evening at Insadong for traditional crafts and tea.
    * **Day 5: Trendy Hongdae** - Youthful vibes, busking, and themed cafes. Great for night life and shopping.
    * **Day 6: Lotte World or Gangnam** - Theme park fun or explore the posh Gangnam district (COEX Mall Library).
    * **Day 7: Grocery Haul** - Last stop at Lotte Mart for seaweed/snacks. Flight from ICN.
    """,
    "Japan (Tokyo)": """
    * **Day 1: Shibuya & Harajuku** - Shibuya Crossing, Hachiko, and Takeshita Street for crazy snacks.
    * **Day 2: Asakusa Culture** - Senso-ji Temple and Nakamise shopping street. Evening at Tokyo Skytree.
    * **Day 3: Shinjuku Vibes** - Visit Shinjuku Gyoen National Garden and the Omoide Yokocho (Memory Lane) for dinner.
    * **Day 4: Akihabara Quest** - The Electric Town. Anime, manga, and retro gaming shops. Must visit Super Potato!
    * **Day 5: Disney Day** - Full day at Tokyo DisneySea (unique to Japan) or Tokyo Disneyland.
    * **Day 6: TeamLab Borderless** - Immersive digital art museum. Afternoon at Ginza for luxury shopping.
    * **Day 7: Tsukiji Breakfast** - Early morning sushi at Tsukiji Outer Market. Last souvenir run at Don Quijote.
    """
}

# 6. TABS
tab1, tab2, tab3, tab4 = st.tabs(["📜 MISSION LOG", "🍱 FOODIE & SOS", "🖼️ GALLERY", "📝 NOTES"])

with tab1:
    st.header(f"Mission: {destinasi}")
    st.markdown(itineraries[destinasi])

with tab2:
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("🍲 Foodie Checklist")
        st.write("Tick once tasted:")
        for f in info['food']:
            st.checkbox(f, key=f"{destinasi}_{f}")
    with col_b:
        st.subheader("🚨 Emergency Info")
        st.error(f"Local SOS: {info['sos']}")
        st.warning("Keep your digital passport copy ready!")

with tab3:
    st.header("🖼️ Memory Bank")
    st.write("Direct Links from PostImages go here!")
    g1, g2 = st.columns(2)
    with g1:
        st.image("https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?q=80&w=1000", caption="Sample Phuket")
    with g2:
        st.image("https://images.unsplash.com/photo-1512100356956-c1227c331f01?q=80&w=1000", caption="Sample Travel")

with tab4:
    st.subheader("📝 Travel Log & Expenses")
    st.text_area("Record your spending or mission notes here...", height=300, placeholder="Eg: Dinner at Night Market - 200 THB")
    if st.button("SAVE ENTRY"):
        st.success("Entry archived!")