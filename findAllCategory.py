# coding: UTF-8
def main(path, out_path):

    main_list = {}

    file = open(path, encoding='utf-8')

    outfile = open(out_path, "w", encoding = 'utf-8')

    while True:
        temp = file.readline()
        if not temp: break
        temp_list = temp.split('\t')
        word = temp_list[1].split(' ')
        x = ''
        if word[-1] == '':
            x = word[-2]
        else:
            x = word[-1]

        if x not in main_list.keys():
            main_list[x] = 1
        else:
            main_list[x] += 1

    for i in main_list.keys():
        outfile.write(i+"\t"+str(main_list[i])+"\n")
    outfile.close()

main("d:\\svo1.txt","d:\\out2.txt")