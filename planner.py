import streamlit as st

# 1. SETUP PAGE
st.set_page_config(page_title="Goji Travel Planner", page_icon="🗺️", layout="wide")

# 2. THE ULTIMATE CSS FIX (ANTI-GLITCH)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
    .stApp { background-color: #0e1117; }

    h1, h2, h3, h4, p, label, li, [data-testid="stMetricValue"], [data-testid="stMetricLabel"], span:not(:has(svg)) {
        font-family: 'VT323', monospace !important;
        color: #ffffff !important;
    }

    [data-testid="stIcon"], svg, i, .material-icons {
        font-family: inherit !important;
        display: inline-block !important;
    }

    h1 { color: #f1c40f !important; font-size: 55px !important; text-shadow: 3px 3px #000000; }
    [data-testid="stSidebar"] { background-color: #1e2129 !important; border-right: 1px solid #3498db; }
    [data-testid="stMetricValue"] { color: #f1c40f !important; font-size: 45px !important; }

    .stButton>button {
        background-color: #3498db !important;
        color: white !important;
        border-radius: 5px !important;
        font-family: 'VT323', monospace !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR (SETTINGS & CONVERTER)
with st.sidebar:
    st.header("⚙️ SETTINGS")
    destinasi = st.selectbox("DESTINATION:", ["Bangkok", "Phuket", "Danang"])
    
    st.divider()
    st.subheader("💰 CURRENCY CONVERTER")
    amount_myr = st.number_input("MYR AMOUNT:", value=100)
    rates = {"Bangkok": 7.50, "Phuket": 7.50, "Danang": 5200.0}
    curr_name = {"Bangkok": "THB", "Phuket": "THB", "Danang": "VND"}
    converted = amount_myr * rates[destinasi]
    st.success(f"Estimate: {converted:,.2f} {curr_name[destinasi]}")
    
    st.divider()
    hari = st.slider("DAYS:", 1, 14, 7)
    hotel = st.number_input("HOTEL/NIGHT (RM):", value=150)
    makan = st.number_input("MEAL/DAY (RM):", value=80)
    
    harga_tiket = {"Bangkok": 450, "Phuket": 380, "Danang": 650}
    tiket = harga_tiket[destinasi]

# 4. MAIN CONTENT
st.title("🗺️ GOJI TRAVEL PLANNER")

total_kos = (hari * hotel) + (hari * makan) + tiket
c1, c2, c3 = st.columns(3)
c1.metric("FLIGHT", f"RM{tiket}")
c2.metric("TOTAL BUDGET", f"RM{total_kos}")
c3.metric("DURATION", f"{hari} DAYS")

st.divider()

# 5. ITINERARY DATABASE (FULL & LONG)
itineraries = {
    "Bangkok": """
    * **Day 1: Arrival & Night Vibe** - Check-in hotel, dinner at Jodd Fairs Night Market (cuba Volcanic Ribs!).
    * **Day 2: Culture & History** - Visit Grand Palace, Wat Pho (Reclining Buddha), and cross the river to Wat Arun for sunset.
    * **Day 3: Shopping Spree** - Full day at Siam Paragon, MBK Center, and CentralWorld. Malam pergi Chinatown (Yaowarat) untuk street food.
    * **Day 4: Cafe Hopping & Ari** - Explore kawasan Ari yang tenang, banyak cafe aesthetic untuk 'Writer's Inspiration'.
    * **Day 5: Floating Market** - Day trip ke Damnoen Saduak Floating Market atau Maeklong Railway Market.
    * **Day 6: Chatuchak Quest** - Shopping sampai lebam kat pasar terbesar dunia, Chatuchak Market.
    * **Day 7: Last Minute & Departure** - Massage terakhir di Let's Relax, beli ole-ole di Big C, dan ke airport.
    """,
    "Phuket": """
    * **Day 1: Patong Landing** - Arrive at Phuket, stroll around Patong Beach, and explore Bangla Road at night.
    * **Day 2: Island Adventure** - Full day boat trip to Phi Phi Islands, Maya Bay, and snorkeling at Pileh Lagoon.
    * **Day 3: Old Town Charm** - Explore Phuket Old Town (bangunan warna-warni), visit Sunday Walking Street Market.
    * **Day 4: Big Buddha & Viewpoints** - Visit Big Buddha, Karon Viewpoint, and sunset dinner at Promthep Cape.
    * **Day 5: Elephants & Nature** - Visit Phuket Elephant Sanctuary and chill at Kata Beach.
    * **Day 6: James Bond Island** - Kayaking trip at Phang Nga Bay and visit floating village, Koh Panyee.
    * **Day 7: Relax & Fly** - Last dip at the beach, souvenir shopping in Phuket Town, and head home.
    """,
    "Danang": """
    * **Day 1: Dragon Bridge Arrival** - Check-in, visit Dragon Bridge, and My Khe Beach.
    * **Day 2: Ba Na Hills Quest** - Full day trip to Golden Bridge and French Village via cable car.
    * **Day 3: Marble Mountains** - Explore caves and temples, then head to Hoi An in the evening.
    * **Day 4: Ancient Hoi An** - Walk through the Ancient Town, try Banh Mi Phuong, and take a lantern boat ride.
    * **Day 5: My Son Sanctuary** - Half-day trip to the ancient ruins of Champa Kingdom, then back for seafood.
    * **Day 6: Son Tra Peninsula** - Visit Lady Buddha (Linh Ung Pagoda) and drive up for coastal views.
    * **Day 7: Han Market Shopping** - Last minute shopping for coffee & snacks at Han Market.
    """
}

# 6. TABS
tab1, tab2, tab3 = st.tabs(["📜 ITINERARY", "🎒 ULTIMATE CHECKLIST", "📓 JOURNAL"])

with tab1:
    st.info(itineraries[destinasi])

with tab2:
    st.header("🎒 The 30KG Luggage Checklist")
    st.warning("⚠️ JANGAN LUPA: UNIVERSAL ADAPTER! Belajar dari sejarah pahit Vietnam!")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("📁 Documents & Essentials")
        for item in ["Passport (Valid >6 months)", "Flight Ticket & E-Boarding Pass", "Hotel Booking Confirmation", "Travel Insurance (Hardcopy)", "International Driving License", "Cash (VND/THB) & Debit Card (Activated)"]:
            st.checkbox(item)
            
        st.subheader("🔌 Electronics & Tech")
        for item in ["Universal Travel Adapter", "Extension Wire (Sangat Penting!)", "Powerbank 20,000mAh", "Charging Cables & Wired Earphones", "Gimbal/Tripod for Sunset Photos"]:
            st.checkbox(item)

    with col_b:
        st.subheader("🧴 Toiletries & Skincare")
        for item in ["Skincare Kit (Niacinamide/Hydration)", "Sunscreen SPF 50++", "Toothbrush & Travel Size Toothpaste", "Wet Wipes & Hand Sanitizer", "Ubat-ubatan (Panadol/Minyak Angin)"]:
            st.checkbox(item)
            
        st.subheader("👕 Clothes & Misc")
        for item in ["7 Sets of Outfits", "Comfortable Walking Shoes", "Microfiber Towel", "Raincoat/Small Umbrella", "Empty Tupperware (Tapau Streetfood)", "Plastic Bags for Dirty Laundry"]:
            st.checkbox(item)

with tab3:
    nota = st.text_area("Writer's Secret Logs...", height=200, placeholder="Inspirasi dari sunset hari ini...")
    if st.button("SAVE ENTRY"):
        st.success("Log archived in the database!")