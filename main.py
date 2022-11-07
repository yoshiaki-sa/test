import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)


"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


left_column, rigth_column = st.beta_columns(2)
button = left_column.button('右カラム')
if button:
    rigth_column.write('aaaa')

expander = st.beta_expander('問い合わせ')

if st.checkbox('show Image'):
    img = Image.open('test.png')
    st.image(img, caption='Kohe Imanishi', use_column_width=True)

option = st.selectbox(
    'あなたの数字をえらんでください',
    list(range(1, 11))
)

'あなたの好きな数字は', option, 'です'

option2 = st.text_input('趣味を教えて下さい')
'あなたの趣味は', option2, 'です'

condition = st.slider('Conditon', 0, 100, 100)
'condition', condition
