# Modificação de frases
frase = 'Curso em vídeo Python'
print(frase.upper().count('O'))  # modifica a frase para maiúscula, depois conta o 'O'
print(frase.replace('Python', 'Android')) # substituição
dividido = frase.split() # divide as palavras
print(dividido[0]) # mostra a primeira palavra que foi dividida
print(dividido[0][2]) # pega a primeira palavra e mostra a terceira letra


print('''olá saori,
vim aqui te dizer que gosto muito de você
espero que tenha muito scat na sua vida
beijos!''') # três aspas para escrever um texto grande com parágrafos