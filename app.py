import pandas as pd 
import plotly.express as px
import streamlit as st


st.set_page_config(page_title = "Astroport vs Terraswap",
					page_icon = ":bar_chart:",
					layout =  "wide")

df = pd.read_excel("dex_apr2022.xlsx",0)

	#io="dex_apr2022.xlsx",
	#enginer='openpyxl',
	#sheet_name = 'dex',
	#skiprows=1,
	#usecols = 'A:E',
	#nrows= 218
	#)

#print(df) # to run this, go to cd /users/sam/desktop/dex_april_2022, then python3 app.py

#st.dataframe(df) # this shows the table list 

#side bar for users to customize stuff 
st.sidebar.header("Filter here:")
dex = st.sidebar.multiselect(
	"Select Dex:",
	options=df["DEX"].unique(),
	default=df["DEX"].unique()
	)

month = st.sidebar.multiselect(
	"Select Month:",
	options=df["MONTH"].unique(),
	default=df["MONTH"].unique()
	)

df_selection = df.query(
	"DEX == @dex & MONTH ==@month"
	)

#st.dataframe(df_selection)

#mainpage 

st.title("Astroport vs Terraswap")

st.markdown("---")
st.header(":sunny: Overview Stats")

#Overview big numbers stats 
swap_volume = int(df_selection["VOLUME_TRADED_USD"].sum())
swap_count = int(df_selection["SWAP_TRANSACTIONS"].sum())
trader_count = int(df_selection["TRADERS"].sum())


col1, col2, col3 = st.columns(3)
with col1:
	st.subheader("Swap Volume")
	st.subheader(f"${swap_volume:,}")

with col2:
	st.subheader("Swap Transactions")
	st.subheader(f"{swap_count:,}")

with col3:
	st.subheader("Number of Traders")
	st.subheader(f"{trader_count:,}")


st.markdown("---")
st.header(":mag_right: Daily Stats")

fig_daily_swap_volume = px.bar(
	df_selection,
	x = 'DAY',
	y = 'VOLUME_TRADED_USD',
	color = 'DEX',
	title="<b>Daily Swap Volume</b>",
	hover_data=['DAY', 'VOLUME_TRADED_USD'],
	width = 1000,
	height = 500,
	)

fig_swap_count = px.line(
	df_selection,
	x = 'DAY',
	y = 'SWAP_TRANSACTIONS',
	color = 'DEX',
	title="<b>Daily Swap Count</b>",
	hover_data=['DAY', 'SWAP_TRANSACTIONS'],
	width = 1000,
	height = 500,
	)

fig_daily_traders = px.line(
	df_selection,
	x = 'DAY',
	y = 'TRADERS',
	color = 'DEX',
	title="<b>Daily Trader Count</b>",
	hover_data=['DAY', 'TRADERS'],
	width = 1000,
	height = 500,
	)

st.plotly_chart(fig_daily_swap_volume)
st.plotly_chart(fig_swap_count)
st.plotly_chart(fig_daily_traders)

st.markdown("---")
st.header("Raw Data")
st.dataframe(df_selection)
























