# TweetThreatDetect

## Descrição
Este projeto implementa um sistema de detecção de ameaças cibernéticas em tweets usando técnicas avançadas de Processamento de Linguagem Natural (NLP) e análise de sentimentos. Ele visa identificar padrões relacionados a ameaças cibernéticas e avaliar a polaridade do sentimento dos tweets, auxiliando na prevenção e resposta a incidentes de segurança cibernética.

## Live Preview
Uma demonstracao da interface desenvolvida para este projeto pode ser encontrada em:
   ```
    https://tweetthreatanalysis-nbzynjakja-rj.a.run.app
   ```

## Pré-Requisitos
- Python 3.x
- Bibliotecas Python: numpy, pandas, scikit-learn, nltk, tensorflow
- Docker (opcional)

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
4. Execute o container:
   ```
   docker run tweet-threat-detection
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

## Contribuições
Contribuições são bem-vindas! Para contribuir, por favor, crie um pull request com suas propostas de melhorias ou correções.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
