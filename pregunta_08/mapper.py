#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
      letra = line.split("  ")[0]
      valor = line.split("  ")[2]
      valor = float(valor)

      sys.stdout.write("{}\t{}\n".format(letra, valor))