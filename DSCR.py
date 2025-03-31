def dscr(net_operating_income, total_debt_service):
    return net_operating_income / total_debt_service


# Example inputs
net_operating_income = 1200000  # Annual NOI in dollars
total_debt_service = 900000  # Annual debt service in dollars

dscr_value = dscr(net_operating_income, total_debt_service)
print(f"Debt Service Coverage Ratio (DSCR): {dscr_value:.2f}")


