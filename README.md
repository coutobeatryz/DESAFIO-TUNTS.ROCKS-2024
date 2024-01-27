# DESAFIO-TUNTS.ROCKS-2024
Parte integrante do processo seletivo da Tunts.Rocks, o desafio de programação tem como objetivo  principal a avaliação das habilidades de programação do candidato. Levando em conta não  apenas o êxito de implementação da funcionalidade desejada, mas também uma análise da  solução de forma estrutural, semântica e performática. 

# SOBRE O DESAFIO 

O desafio consiste na criação de uma aplicação em uma linguagem de programação de sua preferência (no caso foi usado Python) capaz de ler  uma planilha do google sheets, buscar as informações necessárias, calcular e escrever o  resultado na planilha;
<br/><br/>Com as informações da planilha em questão, foi pedido para calcular a situação de cada aluno baseado na média das 3 provas (P1, P2 e P3). Além disso, caso o número de faltas ultrapassasse 25% do número total de aulas o aluno terá a situação  "Reprovado por Falta", independente da média.  Caso a situação seja "Exame Final" é necessário calcular a "Nota para Aprovação Final"(naf) de  cada aluno de acordo com a seguinte fórmula:
```5 <= (m + naf)/2```
<br/> Caso a situação do aluno fosse diferente de "Exame Final", é necessário preencher o campo "Nota para  Aprovação Final" com 0 e, se fosse o caso, arredondar o resultado para o próximo número inteiro (aumentar) caso necessário. Também foi pedido para utiliza linhas de logs para acompanhamento das atividades da aplicação. 

# HOW TO RUN?

1. Pra rodar primeiro vamos instalar o ambiente necessário, segue aí:
```bash
python -m venv venv
```
- Use também:
```bash
.\venv\Scripts\activate
```
2. Certifique-se de ter as bibliotecas necessárias instaladas ;)
- "Quais bibliotecas?"
É fácil, me acompanha. Joga aí no terminal:
```bash
pip install gspread oauth2client google-auth google-auth-oauthlib google-auth-httplib2
```

# GOOGLE SHEETS

A planilha foi levamente modificada em questão da aparência mas continua do mesmo jeito como especificada.
<br/><br/> Caso queira acessar:
<br/>```https://docs.google.com/spreadsheets/d/18Dj5tZbTuafbK3s0313nkC2ghEzh94Ks-MbHOsciX6E/edit#gid=0```
