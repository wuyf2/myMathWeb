import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.subheader('函数类型：')

# Store the initial value of widgets in session state
if 'funcType' not in st.session_state:
    st.session_state.funcType = None

col1, col2 = st.columns(2)

with col1:

    rd1 = st.radio(
        label="选择函数类型， 👇",
        options=["线性函数", "正弦函数", "余弦函数", "正切函数",
        "幂函数", "指数函数", "对数函数", "心形函数"],
        key='funcType'
        # label_line=st.session_state.line,
    )

# with col2:

#     st.checkbox("Disable radio widget", key="disabled")
#     st.checkbox("Orient radio options horizontally", key="horizontal")

st.divider()
def plot(x:float, y:float, title:str, xmin=-10, xmax=10, ymin=-10, ymax=10, subplot_kw=None)->None:

    fig, ax = plt.subplots(subplot_kw=subplot_kw)
    ax.plot(x, y)
    ax.set(xlabel='X', ylabel='Y',
        title= title)
    ax.set_xlim(xmin=xmin, xmax=xmax)
    ax.set_ylim(ymin=ymin, ymax=ymax)
    ax.grid(True)
    st.pyplot(fig)

def linePlot(a, b)->None:
    title = 'y = ax + b'
    xx = np.linspace(-5, 5, 10, endpoint=True)
    yy = a*xx + b
    plot(xx, yy, title, xmin=-5, xmax=5, ymin=-30, ymax=30)

def sinPlot(a, b, c)->None:

    xx = np.linspace(-2*np.pi, 2*np.pi, 180, endpoint=True)
    yy = a*np.sin(b*xx + c)
    # data = {'x':xx,'y':yy}
    # dataFrame = pd.DataFrame(data=data)
    # st.line_chart(dataFrame, x='x', y = 'y')
    plot(xx, yy, title='y=Asin(ωx+φ)', xmin=-2*np.pi, xmax=2*np.pi, ymin=-5, ymax=5)

def cosPlot(a, b, c)->None:

    xx = np.linspace(-2*np.pi, 2*np.pi, 180, endpoint=True)
    yy = a*np.cos(b*xx + c)
    # data = {'x':xx,'y':yy}
    # dataFrame = pd.DataFrame(data=data)
    # st.line_chart(dataFrame, x='x', y = 'y')
    plot(xx, yy, title='y=Acos(ωx+φ)', xmin=-2*np.pi, xmax=2*np.pi, ymin=-5, ymax=5)
def powerData(a, x0, y0)->None:

    xx = np.linspace(-10, 10, 200, endpoint=True)
    yy = np.power(xx+x0, a) + y0

    plot(xx, yy, title='y=(x+X0)^a + Y0', xmin=-10, xmax=10, ymin=-20, ymax=20)
def expData(a)->None:

    xx = np.linspace(-10, 10, 200, endpoint=True)
    yy = np.power(a, xx)
    plot(xx, yy, title='y=a^x', xmin=-10, xmax=10, ymin=-20, ymax=20)
def logData(a)->None:

    xx = np.linspace(0.00001, 10, 500, endpoint=True)
    yy = np.log(xx) / np.log(a)

    plot(xx, yy, title='y=log(a, x)', xmin=0, xmax=10, ymin=-20, ymax=20)
def heartShapedData(a):
    theta = np.linspace(0, 2*np.pi, 360, endpoint=True)
    r = a*(1-np.sin(theta))
    st.write("笛卡尔与瑞典公主的故事：")
    plot(theta, r, title='r=a(1-sin(theta))', xmin=0, xmax=2*np.pi, ymin=0, ymax=10, subplot_kw={'projection': 'polar'})
def tanPlot()->None:

    theta = np.linspace(-np.pi/2, np.pi/2, 1800, endpoint=False)
    theta = theta[1:]
    y = np.tan(theta)
    plot(theta, y, title='y=tan(x)', xmin=-np.pi/2, xmax=np.pi/2, ymin=-1000, ymax=1000)
if st.session_state.funcType == '线性函数':
    # y=ax+b
    a = st.slider(label='斜率, a', min_value=-5, max_value=5,value=1 )
    b = st.slider(label='截距, b', min_value=-5, max_value=5, value=0)
    st.divider() 
    linePlot(a, b)  
if st.session_state.funcType == '正弦函数':
    # y=Asinx + b
    A = st.slider('幅值，A', min_value=-5.0, max_value=5.0, value=1.0)
    omg = st.slider('圆频率，ω', min_value=0.0, max_value=2*np.pi, value=1.0)
    ph = st.slider('相位，ψ', min_value=-np.pi, max_value=np.pi, value=0.0)
    st.divider() 
    sinPlot(A, omg, ph)
if st.session_state.funcType == '余弦函数':
    # y=Acosx + b
    A = st.slider('幅值，A', min_value=-5.0, max_value=5.0, value=1.0)
    omg = st.slider('圆频率，ω', min_value=0.0, max_value=2*np.pi, value=1.0)
    ph = st.slider('相位，ψ', min_value=-np.pi, max_value=np.pi, value=0.0)
    st.divider() 
    cosPlot(A, omg, ph)
if st.session_state.funcType == '正切函数':
    # y=tan(x)
    st.write('y=tan(x), x(-pi/2, pi/2)')

    # A = st.slider('幅值，A', min_value=-5.0, max_value=5.0, value=1.0)
    # omg = st.slider('圆频率，ω', min_value=0.0, max_value=2*np.pi, value=1.0)
    # ph = st.slider('相位，ψ', min_value=-np.pi, max_value=np.pi, value=0.0)
    st.divider() 
    tanPlot()

if st.session_state.funcType == '幂函数':
    # y=x^a
    # 指数为小数的时候，存在bug
    a = st.slider('指数，a', min_value=1, max_value=5, value=1)
    x0 = st.slider('X0', min_value=-5, max_value=5, value=0)
    y0 = st.slider('Y0', min_value=-5, max_value=5, value=0)
    st.divider() 
    powerData(a, x0, y0)    

if st.session_state.funcType == '指数函数':
    # y=a^x
    a = st.slider('底数，a', min_value=0.00001, max_value=5.0, value=0.5)
    st.divider() 
    expData(a)
if st.session_state.funcType == '对数函数':
    # y=logx
    a = st.slider('底数，a', min_value=0.00001, max_value=5.0, value=0.5)
    st.divider() 
    logData(a)
if st.session_state.funcType == '心形函数':
    # r=a(1-sin(theta))
    a = st.slider('放大系数，a', min_value=1, max_value=5, value=1)
    st.divider() 
    heartShapedData(a)