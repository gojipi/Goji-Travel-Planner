import streamlit as st

# 1. Setup Page
st.set_page_config(page_title="Goji Travel Planner", page_icon="🗺️", layout="wide")

# --- 2. CUSTOM CSS (CARA NUKLEAR - HAPUSKAN TERUS KEYBOARD_DOUBLE_ARROW) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

    .stApp {
        background-color: #0e1117;
    }

    /* Target spesifik gila supaya tak terkena icon sistem */
    h1, h2, h3, h4, 
    [data-testid="stHeader"] *, 
    [data-testid="stMarkdownContainer"] p, 
    [data-testid="stMetricValue"], 
    [data-testid="stMetricLabel"],
    label {
        font-family: 'VT323', monospace !important;
        color: #ffffff !important;
    }

    /* MATIKAN terus font pixel pada mana-mana icon */
    [data-testid="stIcon"], 
    svg, 
    i, 
    .material-icons,
    [class*="st-emotion-cache"] i,
    [class*="st-emotion-cache"] svg {
        font-family: inherit !important;
        display: inline-block !important;
    }

    /* Tajuk & Sidebar */
    h1 { color: #f1c40f !important; font-size: 50px !important; text-shadow: 2px 2px #000000; }
    [data-testid="stSidebar"] { background-color: #1e2129 !important; border-right: 1px solid #3498db; }
    
    /* Button */
    .stButton>button {
        background-color: #3498db !important;
        color: white !important;
        border-radius: 5px !important;
        font-family: 'VT323', monospace !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR (INVENTORY)
with st.sidebar:
    st.header("⚙️ SETTINGS")
    destinasi = st.selectbox("DESTINATION:", ["Bangkok", "Phuket", "Danang"])
    st.divider()
    hari = st.slider("DAYS:", 1, 14, 7)
    hotel = st.number_input("HOTEL/NIGHT (RM):", value=150)
    makan = st.number_input("MEAL/DAY (RM):", value=80)
    
    harga_tiket = {"Bangkok": 450, "Phuket": 380, "Danang": 650}
    tiket = harga_tiket[destinasi]

# 4. MAIN CONTENT
st.title("🗺️ GOJI TRAVEL PLANNER")
st.subheader(f"Current Mission: Exploring {destinasi}")

# Budget Stats
total_kos = (hari * hotel) + (hari * makan) + tiket
col1, col2, col3 = st.columns(3)
col1.metric("FLIGHT", f"RM{tiket}")
col2.metric("TOTAL BUDGET", f"RM{total_kos}")
col3.metric("DURATION", f"{hari} DAYS")

st.divider()

# 5. ITINERARY DATABASE (INI YANG PANJANG MACAM KAU NAK)
itineraries = {
    "Bangkok": """
    * **Day 1: Arrival & Night Vibe** - Check-in hotel, dinner at Jodd Fairs Night Market (cuba Volcanic Ribs!).
    * **Day 2: Culture & History** - Visit Grand Palace, Wat Pho (Reclining Buddha), and cross the river to Wat Arun for sunset.
    * **Day 3: Shopping Spree** - Full day at Siam Paragon, MBK Center, and CentralWorld. Malam pergi Chinatown (Yaowarat) untuk street food.
    * **Day 4: Cafe Hopping & Ari** - Explore kawasan Ari yang tenang, banyak cafe aesthetic untuk 'Writer's Inspiration'.
    * **Day 5: Floating Market** - Day trip ke Damnoen Saduak Floating Market atau Maeklong Railway Market (pasar atas landasan keretapi).
    * **Day 6: Chatuchak Quest** - (Hujung minggu sahaja) Shopping sampai lebam kat pasar terbesar dunia, Chatuchak Market.
    * **Day 7: Last Minute & Departure** - Massage terakhir di Let's Relax, beli ole-ole di Big C Supercenter, dan ke airport.
    """,
    "Phuket": """
    * **Day 1: Patong Landing** - Arrive at Phuket, stroll around Patong Beach, and explore Bangla Road at night.
    * **Day 2: Island Adventure** - Full day boat trip to Phi Phi Islands, Maya Bay, and snorkeling at Pileh Lagoon.
    * **Day 3: Old Town Charm** - Explore Phuket Old Town (bangunan warna-warni), visit Sunday Walking Street Market.
    * **Day 4: Big Buddha & Viewpoints** - Visit Big Buddha, Karon Viewpoint, and sunset dinner at Promthep Cape.
    * **Day 5: Elephants & Nature** - Visit Phuket Elephant Sanctuary (ethical experience) and chill at Kata Beach.
    * **Day 6: James Bond Island** - Kayaking trip at Phang Nga Bay and visit the famous floating village, Koh Panyee.
    * **Day 7: Relax & Fly** - Last dip at the beach, souvenir shopping in Phuket Town, and head to HKT airport.
    """,
    "Danang": """
    * **Day 1: Dragon Bridge Arrival** - Check-in, visit Dragon Bridge (tengok dia hembus api malam minggu), and My Khe Beach.
    * **Day 2: Ba Na Hills Quest** - Full day trip to Golden Bridge (Hands Bridge) and French Village via cable car.
    * **Day 3: Marble Mountains** - Explore caves and temples inside Marble Mountains, then head to Hoi An in the evening.
    * **Day 4: Ancient Hoi An** - Walk through the Ancient Town, try the famous Banh Mi Phuong, and take a lantern boat ride.
    * **Day 5: My Son Sanctuary** - Half-day trip to the ancient ruins of Champa Kingdom, then back to Danang for seafood.
    * **Day 6: Son Tra Peninsula** - Visit Lady Buddha (Linh Ung Pagoda) and drive up to the Intercontinental area for views.
    * **Day 7: Han Market Shopping** - Last minute shopping for coffee & snacks at Han Market before heading home.
    """
}

# 6. TABS (QUEST LOG & JOURNAL)
tab1, tab2 = st.tabs(["📜 DETAILED ITINERARY", "✍️ WRITER'S NOTES"])

with tab1:
    st.markdown(f"### 🏁 7-Day Quest Log: {destinasi}")
    st.info(itineraries[destinasi])

with tab2:
    st.header("📓 Writer's Secret Journal")
    nota = st.text_area("Record your thoughts here...", height=250, placeholder="Inspirasi bab baru...")
    if st.button("SAVE ENTRY"):
        st.success("Entry added to the archives!")
        st.markdown(f"**Last Entry:** {nota}")

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.write("v1.0 Goji-Travel-Pro")