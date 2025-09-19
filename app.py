import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello World...")

# df = pd.DataFrame({"A": [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

# st.write("Random Dataset")
# st.write(df)

# st.write('st.table:')
# st.table(df)

# st.write("st.dataframe")
# st.dataframe(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
 )
st.write("Chart data:")
st.write(chart_data)
st.line_chart(chart_data)

st.write("st.area_chart: ")
st.area_chart(chart_data)

st.write("st.bar_chart:")
st.bar_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [52.52 , 13.405],
    columns=['lat', 'lon']
)
st.write("st.map")
st.map(map_data)

tabs = st.tabs(['charts', 'help'])

# with tabs[0]:
#     st.header('Charts')
#     st.write("This is the help tab")
col1, col2 = st.columns(2)
with col1:
    with st.expander("Function settings"):
        x = np.linspace(0, np.pi * 2, 100)
        t = st.slider("t", 0.0, 10.0, 1.0)
        x0 = st.slider("x0", 0.0, np.pi *2, 0.0)
        y = np.sin(x*t+x0)

        function_name = st.selectbox("Function", ["sin", "cos", "tan"])
        function_dict = {"sin": np.sin, "cos": np.cos, "tan": np.tan}

        # if st.checkbox("show line chart: "):
        #    st.line_chart(pd.DataFrame({"sin(x*t+x0)": y}))

with col2:
        if st.checkbox("show line chart: ", True):
            y = function_dict[function_name](x*t+x0)
            st.line_chart(pd.DataFrame({f"{function_name}(x*t+x0)": y}))