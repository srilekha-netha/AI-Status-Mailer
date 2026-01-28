# import pandas as pd
# from summarize import summarize_status
# from mailer import send_email

# # Path to your tracker file
# EXCEL_PATH = "data/QA tracker.xlsx"

# def read_excel_data():
#     try:
#         # Try reading Excel using openpyxl
#         df = pd.read_excel(EXCEL_PATH, engine="openpyxl")
#     except Exception:
#         # Fallback if saved as CSV
#         df = pd.read_csv(EXCEL_PATH.replace(".xlsx", ".csv"))
    
#     # Drop completely empty rows
#     df.dropna(how="all", inplace=True)
    
#     # FILTER ONLY COMPLETED TASKS
#     # df = df[df["Status"].str.strip().str.lower() == "completed"]

#     updates = ""
#     for _, row in df.iterrows():
#         program = row.get("Program Name", "")
#         layer = row.get("ODS Layer", "")
#         owner = row.get("Owner", "Unassigned")
#         status = row.get("Status", "")
#         date_done = row.get("Date Completed", "")
#         comments = row.get("Comments", "")

#         updates += (
#             f"Program: {program}, ODS Layer: {layer}, "
#             f"Owner: {owner}, Status: {status}, "
#             f"Date Completed: {date_done}, Comments: {comments}\n"
#         )

#     return updates.strip()


# def main():
#     print("📊 Reading team updates...")
#     updates_text = read_excel_data()

#     if not updates_text:
#         print("⚠️ No updates found in the Excel file.")
#         return

#     print("🤖 Generating AI summary using Groq...")
#     summary = summarize_status(updates_text)

#     print("\n--- SUMMARY GENERATED ---\n")
#     print(summary)
#     print("\n--------------------------\n")

#     print("📧 Sending email...")
#     send_email(
#         subject="Daily QA Tracker Status Update",
#         body=summary,
#         to_emails=["Masammagari.Navya@Digitide.com", "Jella.Srilekha@digitide.com"]
#     )

# if __name__ == "__main__":
#     main()

import pandas as pd
from mailer import send_email

# Path to your tracker file
EXCEL_PATH = "data/QA tracker.xlsx"


def read_excel_data():
    try:
        df = pd.read_excel(EXCEL_PATH, engine="openpyxl")
    except Exception:
        df = pd.read_csv(EXCEL_PATH.replace(".xlsx", ".csv"))

    # Drop completely empty rows
    df.dropna(how="all", inplace=True)

    # ✅ FILTER ONLY COMPLETED TASKS
    df = df[df["Status"].astype(str).str.strip().str.lower() == "completed"]

    return df


def build_table(df):
    # Define fixed column widths
    col_widths = {
        "Program Name": 18,
        "ODS Layer": 12,
        "Owner": 15,
        "Date Completed": 15,
        "Comments": 30
    }

    # Header
    header = (
        f"{'Program Name':<{col_widths['Program Name']}} "
        f"{'ODS Layer':<{col_widths['ODS Layer']}} "
        f"{'Owner':<{col_widths['Owner']}} "
        f"{'Date Completed':<{col_widths['Date Completed']}} "
        f"{'Comments':<{col_widths['Comments']}}\n"
    )

    separator = (
        f"{'-'*col_widths['Program Name']} "
        f"{'-'*col_widths['ODS Layer']} "
        f"{'-'*col_widths['Owner']} "
        f"{'-'*col_widths['Date Completed']} "
        f"{'-'*col_widths['Comments']}\n"
    )

    table = header + separator

    # Rows
    for _, row in df.iterrows():
        table += (
            f"{str(row.get('Program Name', '—')):<{col_widths['Program Name']}} "
            f"{str(row.get('ODS Layer', '—')):<{col_widths['ODS Layer']}} "
            f"{str(row.get('Owner', 'Unassigned')):<{col_widths['Owner']}} "
            f"{str(row.get('Date Completed', '—')):<{col_widths['Date Completed']}} "
            f"{str(row.get('Comments', '—')):<{col_widths['Comments']}}\n"
        )

    return table


def main():
    print("📊 Reading team updates...")
    df = read_excel_data()

    if df.empty:
        email_body = (
            "Dear Leadership Team,\n\n"
            "There are no completed items recorded in the tracker for today.\n\n"
            "Best regards,\n"
            "Srilekha\n"
            "Senior Project Coordinator"
        )
    else:
        table = build_table(df)
        email_body = (
            "Dear Leadership Team,\n\n"
            "Please find below the list of completed project activities "
            "recorded in the tracker as of today.\n\n"
            f"{table}\n"
            "The above items have been reviewed and marked as completed.\n\n"
            "Best regards,\n"
            "Srilekha\n"
            "Senior Project Coordinator"
        )

    print("\n--- EMAIL PREVIEW ---\n")
    print(email_body)
    print("\n---------------------\n")

    print("📧 Sending email...")
    send_email(
        subject="Completed Tasks – Daily QA Tracker Update",
        body=email_body,
        to_emails=[
            "Srilekhanetha163@gmail.com"
        ]
    )


if __name__ == "__main__":
    main()
