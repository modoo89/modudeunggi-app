
def calc_loan_by_condition(price: int, condition: str) -> dict:
    방공제 = 5_500_0000
    rules = {
        "비1": lambda p: p * 0.70,
        "비2": lambda p: p * 0.60,
        "규2-1": lambda p: p * 0.50,
        "규2-2": lambda p: p * 0.40,
        "사선": lambda p: max(p * 0.85 - 방공제, 0),
        "사후": lambda p: max(p * 0.80 - 방공제, 0),
    }
    if condition not in rules:
        return {"error": "❌ 유효하지 않은 조건 코드입니다."}
    loan_amount = int(rules[condition](price))
    return {"시세": price, "조건": condition, "가능대출금": loan_amount}
