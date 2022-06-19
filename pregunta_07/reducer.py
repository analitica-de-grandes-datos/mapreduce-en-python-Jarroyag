#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    vector = []
    
    for line in sys.stdin:

        letra, data, valor = line.split("\t")
        valor = int(valor)
        vector.append((letra, data, valor))
    vector.sort(key=lambda orden: (orden[0], orden[2])) 

    for line in vector:


        sys.stdout.write("{} {} {}\n".format(line[0], line[1].strip(), line[2]))