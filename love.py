import streamlit as st
from time import sleep

st.set_page_config(page_title="Письмо любви 💌", page_icon="💌", layout="centered")

st.title("💌 С праздником")
st.write("Нажимай на кнопки ниже, чтобы прочитать письмо по строчкам. Каждое нажатие — шаг ближе к сердцу ✨")

# Список строчек письма
love_lines = [
    "Привет, попашка... ❤️",
    "Я давно хотел сказать тебе кое-что важное...",
    "Каждый день с тобой — как страница самой прекрасной книги.",
    "Ты умеешь сделать мой день просто улыбкой. 😌",
    "Спасибо, что ты есть в моей жизни.",
    "Ты — вдохновение, покой и радость в одном человеке.",
    "С тобой я чувствую себя настоящим.",
    "Я люблю тебя. Без условий. Просто так. Всей душой. 💖"
]

# Сессия для отслеживания прогресса
if 'step' not in st.session_state:
    st.session_state.step = 0

# Кнопка следующей строки
if st.session_state.step < len(love_lines):
    if st.button("Показать следующую строку ✨"):
        st.session_state.step += 1
        sleep(0.5)

# Отображение уже открытых строк
for i in range(st.session_state.step):
    st.markdown(f"**{love_lines[i]}**")

# Финальное послание
if st.session_state.step == len(love_lines):
    st.balloons()
    st.success("Письмо окончено, но чувства бесконечны 💕")
