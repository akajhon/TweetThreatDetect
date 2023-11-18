import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
from LoadModel import limpezaTweet
from TrainModel import extrairDados
from streamlit_option_menu import option_menu
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#with st.sidebar:
#    selected = option_menu(
#        menu_title=None,
#        options=["Threat Analysis", "Database Analysis"],
#        orientation="horizontal",
#    )
    
def main():

    st.title("Sentiment Analysis")
    
    input_text = st.text_input("Digite uma frase:")
    if input_text != "":
        #Limpando antes de fazer a extração
        limpezaTweet(input_text)
        sentiment , recognized_entities, average_prediction , positive_probability , negative_probability , percent_similarity, prob_threat, prob_percent = extrairDados(input_text)
        prob_percent = prob_percent * 100
        if prob_threat == 1:
            st.success("A frase não representa uma ameaça", icon="✅")
        elif prob_threat == 0:
            st.error("A frase representa uma ameaça", icon="🚨")
        else:
            st.warning(sentiment, icon="⚠️")

        positive_probability = round(positive_probability, 3)
        negative_probability = round(negative_probability,3)
        percent_similarity = round(percent_similarity,3)
        entities = [entity[1] for entity in recognized_entities]
        words = [entity[0] for entity in recognized_entities]

        # Definindo as categorias e seus respectivos textos para as legendas
        labels = ['É ameaça', 'Não é ameaça']
        values = [prob_percent, 100 - prob_percent]

        # Criando o gráfico de pizza com Plotly
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

        # Personalizando o layout do gráfico
        fig.update_traces(textinfo="percent", hole=0.3)

        # Personalizando o layout do gráfico
        fig.update_layout(
            title="Probabilidade de representar uma ameaça",
            xaxis_title="",
            yaxis_title="Porcentagem",
            showlegend=True
        )

        # Exibindo o gráfico
        st.plotly_chart(fig)

        data = pd.DataFrame({
            'Sentimento': ['Positivo', 'Negativo'],
            'Porcentagem': [positive_probability, negative_probability]
        })

        # Mapeamento de cores para sentimentos
        colors = {
            'Positivo': 'green',
            'Negativo': 'red'
        }

        # Adicione uma coluna "Cor" ao DataFrame
        data['Cor'] = data['Sentimento'].map(colors)

        # Crie um gráfico de barras com plotly.graph_objects
        fig = go.Figure(data=[
            go.Bar(
                x=data['Sentimento'],
                y=data['Porcentagem'],
                marker_color=data['Cor'],
                text=data['Porcentagem'],
                textposition='auto'
            )
        ])

        # Personalizar o layout do gráfico
        fig.update_layout(
            xaxis_title='',
            yaxis_title='Porcentagem',
            title_text='Porcentagem de sentimento',
            showlegend=False  # Ocultar a legenda
        )

        # Exibir o gráfico
        st.plotly_chart(fig)
        
        st.write("Gráfico de palavras reconhecidas das Entidades")

        # Criar um gráfico de pizza com Plotly
        fig = go.Figure()

        # Adicionar as palavras no gráfico
        fig.add_trace(go.Pie(labels=words))

        # Personalize o layout do gráfico
        fig.update_traces(textinfo="percent+label", pull=[0.1], hole=0.3)

        # Exibir o gráfico
        st.plotly_chart(fig)
        
        st.write("Gráfico de Entidades reconhecidas")

        # Criar um gráfico de pizza com Plotly
        fig = go.Figure()

        # Adicionar as palavras no gráfico
        fig.add_trace(go.Pie(labels=entities))

        # Personalize o layout do gráfico
        fig.update_traces(textinfo="percent+label", pull=[0.1], hole=0.3)

        # Exibir o gráfico
        st.plotly_chart(fig)
                
        percent_similarity_percent = percent_similarity * 100

        data = {"Cibersegurança": ["Similaridade"], "Percentagem": [percent_similarity_percent]}
        df = pd.DataFrame(data)

        # Crie o gráfico de barras com Plotly
        fig = px.bar(df, x="Cibersegurança", y="Percentagem", text="Percentagem")

        # Personalize o layout do gráfico
        fig.update_layout(
            title="Similaridade com Termos de Cibersegurança",
            xaxis_title="Cibersegurança",
            yaxis_title="Percentagem",  # Deixe apenas "Percentagem" no título do eixo Y
            showlegend=False,  # Ocultar a legenda
        )

        # Formate o rótulo de texto no gráfico para incluir "%"
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")

        # Exiba o gráfico
        st.plotly_chart(fig)

main()
