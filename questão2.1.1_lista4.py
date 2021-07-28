def bracket (a,f,s=0.01,m=2):    #f é para avaliar, #s é o passo, m é o multiplicador para acelerar o processo.

    bracket = [a] #criando vetor com o intervalo desejado. # a=-2
    #print("\nprimeiro bracket:",bracket)
    b = a + s # é um ponto b tal que é a soma de a + o passo, para avaliar se o próximo ponto é maior ou menor, tem de ser menor pois quer minimizar.
    bracket = [a,b] #criando vetor com o intervalo desejado. # a=-2 ; b = -2+0.01=-1.99
    #print("\n\nsegundo bracket:",bracket)

    fa = f(a)   #valor da função no ponto a, indo para fa, ou seja, é a^2
    #print("\nimpriminfo fa",fa,"\n")
    fb = f(b)   #valor da função no ponto b, indo para fb,ou seja, é b^2
    #print("\nimpriminfo fb",fb,"\n")
    
    if fa>=fb :

        c = b + s #criando ponto para encontrar o mínimo preservando o ponto a.
        fc = f(c)
              
        while fc < fb: #encontrando o mínimo comparando pontos.
            b = c
            fb = fc
            s = s*m
            c = c + s
            fc = f(c)
            print("\naqui está procurando-se o menor valor de b\nvalors de b:",b,"valors de b:",c)
        print("fb",fb,"valor de fc",fc) 
        bracket = [a,c] #criando vetor com o intervalo desejado.
        print("\n\nvalor encontrado minimizando: ",bracket,)
    elif fa < fb :
        c = a - s
        fc = f(c)
        while fc < fa :
            a = c
            fa = fc
            s = s*m
            c = c - s
        bracket = [c,b] #criando lista com C e B
        print("\n\nquarto bracket:",bracket)
    return bracket

f = lambda x: x**2 # f é minha função
b = bracket(-2,f)

print("\n\n\nbreacket final",b)

