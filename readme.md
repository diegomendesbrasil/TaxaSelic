# Taxa Selic – Scripts para Consulta de Dados

Este repositório traz scripts simples em Python para consultar e visualizar informações sobre a Taxa Selic diretamente da API do Banco Central do Brasil. O objetivo é facilitar o acesso a dados históricos da taxa básica de juros, seja para estudos, análises ou integração com outros projetos.

Com base nesses códigos, você será capaz de criar em seu lakehouse tabelas capazes de trazer capacidade analitica para qualquer time financeiro utilizando a selic como base. 

No meu caso, disponibilizarei 2 bases, selic e selicacumuladamensal para que o time de negócio consiga criar seus relacionamentos necessários que dependam da taxa selic.

fontes: https://dadosabertos.bcb.gov.br/dataset/11-taxa-de-juros---selic/resource/b73edc07-bbac-430c-a2cb-b1639e605fa8
        
        
        https://dadosabertos.bcb.gov.br/group/economia-e-financas?q=selic&sort=score+desc%2C+metadata_modified+desc

## O que você encontra aqui

- **metaselic.py**  
  Baixa a Meta Selic definida pelo COPOM desde junho de 2022 e mostra os resultados em formato de tabela (DataFrame). Útil para acompanhar as decisões do Banco Central ao longo do tempo.

- **selicacumuladamensal.py**  
  Consulta a Selic acumulada mês a mês, também exibindo os dados em tabela. Ideal para quem precisa analisar o rendimento mensal da taxa.

## Como usar

1. **Instale as dependências**  
   Antes de rodar os scripts, instale as bibliotecas necessárias:
   ```sh
   pip install -r requirements.txt
