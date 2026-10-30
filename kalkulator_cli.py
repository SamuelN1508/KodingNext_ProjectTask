# ============================================================
# Simple Discount Calculator (CLI - Python)
# Designed for live-coding and beginner teaching demos
# ============================================================

def main():
    print("=" * 35)
    print("      DISCOUNT CALCULATOR")
    print("=" * 35)

    # 1. Take input from user
    try:
        price = float(input("Enter original price: "))
        discount = float(input("Enter discount rate (%): "))
    except ValueError:
        print("Error: Please enter valid numbers!")
        return

    # 2. Calculate discount formula
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount

    # 3. Display output
    print("-" * 35)
    print(f"Original Price : Rp {price:,.2f}")
    print(f"Discount ({discount:.0f}%)  : Rp {discount_amount:,.2f}")
    print(f"Final Price    : Rp {final_price:,.2f}")
    print("=" * 35)


if __name__ == "__main__":
    main()
