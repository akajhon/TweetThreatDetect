import streamlit as st
st.title("Database Analysis")

st.markdown(
    """
    <style>
    [style*="--aspect-ratio"] > :first-child {
    width: 100%;
    }

    [style*="--aspect-ratio"] > img {  
    height: auto;
    }

    @supports (--custom:property) {
    [style*="--aspect-ratio"] {
        position: relative;
        display: flex;
        justify-content: center; /* Adiciona centralização horizontal */
        align-items: center; /* Adiciona centralização vertical */
    }
    
    [style*="--aspect-ratio"]::before {
        content: "";
        display: block;
        padding-bottom: calc(100% / (var(--aspect-ratio)));
    }
    
    [style*="--aspect-ratio"] > :first-child {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
    }  
    }
    </style>
    <br><br>
    <div style="--aspect-ratio: 16/9;">
    <iframe title="TCC" width="1000" height="750"  src="https://app.powerbi.com/view?r=eyJrIjoiZmM4ZDU0M2YtMzIzYi00ZGZlLTkxZWMtZjBhNTc2YzM3NDQxIiwidCI6ImZkYzJlZjNkLWEzZDEtNDA1OC1hOTA4LTAxMWMxMTcxZTYxNiJ9" frameborder="0" allowFullScreen="true"></iframe>
    </div>""",
    unsafe_allow_html=True
)