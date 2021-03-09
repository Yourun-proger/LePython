import sys
from re import sub

file = open(sys.argv[1], 'r', encoding='utf-8').read()
changes = {
    ' comme ': ' as ',
    ' attendre ': 'await',
    'attendre': 'await',
    'si ': 'if ',
    'si_autre ': 'elif ',
    'autre': 'else',
    'passe': 'pass',
    'est_il ': 'is ',
    'n_est_pas ': 'not',
    'affirme ': 'assert',
    'augmente ': 'raise ',
    'et ': 'and ',
    'pause': 'break',
    'de ': 'from ',
    'importe ': 'import ',
    'sauf ': 'except ',
    'dans ': 'in ',
    'enfin': 'finally',
    'avec ': 'with',
    'rendement ': 'yield',
    'pendant_que ': 'while ',
    'pour ': 'for ',
    ' ou ': ' or '
}
for key, value in changes.items():
    file = sub(key, value, file)

exec(file,
     {
         'imprime': print,
         'long': len,
         'annu': dir,
         'gamme': range,
         'inter': exec,
         'ouvre': open,
         'entre': input,
         'Faux': False,
         'Vrai': True,
         'rien': None,
         'comp': int,
         'flot': float,

     }
     )
