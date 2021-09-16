
# ======variables======
string = 'hello, let\'s learn python'
string1 = '--test the strip()---'

# ======Escape character======
print('doesn\'t')
print("doesn't")


# ======Common functions======
string.replace(",", "")
# 把所有的','去掉

string.split(" ")
# 以" "为分隔符，分割成列表的形式.
# split(str="", num=string.count(str))  (分隔符，要分割成几个默认-1即所有)

string1.strip('-')
# 去掉字符串两头的指定字符

# ======字符串格式化======
A = 'pdf'
print(f'this is a {A}')


