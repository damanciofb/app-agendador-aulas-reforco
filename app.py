from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
from io import BytesIO
from pymongo import MongoClient

app = Flask(__name__)

# Conectar ao MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['escola']
alunos_collection = db['alunos']
agenda_collection = db['agenda']

# Lista de matérias, dias da semana e agendamento
materias = ["Matemática", "Português", "História", "Inglês", "Física"]
dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

# Séries para os níveis de ensino
series = {
    "Ensino Fundamental": ["1ª Série", "2ª Série", "3ª Série", "4ª Série", "5ª Série", "6ª Série", "7ª Série", "8ª Série", "9ª Série"],
    "Ensino Médio": ["1ª Ano", "2ª Ano", "3ª Ano"]
}

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para cadastrar alunos
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form.get('name')
        idade = request.form.get('age')
        nivel_ensino = request.form.get('education_level')
        serie_selecionada = request.form.get('grade')  # Captura a série selecionada
        materias_selecionadas = request.form.getlist('subjects')  # Captura as matérias selecionadas
        dias_selecionados = request.form.getlist('days')  # Captura os dias da semana selecionados
        horario_inicio = request.form.get('start_time')  # Captura o horário inicial
        horario_fim = request.form.get('end_time')  # Captura o horário final

        # Cadastrar aluno e agendar automaticamente
        dados_aluno = {
            "nome": nome,
            "idade": idade,
            "nivel_ensino": nivel_ensino,
            "serie": serie_selecionada,
            "materias": materias_selecionadas,
            "dias": dias_selecionados,
            "horario_inicio": horario_inicio,
            "horario_fim": horario_fim
        }
        alunos_collection.insert_one(dados_aluno)
        
        # Agendar o aluno nos dias selecionados
        for dia in dias_selecionados:
            agenda_collection.update_one(
                {"dia": dia},
                {"$push": {"alunos": dados_aluno}},
                upsert=True
            )
        
        return redirect(url_for('success', name=nome))

    return render_template('register.html', subjects=materias, weekdays=dias_semana, series=series)

# Rota para exibir o agendamento
@app.route('/schedule', methods=['GET', 'POST'])
def view_schedule():
    aluno_selecionado = None
    agenda_aluno = {}

    if request.method == 'POST':
        nome_aluno = request.form.get('student')
        # Buscar o aluno selecionado
        aluno_selecionado = alunos_collection.find_one({"nome": nome_aluno})

        # Criar um dicionário com os dias e horários agendados
        if aluno_selecionado:
            agenda_aluno = {
                "dias": aluno_selecionado.get('dias', []),
                "horario_inicio": aluno_selecionado.get('horario_inicio', 'Não definido'),
                "horario_fim": aluno_selecionado.get('horario_fim', 'Não definido')
            }

    return render_template('schedule.html', students=alunos_collection.find(), selected_student=aluno_selecionado, student_agenda=agenda_aluno)

# Rota para exportar o agendamento de um aluno específico para Excel
@app.route('/export_student/<student_name>')
def export_student(student_name):
    dados_aluno = alunos_collection.find_one({"nome": student_name})
    
    if dados_aluno:
        # Cria um DataFrame para o aluno
        df = pd.DataFrame({
            "Nome": [dados_aluno['nome']],
            "Idade": [dados_aluno['idade']],
            "Nível de Ensino": [dados_aluno['nivel_ensino']],
            "Série": [dados_aluno['serie']],
            "Matérias": [', '.join(dados_aluno['materias'])],
            "Dias": [', '.join(dados_aluno['dias'])],
            "Horário Inicial": [dados_aluno['horario_inicio']],
            "Horário Final": [dados_aluno['horario_fim']]
        })
        
        # Cria um buffer em memória
        output = BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)

        return send_file(output, as_attachment=True, download_name=f"{student_name}_agendamento.xlsx", mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    return "Aluno não encontrado", 404

# Rota para exportar o relatório geral para Excel
@app.route('/export_general')
def export_general():
    # Cria um DataFrame para todos os alunos
    alunos = list(alunos_collection.find())
    df = pd.DataFrame(alunos)
    
    # Renomeia as colunas para português (caso necessário)
    if not df.empty:
        df = df.rename(columns={
            "nome": "Nome",
            "idade": "Idade",
            "nivel_ensino": "Nível de Ensino",
            "serie": "Série",
            "materias": "Matérias",
            "dias": "Dias",
            "horario_inicio": "Horário Inicial",
            "horario_fim": "Horário Final"
        })
    
    # Cria um buffer em memória
    output = BytesIO()
    df.to_excel(output, index=False, engine='openpyxl')
    output.seek(0)

    return send_file(output, as_attachment=True, download_name="relatorio_geral.xlsx", mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# Rota de confirmação após o cadastro
@app.route('/success')
def success():
    nome = request.args.get('name')
    return render_template('success.html', name=nome)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
