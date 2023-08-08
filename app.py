import networkx as nx
import pandas as pd
import numpy as np
from pyvis.network import Network
from collections import defaultdict
import random
import json
import streamlit as st
import streamlit.components.v1 as components


st.title('Members Network')

with open('Mems Network.html', 'r') as f:
	html_content = f.read()
	components.html(html_content, height = 1200, width = 1200)