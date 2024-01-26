import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SAMPLE_SPREADSHEET_ID = "18Dj5tZbTuafbK3s0313nkC2ghEzh94Ks-MbHOsciX6E"
SAMPLE_RANGE_NAME = "engenharia_de_software!A3:H27"

def calculate_status_and_grade(average, absences):
    if absences > 60*0.25:
        return "Reprovado por Falta", 0
    elif average < 50:
        return "Reprovado por Nota", 0
    elif 50 <= average < 70:
        grade = round(70 - average) 
        return "Exame Final", grade
    else:
        return "Aprovado", 0


def main():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    try:
        service = build("sheets", "v4", credentials=creds)

        # Lendo as informações da planilha
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()

        values = result['values']
        
        total_aulas = 60 

        column_status = values[0].index("Situação") if "Situação" in values[0] else None
        column_grade = values[0].index("Nota para Aprovação Final") if "Nota para Aprovação Final" in values[0] else None

        # Cálculo e adição das informações para cada aluno
        for i in range(1, len(values)):
            student = values[i]
            p1, p2, p3 = float(student[3]), float(student[4]), float(student[5])
            absences = int(student[2])
            
            average = (p1 + p2 + p3) / 3

            status, grade = calculate_status_and_grade(average, absences)

            if column_status is not None:
                student[column_status] = status
            if column_grade is not None:
                student[column_grade] = grade

            print(f"student: {student[1]} (Matrícula: {student[0]}) - Média: {average}, absences: {absences}, Situação: {status}, grade: {grade}")

        result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME, valueInputOption="USER_ENTERED", body={'values': values}).execute()

    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()
