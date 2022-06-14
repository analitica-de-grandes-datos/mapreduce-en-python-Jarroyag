#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ =="__main__":
    for line in sys.stdin:
        for word in line.split():
            sys.stdout.write("{}\t1\n".format(word))
cat /tmp/wordcount/input/text*.txt | python3 mapper.py | head            
