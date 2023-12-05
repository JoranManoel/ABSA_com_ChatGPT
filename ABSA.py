import pandas as pd
import openai
import csv

dados = pd.read_csv('comments.csv', delimiter=";")

feedbacks = dados['comments']

openai_api_key = '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'

openai.api_key = openai_api_key

def analisar_sentimentos(feedbacks):

  comentarios_formatados = "\n".join([f"- {feedback}" for feedback in feedbacks])

  prompt = f"""
            Indentifique os aspectos, opinião e os sentimentos dos comentários abaixo e obedeça as regras na resposta:
            {comentarios_formatados}
            """

  respostaAPI = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "system",
          "content": """
                        Você é um modelo de análise de sentimentos baseada em aspectos com foco em feedbacks sobre 
                        experiências dos usuários dos serviços da prefeitura do Recife.
                        exemplo de comentário: O atendimento na unidade de saúde local é excelente.
                        as respostas tem que seguir esse padrão: "atendimento na unidade de saúde, exelente, positivo"
                        obedeça regorosamente as regras:
                        1 não utilize nem mais nem menos que duas virgulas 
                        2 os sentimentos serão positivo, negativos ou neutros
                        3 as virgulas separam as 3 colunas 
                        4 coso um comentario tenha emojis serão adicionados na coluna 2 opnião
                        5 nenhuma das três colunas podem ser vazias
                        6 faça exatamente 3 colunas para aspecto, opinião e sentimento separadas por virgula
                        7 enclua os emojis literalmente na coluna de opiniões
                        8 os aspectos devem estar relacionado a algum serviço da prefeitura
                        9 caso não encontre o aspecto coloque "Relacionado a postagem"
                      """
      },
      {
          "role": "user",
          "content": prompt
      }
    ]
  )
  return respostaAPI.choices[0].message.content

insights = analisar_sentimentos(feedbacks)

def write_row_without_quotes(file, data):
    writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
    writer.writerow(data)

with open('insights.csv', 'a', newline='', encoding='utf-8') as arquivo_csv:
    write_row_without_quotes(arquivo_csv, [insights])

print("Aspect-based sentiment analysis completed!")
