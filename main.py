import streamlit as st
import time

st.title('Streamlil 超入門')
st.write('プログレスバーの表示')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Itaration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

st.write('Done!!')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問合せ内容を書く')