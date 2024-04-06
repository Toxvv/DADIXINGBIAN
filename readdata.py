def openreadtxt(file_name):
    data = []
    file = open(file_name, 'r')  # 打开文件
    file_data = file.readlines()  # 读取所有行
    for row in file_data:
        tmp_list = row.split(' ')  # 按‘，’切分每行的数据
        tmp_list[-1] = tmp_list[-1].replace('\n','') #去掉换行符
        data.append(tmp_list)  # 将每行数据插入data中
    return data



data = openreadtxt('D:\大地形变测量学\第二次作业说明\青藏高原GPS数据\gps_data.txt.txt')
print(data[1])