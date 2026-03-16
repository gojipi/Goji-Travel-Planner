import streamlit as st

# 1. SETUP PAGE
st.set_page_config(page_title="Goji Travel Planner", page_icon="🗺️", layout="wide")

# 2. THE ULTIMATE CSS (ANTI-GLITCH V5)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
    .stApp { background-color: #0b0e14; }

    /* Target Teks Sahaja */
    h1, h2, h3, h4, p, label, li, [data-testid="stMetricValue"], [data-testid="stMetricLabel"], span:not(:has(svg)) {
        font-family: 'VT323', monospace !important;
        color: #ffffff !important;
    }

    /* Protect Icons & Sidebar Arrow */
    [data-testid="stIcon"], svg, .material-icons, button[kind="headerNoPadding"] span {
        font-family: sans-serif !important;
        display: inline-block !important;
    }

    h1 { color: #f1c40f !important; font-size: 55px !important; text-shadow: 3px 3px #3498db; text-align: center; }
    div[data-testid="stMetricContainer"] {
        background-color: #1a1f29; border: 2px solid #3498db; border-radius: 10px; padding: 15px; box-shadow: 0 0 10px #3498db;
    }
    [data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 2px solid #f1c40f; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR & LOGIC
with st.sidebar:
    st.title("🕹️ COMMAND CENTER")
    st.write("📍 **Base: Kuching, Sarawak**")
    st.divider()
    
    destinasi = st.selectbox("CHOOSE MISSION:", 
        ["Bangkok", "Phuket", "Danang", "Sabah", "Sarawak", "China (Beijing)", "South Korea", "Japan (Tokyo)"])
    
    data_destinasi = {
        "Bangkok": {"rate": 7.50, "curr": "THB", "weather": "32°C - Hot", "cloth": "Light cotton"},
        "Phuket": {"rate": 7.50, "curr": "THB", "weather": "30°C - Tropical", "cloth": "Beachwear"},
        "Danang": {"rate": 5200.0, "curr": "VND", "weather": "28°C - Windy", "cloth": "Casual"},
        "Sabah": {"rate": 1.0, "curr": "MYR", "weather": "27°C - Fresh", "cloth": "Outdoor shoes"},
        "Sarawak": {"rate": 1.0, "curr": "MYR", "weather": "29°C - Humid", "cloth": "Casual"},
        "China (Beijing)": {"rate": 1.55, "curr": "CNY", "weather": "15°C - Cold", "cloth": "Jacket/Layers"},
        "South Korea": {"rate": 285.0, "curr": "KRW", "weather": "12°C - Chilly", "cloth": "Coat & Boots"},
        "Japan (Tokyo)": {"rate": 32.0, "curr": "JPY", "weather": "14°C - Refreshing", "cloth": "Sneakers & Heat-tech"}
    }
    
    info = data_destinasi[destinasi]
    amount_myr = st.number_input("MYR AMOUNT:", value=100)
    st.success(f"Estimate: {amount_myr * info['rate']:,.2f} {info['curr']}")
    
    st.divider()
    hari = st.slider("DAYS:", 1, 14, 7)
    hotel = st.number_input("HOTEL/NIGHT (RM):", value=150)
    makan = st.number_input("MEAL/DAY (RM):", value=80)
    tiket_prices = {"Bangkok": 450, "Phuket": 380, "Danang": 650, "Sabah": 250, "Sarawak": 150, "China (Beijing)": 1200, "South Korea": 1500, "Japan (Tokyo)": 1800}
    tiket = tiket_prices[destinasi]

# 4. DASHBOARD
st.title("🗺️ GOJI GLOBAL PLANNER")
total_kos = (hari * hotel) + (hari * makan) + tiket
c1, c2, c3, c4 = st.columns(4)
c1.metric("FLIGHT", f"RM{tiket}")
c2.metric("BUDGET", f"RM{total_kos}")
c3.metric("WEATHER", info['weather'])
c4.metric("DRESS", info['cloth'])

st.divider()

# 5. ITINERARY DATABASE
itineraries = {
    "Bangkok": """
    * **Day 1: Arrival & Night Street Food** - Check-in and head to Jodd Fairs. Must try: Volcanic Pork Ribs & Fruit Shakes.
    * **Day 2: Royal Heritage** - Grand Palace & Wat Pho. Take a cross-river boat (5 THB) to Wat Arun for sunset views.
    * **Day 3: Shopping Marathon** - Siam Paragon for brands, MBK for gadgets, and CentralWorld. Dinner at Yaowarat (Chinatown).
    * **Day 4: Cafe Hopping Ari** - Explore Ari's hidden cafes. Great spot for writers to get inspiration.
    * **Day 5: Floating Market** - Day trip to Maeklong Railway Market (train passes through stalls) & Damnoen Saduak.
    * **Day 6: Chatuchak Quest** - Full day at the world's largest weekend market. Buy home decor & cheap clothes.
    * **Day 7: Last Massage & Fly** - Foot massage at Let's Relax, grab snacks at Big C Supercenter, and head home.
    """,
    "Phuket": """
    * **Day 1: Patong Vibe** - Check-in and enjoy Patong Beach. Explore Bangla Road's neon lights at night.
    * **Day 2: Phi Phi Islands** - Speedboat tour to Maya Bay, Pileh Lagoon, and Viking Cave. Snorkeling is a must!
    * **Day 3: Old Town History** - Walk through Thalang Road. Beautiful Sino-Portuguese architecture & Sunday Market.
    * **Day 4: Big Buddha & Viewpoints** - Visit the 45m tall Big Buddha and catch sunset at Promthep Cape.
    * **Day 5: Elephant Sanctuary** - Ethical interaction with rescued elephants. Learn about their conservation.
    * **Day 6: James Bond Island** - Kayaking through limestone caves in Phang Nga Bay.
    * **Day 7: Chill & Fly** - Relax at Kata or Karon Beach. Buy cashew nut snacks before heading to airport.
    """,
    "Danang": """
    * **Day 1: City of Bridges** - Arrival and watch Dragon Bridge spit fire (Weekends 9PM).
    * **Day 2: Ba Na Hills** - Take the cable car to Golden Bridge and the French Village.
    * **Day 3: Marble Mountains & Hoi An** - Explore caves and pagodas. Evening in Hoi An Ancient Town.
    * **Day 4: Hoi An Immersion** - Take a lantern boat ride and try Banh Mi Phuong.
    * **Day 5: My Son Sanctuary** - Visit the UNESCO Champa ruins. Afternoon back for seafood.
    * **Day 6: Son Tra Peninsula** - Visit Lady Buddha and drive up for coastal views.
    * **Day 7: Han Market Shopping** - Buy Vietnamese coffee (Trung Nguyen) before flying home.
    """,
    "Sabah": """
    * **Day 1: KK Waterfront** - Dinner at Todak Waterfront. Watch sunset at Tanjung Aru.
    * **Day 2: Kundasang Trip** - Drive to Kundasang. Visit Desa Dairy Farm (New Zealand vibes).
    * **Day 3: Nature & Springs** - Poring Hot Spring, Canopy Walk, and find the Rafflesia flower.
    * **Day 4: Kinabalu Park** - Botanical Garden tour at the base of Mt. Kinabalu.
    * **Day 5: Island Hopping** - Boat from Jesselton Point to Manukan and Sapi Island.
    * **Day 6: Cultural Village** - Mari Mari Cultural Village to learn about the 5 main tribes.
    * **Day 7: Gaya Street Market** - (Sunday only) Shopping for local souvenirs and head to KKIA.
    """,
    "Sarawak": """
    * **Day 1: Kuching Waterfront** - Try Kek Lapis India and Gula Apong ice cream.
    * **Day 2: Bako National Park** - Boat ride to see Proboscis Monkeys and sea stacks.
    * **Day 3: Cultural Heritage** - Sarawak Cultural Village. Watch the multi-cultural dance show.
    * **Day 4: Wildlife Encounter** - Semenggoh Wildlife Centre to see Orangutans.
    * **Day 5: Caves & Heritage** - Visit Fairy Cave and Wind Cave in Bau. Evening at Siniawan.
    * **Day 6: Food Quest** - Hunting for the best Laksa Sarawak and Kolo Mee.
    * **Day 7: Main Bazaar Shopping** - Buy Sarawak Pepper and beads before heading to KCH.
    """,
    "China (Beijing)": """
    * **Day 1: Arrival & Roast Duck** - Dinner with authentic Peking Duck at Quanjude.
    * **Day 2: The Great Wall** - Hike the Mutianyu section. Take the toboggan slide down!
    * **Day 3: Imperial History** - Forbidden City and Tiananmen Square. Jingshan Park view.
    * **Day 4: Summer Palace** - Huge royal garden and Kunming Lake boat ride.
    * **Day 5: Temple of Heaven** - Watch locals do Tai Chi. Afternoon shopping at Pearl Market.
    * **Day 6: Modern Beijing** - Visit Olympic Park (Bird's Nest) and the 798 Art District.
    * **Day 7: Hutong Tour** - Rickshaw ride through old alleys before heading to airport.
    """,
    "South Korea": """
    * **Day 1: Myeongdong Seoul** - Arrival and check-in. Street food and skincare shopping.
    * **Day 2: Royal Palaces** - Gyeongbokgung Palace in a Hanbok. Visit Bukchon Hanok Village.
    * **Day 3: Nami Island** - Romantic day trip to Nami Island and Petite France.
    * **Day 4: N Seoul Tower** - Panoramic views. Evening at Insadong for traditional crafts.
    * **Day 5: Trendy Hongdae** - Youthful vibes, busking, and themed cafes.
    * **Day 6: Lotte World or Gangnam** - Theme park fun or explore the posh Gangnam district.
    * **Day 7: Grocery Haul** - Last stop at Lotte Mart for seaweed/snacks.
    """,
    "Japan (Tokyo)": """
    * **Day 1: Shibuya & Harajuku** - Shibuya Crossing and Takeshita Street snacks.
    * **Day 2: Asakusa Culture** - Senso-ji Temple. Evening at Tokyo Skytree.
    * **Day 3: Shinjuku Vibes** - Visit Shinjuku Gyoen Garden and Omoide Yokocho.
    * **Day 4: Akihabara Quest** - The Electric Town. Anime and retro gaming shops.
    * **Day 5: Disney Day** - Full day at Tokyo DisneySea or Tokyo Disneyland.
    * **Day 6: TeamLab Borderless** - Immersive digital art museum. Afternoon at Ginza.
    * **Day 7: Tsukiji Breakfast** - Early morning sushi at Tsukiji Outer Market.
    """
}

# 6. TABS
tab1, tab2, tab3, tab4 = st.tabs(["📜 MISSION LOG", "🎒 CHECKLIST", "🖼️ MEMORY BANK", "📓 JOURNAL"])

with tab1:
    st.markdown(f"### 🏁 Destination: {destinasi}")
    st.info(itineraries[destinasi])

with tab2:
    st.header("🎒 30KG Packing List")
    st.warning("⚠️ REMINDER: UNIVERSAL ADAPTER (Vietnam trauma prevention!)")
    c_a, c_b = st.columns(2)
    with c_a:
        st.subheader("📁 Documents")
        for i in ["Passport", "Tickets", "Insurance", "Cash/Debit Card"]: st.checkbox(i)
        st.subheader("🔌 Tech")
        for i in ["Universal Adapter", "Extension Wire", "Powerbank", "Gimbal"]: st.checkbox(i)
    with c_b:
        st.subheader("🧴 Skincare")
        for i in ["Niacinamide Serum", "Moisturizer", "Sunscreen SPF50", "Wet Wipes"]: st.checkbox(i)
        st.subheader("👕 Others")
        for i in ["7 Sets Outfit", "Walking Shoes", "Empty Tupperware", "Raincoat"]: st.checkbox(i)

with tab3:
    st.header("🖼️ Memory Bank")
    st.image("https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?q=80&w=1000", caption="Phuket Dream")

with tab4:
    nota = st.text_area("Write your quest logs or Wattpad drafts...", height=250)
    if st.button("SAVE ENTRY"):
        st.success("Entry archived!")