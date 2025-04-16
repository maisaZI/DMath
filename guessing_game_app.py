# -*- coding: utf-8 -*-
"""guessing_game_app"""

import streamlit as st

def binary_search_guess(low, high, feedback_func):
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        feedback = feedback_func(mid)

        if feedback == "correct":
            return mid, steps
        elif feedback == "higher":
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps

st.title("🤖 هل الذكاء الاصطناعي يقدر يخمن رقمك؟!")

st.write("اختر رقمًا بين 1 و100 في ذهنك، وسأحاول تخمينه!")

if st.button("ابدأ التخمين!"):
    st.session_state["start"] = True
    st.session_state["low"] = 1
    st.session_state["high"] = 100
    st.session_state["step"] = 0

if "start" in st.session_state and st.session_state["start"]:
    if "mid" not in st.session_state or st.button("التالي"):
        st.session_state["mid"] = (st.session_state["low"] + st.session_state["high"]) // 2
        st.session_state["step"] += 1

    st.subheader(f"هل الرقم هو {st.session_state['mid']}؟")
    col1, col2, col3 = st.columns(3)

    if col1.button("📉 أصغر"):
        st.session_state["high"] = st.session_state["mid"] - 1
    if col2.button("✅ صحيح!"):
        st.success(f"وجدته! الرقم هو {st.session_state['mid']} بعد {st.session_state['step']} محاولة 👏")
        st.session_state["start"] = False
    if col3.button("📈 أكبر"):
        st.session_state["low"] = st.session_state["mid"] + 1
