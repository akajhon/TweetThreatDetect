# TweetThreatDetect

## Descrição
Este projeto implementa um sistema de detecção de ameaças cibernéticas em tweets usando técnicas avançadas de Processamento de Linguagem Natural (NLP) e análise de sentimentos. Ele visa identificar padrões relacionados a ameaças cibernéticas e avaliar a polaridade do sentimento dos tweets, auxiliando na prevenção e resposta a incidentes de segurança cibernética.

## Pré-Requisitos
- Python 3.x
- Bibliotecas Python: gensim, matplotlib, nltk, numpy, pandas, Pillow, plotly, scikit_learn, spacy, streamlit, streamlit_option_menu, tensorflow, tqdm, wordcloud
- Docker (opcional)

## Bibliotecas Python
Certifique-se de ter o pip instalado e, em seguida, execute o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt
```

## Como Executar
Este projeto pode ser executado de duas maneiras: via Docker ou por um script em shell.

### Via Docker
1. Clone o repositório:
   ```
   git clone https://github.com/seuprojeto/tweet-threat-detection.git
   ```
2. Navegue até o diretório do projeto:
   ```
   cd tweet-threat-detection
   ```
3. Construa a imagem Docker:
   ```
   docker build -t tweet-threat-detection .
   ```
4. Execute o container, adicionando a porta de execução (por exemplo, 8501):
   ```
   docker run -p 8501:8501 tweet-threat-detection
   ```

### Via Script em Shell
1. Clone o repositório:
   ```
   git clone https://github.com/seuprojeto/tweet-threat-detection.git
   ```
2. Navegue até o diretório do projeto:
   ```
   cd tweet-threat-detection
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
4. Execute o script:
   ```
   sh run_analysis.sh
   ```

**Observação:** O projeto será executado na porta 8501 por padrão.

## Contribuições
Contribuições são bem-vindas! Para contribuir, por favor, crie um pull request com suas propostas de melhorias ou correções.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
