import random as r

class Generator:
    @staticmethod
    def generate_login():
        name = 'valeria'
        surname = 'syrtsova'
        cohort = '6'
        num = str(r.randint(100, 999))
        domain = r.choice(['@ya.ru', '@mail.ru', '@gmail.com', '@vk.com'])
        email = name+surname+cohort+num+domain
        return email


    @staticmethod
    def generate_password():
        symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()—_+=;:,./?`~[]{}'
        password = ''
        for num in range(6):
            password += r.choice(symbols)
        return password




