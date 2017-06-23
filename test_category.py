import csv

category = ['library', 'tool', 'system', 'plugin', 'api', 'database', 'engine']
tagCat_body = []
freq_dict = {}

def process(path, out_path):

    global freq_dict
    global tagCat_body

    csv_file = csv.reader(open(path, encoding='utf-8'))
    outfile = open(out_path, "w")

    for row in csv_file:
        freq_dict[row[0]] = int(row[1])

    for i in tagCat_body:
        try:
            if  freq_dict[i[0]] > 1000:
                print(i)
                outfile.write(i[0] +"\t" + i[1] +"\t"+ i[2])
        except KeyError:
            continue





def readFile(path, out_path):

    global category
    global tagCat_body

    file = open(path, encoding='utf-8')

    outfile = open(out_path, "w")

    while True:
        temp = file.readline()
        if not temp: break
        temp_list = temp.split('\t')
        word = temp_list[1].split(' ')
        if word[-1] == '':
            x = word[-2]
        else:
            x = word[-1]
        temp_list[1] = x

        try:
            outfile.write(temp_list[0] +"\t" + temp_list[1] +"\t"+ temp_list[2])
        except UnicodeEncodeError:
            continue
        if x in category:

            tagCat_body.append(temp_list)

    outfile.close()

readFile("d:\\tagCategory.txt", "d:\\processed_category.txt")
process("d:\\frequency.csv", "d:\\out.txt")



