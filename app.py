# -*- coding: utf-8 -*-
import streamlit as st
import requests
import json

# -----------------------------------
# تحميل بيانات الجدول الدوري الرسمية
# -----------------------------------

URL = "https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json"
elements = requests.get(URL).json()["elements"]

# -----------------------------------
# تحميل أماكن الوجود في الطبيعة من ملف خارجي
# -----------------------------------

with open("pp.json", "r", encoding="utf-8") as f:
    occurrence_data = json.load(f)

# -----------------------------------
# ترجمة عربي → إنجليزي
# -----------------------------------

arabic_to_english = {
    "هيدروجين":"hydrogen","هيليوم":"helium","ليثيوم":"lithium","بيريليوم":"beryllium",
    "بورون":"boron","كربون":"carbon","نيتروجين":"nitrogen","أكسجين":"oxygen","اوكسجين":"oxygen",
    "فلور":"fluorine","نيون":"neon","صوديوم":"sodium","مغنيسيوم":"magnesium","ألمنيوم":"aluminum",
    "المنيوم":"aluminum","سيليكون":"silicon","فوسفور":"phosphorus","كبريت":"sulfur","كلور":"chlorine",
    "أرجون":"argon","بوتاسيوم":"potassium","كالسيوم":"calcium","حديد":"iron","نحاس":"copper",
    "فضة":"silver","ذهب":"gold","زئبق":"mercury","رصاص":"lead","يورانيوم":"uranium",
    "أوغانيسون":"oganesson"
}

# -----------------------------------
# إعداد الصفحة
# -----------------------------------

st.set_page_config("العناصر الكيميائية", "🧪", layout="centered")
st.title("🔬 البحث عن عنصر كيميائي")

query = st.text_input("اكتب اسم العنصر (عربي / إنجليزي / رمز)")

# -----------------------------------
# البحث
# -----------------------------------

if query:
    q = query.strip().lower()

    if query in arabic_to_english:
        q = arabic_to_english[query]

    found = None
    for el in elements:
        if q == el["name"].lower() or q == el["symbol"].lower():
            found = el
            break

    if found:
        st.success("تم العثور على العنصر ✅")
        st.write(f"**الاسم:** {found['name']}")
        st.write(f"**الرمز:** {found['symbol']}")
        st.write(f"**العدد الذري:** {found['number']}")
        st.write(f"**الكتلة الذرية:** {found['atomic_mass']}")
        st.write(f"**التصنيف:** {found['category']}")
        st.write(f"**المجموعة:** {found.get('group','—')}")
        st.write(f"**الدورة:** {found['period']}")

        symbol = found["symbol"]
        occ = occurrence_data.get(symbol, "لا توجد بيانات حالياً.")
        st.write(f"**أماكن وجوده في الطبيعة:** {occ}")

    else:
        st.error("العنصر غير موجود ❌")

# -----------------------------------
# زر صورة الجدول الدوري
# -----------------------------------

st.markdown("---")

if st.button("🖼️ عرض صورة الجدول الدوري"):
    st.image(
        "periodic_table.png",
        caption="الجدول الدوري",
        use_container_width=True
    )

# -----------------------------------
# التوقيع
# -----------------------------------

st.markdown("---")
st.markdown(
    """
    <div style="text-align:center;">
        <h4>الاسم: يوسف</h4>
        <h4>الصف: عاشر "ب"</h4>
    </div>
    """,
    unsafe_allow_html=True
)
