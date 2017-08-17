with open('/Users/songshuaichen/Downloads/Tag.txt', 'r') as f:
    with open('/Users/songshuaichen/Downloads/Tags.txt', 'w') as f1:

        temp = ''
        dict = {}
        for row in f:
            new_row = row[1:-2]
            s = new_row.split('><')


        #print(s)
            f1.write(' '.join(s))
            f1.write('\n')

   # print(temp)

