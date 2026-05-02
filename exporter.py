from config import OUTPUT_FILE_EXCEL, OUTPUT_FILE_CSV

def export_data(df, export_type="both"):
    if export_type in ["excel", "both"]:
        df.to_excel(OUTPUT_FILE_EXCEL, index=False)

    if export_type in ["csv", "both"]:
        df.to_csv(OUTPUT_FILE_CSV, index=False)