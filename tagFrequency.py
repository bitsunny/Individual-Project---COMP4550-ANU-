import csv

## dictionary key: word, value: frequency
fre_dict = {}

## save the keys for dictionary to make it faster
cache_list = []

adict = []

def getIntroduction(path):

    global adict

    intro_dict = {}

    file = open(path, encoding = 'utf-8')

    ##csv_file = csv.reader(open(path,encoding = 'gb2312'))
    print('GOGO')
    intr = 0
    while True:
        temp = file.readline()
        if not temp: break
        temp_list = temp.split('\t')
        intro_dict[temp_list[0]] = [temp_list[1], temp_list[2]]

    print('Bad')
    intc = 1
    for i in adict:
        try:
            print(str(intc) + "\t" + i[0] + "\tCategory: " + intro_dict[i[0]][0] + "\tIntro: " + intro_dict[i[0]][1][:-1])
        except KeyError:
            print(i[0] + "\t" + 'is not in the list')
        intc += 1



def main(path, apath):

    global fre_dict
    global cache_list
    global adict

    csv_file = csv.reader(open(path, encoding='utf-8'))

    temp_str = ''
    for row in csv_file:
        if row[0] == 'NULL': continue
        else:
            temp_str = row[0][1:-1]
            s = temp_str.split('><')
            for i in s:
                if i in fre_dict.keys():
                    fre_dict[i] += 1;
                else:
                    fre_dict[i] = 1;

    print('----- read finished -----')

    dict = sorted(fre_dict.items(), key=lambda d: d[1], reverse=True)

    print('----- sort finished -----')

    for i in range(1000):
        print(dict[i])
        adict.append(dict[i])

    getIntroduction(apath)

main('d:\\alltags.csv',"d:\\tagCategory.txt")