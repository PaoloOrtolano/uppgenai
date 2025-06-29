import streamlit as st
import pandas as pd
import openai
import os
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI as PandasAI_OpenAI

# === CONFIGURAZIONE ===
st.set_page_config(page_title="UPP + GenAI", layout="wide")
st.title("📊 UPP + GenAI - Domande Libere sui Dati")

# === API KEY ===
API_KEY = "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"
os.environ["OPENAI_API_KEY"] = API_KEY
llm = PandasAI_OpenAI(api_token=API_KEY)

# === CARICAMENTO DATI ===
@st.cache_data
def load_data():
    df = pd.read_csv("analisi_upp.csv", encoding="ISO-8859-1", sep=";")
    df = df[df["Semestre"].str.contains("II", na=False)]
    df = df[["Distretto", "tipo ufficio", "CR", "definiti per addetto", "numero addetti", "modello organizzativo", "tipo sezione"]]
    return df.dropna()

df = load_data()
sdf = SmartDataframe(df, config={"llm": llm})

# === INTERFACCIA ===
st.markdown("Fai una domanda libera: l'AI interrogherà direttamente i dati UPP completi.")
prompt = st.text_area("Scrivi la tua domanda", "Quali sono i 10 uffici più produttivi?")

if st.button("Invia domanda all'AI"):
    try:
        risposta = sdf.chat(prompt)
        st.success("✅ Risposta AI:")
        st.write(risposta)
    except Exception as e:
        st.error(f"Errore: {e}")
import streamlit as st
import pandas as pd
import openai
import os
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI as PandasAI_OpenAI

# === CONFIGURAZIONE ===
st.set_page_config(page_title="UPP + GenAI", layout="wide")
st.title("📊 UPP + GenAI - Domande Libere sui Dati")

# === API KEY ===
API_KEY = "sk-INSERISCI-LA-TUA-CHIAVE-QUI"
os.environ["OPENAI_API_KEY"] = API_KEY
llm = PandasAI_OpenAI(api_token=API_KEY)

# === CARICAMENTO DATI ===
@st.cache_data
def load_data():
    df = pd.read_csv("analisi_upp.csv", encoding="ISO-8859-1", sep=";")
    df = df[df["Semestre"].str.contains("II", na=False)]
    df = df[["Distretto", "tipo ufficio", "CR", "definiti per addetto", "numero addetti", "modello organizzativo", "tipo sezione"]]
    return df.dropna()

df = load_data()
sdf = SmartDataframe(df, config={"llm": llm})

# === INTERFACCIA ===
st.markdown("Fai una domanda libera: l'AI interrogherà direttamente i dati UPP completi.")
prompt = st.text_area("Scrivi la tua domanda", "Quali sono i 10 uffici più produttivi?")

if st.button("Invia domanda all'AI"):
    try:
        risposta = sdf.chat(prompt)
        st.success("✅ Risposta AI:")
        st.write(risposta)
    except Exception as e:
        st.error(f"Errore: {e}")

