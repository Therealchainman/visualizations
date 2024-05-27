import streamlit as st
import streamlit.components.v1 as components
import pyautogui
from pathlib import Path
import pandas as pd
import numpy as np

# run with streamlit run directed_graph_viz.py

# Set header title
st.title('Network Graph Visualization of Constrained Directed Graph')

path = 'vis_htmls'
pages = {}
page_index = {}
pages_list = []
for i, file in enumerate(sorted(Path('.').glob(f'{path}/*.html'))):
    name = f'iteration/graph: {str(i).zfill(4)}'
    pages[name] = str(file)
    page_index[name] = i
    pages_list.append(name)

def open_page(page_name: str) -> None:
    index = str(page_index[page_name]).zfill(4)
    reach_matrix_path = f'vis_matrices/reach_{index}.npy'
    matrix = np.load(reach_matrix_path)
    # df = pd.DataFrame(matrix)
    st.table(matrix)
    st.header(page_name)
    htmlFile = open(pages[page_name], 'r', encoding = 'utf-8')
    components.html(htmlFile.read(), height=400, width = 400)

# create a button in the side bar that will move to the next page/radio button choice
next = st.sidebar.button('NEXT SLIDE')

choice = st.sidebar.radio("GO TO", tuple(sorted(pages.keys())))
if next:
    pyautogui.press("tab")
    pyautogui.press("down")
else:
    # finally get to whats on each page
    open_page(choice)
