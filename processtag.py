with open ('/Users/songshuaichen/Desktop/tagWiki 2.txt', 'r') as f:
    temp = ''
    for line in f:
        new_line = line[2:-2]
        num = 0
        for i in new_line:

            if i == ' ':
                new_line = new_line[:num]+'\t'+new_line[28:]
                break
            num += 1
        num = 0
        for i in new_line:
            if i == ' ' and new_line[num+1] == ' ':
                new_line = new_line[:num]
                break
            num += 1
       #print new_line
        temp += new_line + '\n'
        line = new_line
    print(temp)
    with open('/Users/songshuaichen/Desktop/tagWiki.txt', 'w') as f1:

        f1.write(temp)