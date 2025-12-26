def fee_status(paid, total):
    return "Paid" if paid >= total else "Pending"
