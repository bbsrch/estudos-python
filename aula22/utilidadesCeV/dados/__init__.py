def leiadinheiro(txt):
    while True:
        v = str(input(txt))
        if "," in v:
            v = v.replace(',', '.')
        if not v.isnumeric() and not '.' in v:
            print('\033[31mErro! Digite um valor monetário válido.\033[m')
        else:
            return float(v)