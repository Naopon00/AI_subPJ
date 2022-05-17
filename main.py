import streamlit as st
import time

st.title("streamlit 入門")
st.write("プレグレスバーの表示")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration { i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'
# option = st.selectbox(
#     'あなたの好きな数字を教えてください.',
#     list(range(1,11))
# )

# 'あなたの好きな数字は', option, 'です.'
left_column, right_column = st.columns(2)

button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
# text = st.text_input('あなたの趣味を教えてください.')
# 'あなたの趣味は', text, 'です'

# condition = st.slider('あなたの今の調子は?', 0, 100, 50)#変数　最小値、最大値、デフォルト
# 'コンディション:', condition

# if st.checkbox("Show Image"):
#     img = Image.open('sample.jpg')
#     st.image(img, caption = 'MotorBike', use_column_width = True)

#df = pd.DataFrame(
#    np.random.rand(100,2)/ [50, 50] + [35.69, 139.70],
#    columns=['lat','lon']
#)

#st.map(df)