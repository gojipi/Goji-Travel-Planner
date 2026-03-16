import streamlit as st

# 1. SETUP PAGE
st.set_page_config(page_title="Goji Travel Planner", page_icon="🗺️", layout="wide")

# 2. THE ULTIMATE CSS (NEON PIXEL UI)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
    
    .stApp { background-color: #0b0e14; }

    /* Fix Glitch & Font Global */
    h1, h2, h3, h4, p, label, li, [data-testid="stMetricValue"], [data-testid="stMetricLabel"], span:not(:has(svg)) {
        font-family: 'VT323', monospace !important;
        color: #ffffff !important;
    }

    [data-testid="stIcon"], svg, .material-icons {
        font-family: inherit !important;
        display: inline-block !important;
    }

    /* Tajuk Gempak */
    h1 { color: #f1c40f !important; font-size: 60px !important; text-shadow: 3px 3px #3498db; text-align: center; }

    /* Neon Cards */
    div[data-testid="stMetricContainer"] {
        background-color: #1a1f29;
        border: 2px solid #3498db;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 0 10px #3498db;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 2px solid #f1c40f; }

    /* Button Neon */
    .stButton>button {
        background-color: #f1c40f !important;
        color: #000 !important;
        font-weight: bold !important;
        border-radius: 5px !important;
        font-family: 'VT323', monospace !important;
        border: none;
        box-shadow: 0 0 15px #f1c40f;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR & LOGIC
with st.sidebar:
    st.title("🕹️ COMMAND CENTER")
    st.write("📍 **Base: Kuching, Sarawak**")
    st.write("📝 **Writer Mode: ACTIVE**")
    st.divider()
    
    destinasi = st.selectbox("CHOOSE MISSION:", 
        ["Bangkok", "Phuket", "Danang", "Sabah", "Sarawak", "China (Beijing)", "South Korea", "Japan (Tokyo)"])
    
    st.subheader("💰 CURRENCY CONVERTER")
    amount_myr = st.number_input("MYR AMOUNT:", value=100)
    
    # Rates and Weather Data
    data_destinasi = {
        "Bangkok": {"rate": 7.50, "curr": "THB", "weather": "32°C - Hot & Humid", "cloth": "Light cotton & sunglasses"},
        "Phuket": {"rate": 7.50, "curr": "THB", "weather": "30°C - Tropical Breeze", "cloth": "Beachwear & Sunscreen"},
        "Danang": {"rate": 5200.0, "curr": "VND", "weather": "28°C - Windy", "cloth": "Casual & Windbreaker"},
        "Sabah": {"rate": 1.0, "curr": "MYR", "weather": "27°C - Rainforest Fresh", "cloth": "Hiking shoes & raincoat"},
        "Sarawak": {"rate": 1.0, "curr": "MYR", "weather": "29°C - Home Vibes", "cloth": "Comfortable casual"},
        "China (Beijing)": {"rate": 1.55, "curr": "CNY", "weather": "15°C - Chilly", "cloth": "Layers & Jacket"},
        "South Korea": {"rate": 285.0, "curr": "KRW", "weather": "12°C - Cool Autumn", "cloth": "Stylish Coat & Boots"},
        "Japan (Tokyo)": {"rate": 32.0, "curr": "JPY", "weather": "14°C - Refreshing", "cloth": "Heat-tech & Sneakers"}
    }
    
    info = data_destinasi[destinasi]
    converted = amount_myr * info['rate']
    st.success(f"{amount_myr} MYR = {converted:,.2f} {info['curr']}")
    
    st.divider()
    hari = st.slider("DAYS:", 1, 14, 7)
    hotel = st.number_input("HOTEL/NIGHT (RM):", value=150)
    makan = st.number_input("MEAL/DAY (RM):", value=80)
    
    tiket_prices = {"Bangkok": 450, "Phuket": 380, "Danang": 650, "Sabah": 250, "Sarawak": 150, "China (Beijing)": 1200, "South Korea": 1500, "Japan (Tokyo)": 1800}
    tiket = tiket_prices[destinasi]

# 4. MAIN DASHBOARD
st.title("🗺️ GOJI GLOBAL PLANNER")

# Stats Row
total_kos = (hari * hotel) + (hari * makan) + tiket
c1, c2, c3, c4 = st.columns(4)
c1.metric("FLIGHT", f"RM{tiket}")
c2.metric("BUDGET", f"RM{total_kos}")
c3.metric("WEATHER", info['weather'])
c4.metric("DRESS CODE", "Verified")

st.info(f"💡 **Suggested Wear:** {info['cloth']}")

st.divider()

# 5. ITINERARY DATABASE (SUPER LONG - NO TRIMMING)
itineraries = {
    "Bangkok": """* **Day 1:** Arrival & Jodd Fairs Market. * **Day 2:** Grand Palace & Wat Arun. * **Day 3:** Siam Shopping District. * **Day 4:** Ari Cafe Hopping. * **Day 5:** Floating Market Trip. * **Day 6:** Chatuchak Weekend Market. * **Day 7:** Massage & Airport.""",
    "Phuket": """* **Day 1:** Patong Beach Explore. * **Day 2:** Phi Phi Island Boat Tour. * **Day 3:** Phuket Old Town Photography. * **Day 4:** Big Buddha & Sunset Viewpoints. * **Day 5:** Elephant Sanctuary. * **Day 6:** James Bond Island Kayaking. * **Day 7:** Relax at Kata Beach & Fly.""",
    "Danang": """* **Day 1:** Dragon Bridge & Seafood Dinner. * **Day 2:** Ba Na Hills (Golden Bridge). * **Day 3:** Marble Mountains & Hoi An Arrival. * **Day 4:** Hoi An Ancient Town Walking Tour. * **Day 5:** My Son Sanctuary Ruins. * **Day 6:** Son Tra Peninsula & Lady Buddha. * **Day 7:** Han Market & Fly home.""",
    "Sabah": """* **Day 1:** KK Waterfront sunset. * **Day 2:** Kundasang (Desa Dairy Farm & Alpaca). * **Day 3:** Poring Hot Spring & Canopy Walk. * **Day 4:** Kinabalu Park hiking trail. * **Day 5:** Island Hopping (Manukan/Sapi). * **Day 6:** Mari Mari Cultural Village. * **Day 7:** Gaya Street Market (Sunday) & Fly.""",
    "Sarawak": """* **Day 1:** Kuching Waterfront & Terubok Mas shopping. * **Day 2:** Bako National Park (Proboscis monkeys). * **Day 3:** Sarawak Cultural Village. * **Day 4:** Semenggoh Wildlife Centre (Orangutan). * **Day 5:** Siniawan Night Market. * **Day 6:** Tasik Biru & Wind Caves Bau. * **Day 7:** Laksa Sarawak breakfast & Airport.""",
    "China (Beijing)": """* **Day 1:** Arrival & Wangfujing Street Food. * **Day 2:** Great Wall of China (Mutianyu). * **Day 3:** Forbidden City & Tiananmen Square. * **Day 4:** Summer Palace & Kunming Lake. * **Day 5:** Temple of Heaven & Pearl Market. * **Day 6:** Olympic Park (Bird's Nest). * **Day 7:** Hutong Tour & Departure.""",
    "South Korea": """* **Day 1:** Incheon to Myeongdong shopping. * **Day 2:** Gyeongbokgung Palace (Hanbok experience). * **Day 3:** Nami Island & Petite France. * **Day 4:** Bukchon Hanok Village & Insadong. * **Day 5:** Hongdae Street Vibe & Cafes. * **Day 6:** Lotte World or N Seoul Tower. * **Day 7:** Last minute skincare shopping at Olive Young & Fly.""",
    "Japan (Tokyo)": """* **Day 1:** Shibuya Crossing & Hachiko. * **Day 2:** Shinjuku Gyoen & Tokyo Metropolitan View. * **Day 3:** Senso-ji Temple (Asakusa) & Nakamise. * **Day 4:** Akihabara Electric Town explore. * **Day 5:** Tokyo DisneySea or Disneyland. * **Day 6:** Harajuku (Takeshita Street) & Meiji Jingu. * **Day 7:** Tsukiji Outer Market breakfast & Airport."""
}

# 6. TABS
tab1, tab2, tab3, tab4 = st.tabs(["📜 MISSION LOG (ITINERARY)", "🎒 30KG CHECKLIST", "🖼️ MEMORY BANK (GALLERY)", "📓 WRITER'S JOURNAL"])

with tab1:
    st.markdown(f"### 🏁 7-Day Quest: {destinasi}")
    st.write(itineraries[destinasi])

with tab2:
    st.header("🎒 The Ultimate 30KG Checklist")
    st.warning("⚠️ CRITICAL: UNIVERSAL ADAPTER (Vietnam Lesson Learned!)")
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
    st.write("Future spot for your sunset photography from Thailand, Vietnam, and beyond!")
    st.image("https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?q=80&w=1000", caption="Phuket Dream")
    st.image("https://images.unsplash.com/photo-1528127269322-539801943592?q=80&w=1000", caption="Danang Bridge")

with tab4:
    nota = st.text_area("Write your fantasy bab draft or trip notes...", height=250)
    if st.button("SAVE ENTRY"):
        st.success("Archived in the brain cloud!")