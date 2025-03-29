
def get_kb_price_from_hogang(query):
    dummy_prices = {
        "리버힐삼성아파트": 1230000000,
        "장암주공5단지": 280000000
    }
    return dummy_prices.get(query, "❌ 해당 아파트 시세 없음")
