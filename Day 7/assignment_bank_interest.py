class Bank_interest_calculator:
    # Class Variables
    __interest_rate = 8.6
    __interest_rate_SeniorCitizen = 8.4

    def __init__(self, p_amount, duration, seniorF):
        self.principle = p_amount
        self.dur = duration
        self.senior_flag = seniorF

    def si_calc(self):
        if self.senior_flag:
            print(f"SI for senior: {(self.principle * Bank_interest_calculator.__interest_rate_SeniorCitizen * self.dur) / 100}")
        else:
            print(f"SI for regular: {(self.principle * Bank_interest_calculator.__interest_rate * self.dur) / 100}")


if __name__ == '__main__':
    bank1 = Bank_interest_calculator(200, 1, True)
    bank2 = Bank_interest_calculator(200, 1, False)

    bank1.si_calc()
    bank2.si_calc()
