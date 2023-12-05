# Análise de Sentimento Baseada em Aspectos

## Visão Geral
Este script em Python realiza análise de sentimento baseada em aspectos em feedbacks/comentários de usuários relacionados aos serviços da prefeitura do Recife. Ele utiliza o modelo GPT-3.5-turbo da OpenAI para analisar e extrair aspectos, opiniões e sentimentos dos comentários fornecidos. Os resultados analisados são então salvos em um arquivo CSV chamado 'insights.csv'.

## Pré-requisitos
Antes de executar o script, certifique-se de ter as bibliotecas Python necessárias instaladas. Você pode instalá-las usando o seguinte comando:

```bash
pip install pandas openai
```

## Uso
1. **Dados de Entrada**: Certifique-se de que o arquivo de dados de entrada ('comments.csv') está disponível e formatado corretamente. Os comentários devem ser armazenados na coluna 'comments' do arquivo CSV.

2. **Chave de API da OpenAI**: Substitua a chave fictícia 'openai_api_key' pela sua chave real da API da OpenAI.

3. **Execute o Script**: Execute o script em um ambiente Python. As análises serão impressas no console, e os resultados serão salvos em 'insights.csv'.

```bash
python script_name.py
```

## Detalhes do Script
- O script utiliza a biblioteca Pandas para ler comentários do arquivo 'comments.csv'.
- O modelo GPT-3.5-turbo da OpenAI é utilizado para analisar sentimentos com base em uma mensagem de sistema predefinida e comentários fornecidos pelo usuário.
- Os resultados da análise, incluindo aspectos, opiniões e sentimentos, são salvos no arquivo 'insights.csv'.
- O sistema fornece diretrizes na mensagem de sistema para formatação de respostas de acordo com regras específicas.

## Saída
O script gera um arquivo 'insights.csv' contendo os resultados analisados. Cada linha no arquivo CSV inclui três colunas: aspecto, opinião e sentimento, separadas por vírgulas.

## Notas Importantes
- Certifique-se de manter a chave da API da OpenAI segura e não compartilhá-la publicamente.
- Revise e atualize o script conforme necessário para atender a quaisquer alterações na API da OpenAI ou outras dependências.

**Observação:** O script assume um formato específico para os comentários dos usuários e segue as regras fornecidas na mensagem de sistema. Ajustes podem ser necessários com base em requisitos em evolução ou mudanças na estrutura dos dados de entrada.

Sinta-se à vontade para entrar em contato para qualquer assistência adicional ou personalização.
