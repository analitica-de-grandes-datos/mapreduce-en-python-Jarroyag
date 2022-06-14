#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    curkey = None
    total = 0
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
            total += val
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, total))
        urkey = key
        total = val
sys.stdout.write("{}\t{}\n".format(curkey, total))    

cat /tmp/wordcount/input/credit.csv | python3 /tmp/wordcount/mapper.py | sort | python3 /tmp/reducer.py | head
                
