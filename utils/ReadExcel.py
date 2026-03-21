from openpyxl import load_workbook


def get_data(filepath, sheet_name):
    workbook = load_workbook(filepath)
    sheet = workbook[sheet_name]
    data = []
    rows = sheet.iter_rows(values_only=True)
    headers = next(rows)  # skip header
    for row in rows:
        data.append(dict(zip(headers, row)))

    workbook.close()
    return data

def get_login_data(filepath, sheet_name):
    data = get_data(filepath, sheet_name)
    valid_data = []
    invalid_data = []

    for d in data:
        if d["testcase"] == "valid":
            valid_data.append((d["Username"], d["Password"]))
        elif d["testcase"] == "invalid":
            invalid_data.append((d["Username"], d["Password"], d["msg"]))

    return valid_data, invalid_data
