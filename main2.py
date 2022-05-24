import streamlit as st
import random
import time

st.title("写真を撮れるサイト")
latest_iteration = st.empty()
bar = st.progress(0)


st.sidebar.write('プログレスバーの設定')
speed = st.sidebar.slider('プログレスバーの速さ', 0.0, 1.0, 0.1)
start_button = st.sidebar.button("実行する")
random_button = st.sidebar.button("ランダムにバーを動かす")
real_random_button = st.sidebar.button("めっちゃランダム")
balloon = st.sidebar.button("風船を表示")
if balloon:
    st.balloons()

st.sidebar.write("じゃんけん")
hands = ['グー', 'チョキ', 'パー']
option = st.sidebar.selectbox(
    'じゃんけんの手',
    hands
)
myhand = 0
for l in range(3):
    if option == hands[l]:
        myhand = l

handbutton = st.sidebar.button('じゃんけんをする')
if handbutton:
    hand = random.randint(0, 2)
    if myhand == hand:
        st.sidebar.write("CPUの手：", hands[hand])
        st.sidebar.write('あいこです')
    elif myhand == 0 and hand == 1:
        st.sidebar.write("CPUの手：", hands[hand])
        st.sidebar.write("あなたの勝ちです")
    elif myhand == 0 and hand == 2:
        st.sidebar.write("CPUの手：", hands[hand])
        st.sidebar.write("あなたの負けです")
    elif myhand == 1 and hand == 0:
        st.sidebar.write("CPUの手：", hands[hand])
        st.sidebar.write("あなたの負けです")
    elif myhand == 1 and hand == 2:
        st.sidebar.write("CPUの手：", hands[hand])
        st.sidebar.write("あなたの勝ちです")
    elif myhand == 2 and hand == 0:
        st.sidebar.write("CPUの手：", hands[hand])
        st.sidebar.write("あなたの勝ちです")
    elif myhand == 2 and hand == 1:
        st.sidebar.write("CPUの手：", hands[hand])
        st.sidebar.write("あなたの負けです")

if start_button:
    bar.progress(0)
    for i in range(100):
        latest_iteration.text(f'Iteration { i + 1}')
        bar.progress(i + 1)
        time.sleep(speed)
    'Done!'

if real_random_button:
    bar.progress(0)
    while True:
        a = random.randint(0, 100)
        latest_iteration.text(f'Iteration {a}')
        bar.progress(a)
        if a >= 100:
            bar.progress(100)
            break
        time.sleep(speed)
    'Done!'

if random_button:
    i = 0
    while True:
        latest_iteration.text(f'Iteration { i + 2}')
        a = random.randint(0, 100)
        if a >= 50:
            if i + 10 >= 100:
                bar.progress(100)
                latest_iteration.text(f'Iteration {100}')
                break
            else:
                bar.progress(i + 2)
                i += 2
        elif a >= 10 and i >= 10:
            bar.progress(i - 3)
            i -= 2
        else:
            if i + 5 >= 100:
                bar.progress(100)
                latest_iteration.text(f'Iteration {100}')
                break
            else:
                bar.progress(i + 5)
                i += 5
        time.sleep(speed)

    'Done!!!'

check = st.checkbox("写真を取る")
if check:
    picture = st.camera_input("Take a picture")
    if picture:
        st.balloons()
        st.image(picture)
        with open("photo.png", "w") as file:
            btn = st.download_button(
                label = "Download image",
                data = picture,
                file_name = "photo.png",
                mime = "image/png"
            )

left_column, right_column = st.columns(2)
l_button = left_column.button("右側に文字を表示")
if l_button:
    right_column.write("このように表示されます")

expander = st.expander("使い方")
expander.write("1.「写真を撮る」にチェックを入れる")
expander.write("2.お好きなタイミングで「Take Photo」をクリック！")
expander.write("3.「Download Image」をクリックするとダウンロードできます")
expander.write("4.「Clear Photo」をクリックすると撮り直す事ができます")