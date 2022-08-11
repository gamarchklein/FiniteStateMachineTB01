# Gabriel Marchioro Klein
# O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt) contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de entrada. As linhas subsequentes contém uma string por linha. A seguir está um exemplo das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
#   3
#   abbaba
#   abababb
#   bbabbaaab
# Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo será representado  por  um  número  inteiro  positivo.  A  resposta  do  seu  programa  deverá conter  uma, e somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado  da validação conforme o formato indicado a seguir:
#   abbaba: não pertence.

def state1(line, completeLine):
  if len(line) == 0:
    print(completeLine + ' não pertence')
    return False
  elif line[0] == 'a':
    line = line[1:]
    state2(line, completeLine)
  elif line[0] == 'b':
    line = line[1:]
    state1(line, completeLine)
  else:
    print(completeLine + ' não pertence')
    return False

def state2(line, completeLine):
  if len(line) == 0:
    print(completeLine + ' não pertence')
    return False
  elif line[0] == 'b':
    line = line[1:]
    state3(line, completeLine)
  elif line[0] == 'a':
    state5(completeLine)
  else:
    print(completeLine + ' não pertence')
    return False

def state3(line, completeLine):
  if len(line) == 0:
    print(completeLine + ' não pertence')
    return False
  elif line[0] == 'b':
    line = line[1:]
    state4(line, completeLine)
  elif line[0] == 'a':
    state5(completeLine)
  else:
    print(completeLine + ' não pertence')
    return False

def state4(line, completeLine):
  if len(line) == 0:
    print(completeLine + ' pertence')
    return True
  elif line[0] == 'a':
    line = line[1:]
    state2(line, completeLine)
  elif line[0] == 'b':
    line = line[1:]
    state4(line, completeLine)
  else:
    print(completeLine + ' não pertence')
    return False


def state5(completeLine):
  print(completeLine + ' não pertence')
  return False

def stateMachine(file):
  with open(file, 'r') as file:
    lines = file.readlines()
    stringNum = int(lines[0].strip())
    for i in range(1, stringNum + 1):
      try:
        line = lines[i].strip()
        state1(line, line)
      except:
        print('Número de linhas registradas maior do que número de linhas presentes')
  file.close()

#print('\nFILE 1') #opcional
stateMachine('finiteFile.txt') # COLOQUE SEUS ARQUIVOS AQUI
#print('\nFILE 2') #opcional
stateMachine('finiteFile2.txt') # COLOQUE SEUS ARQUIVOS AQUI
#print('\nFILE 3') #opcional
stateMachine('finiteFile3.txt') # COLOQUE SEUS ARQUIVOS AQUI