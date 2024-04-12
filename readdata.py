def openreadtxt(file_name):
    data = []
    with open(file_name, 'r') as file:  # 使用 with 语句自动关闭文件
        for line in file:
            # 分割每一行数据
            parts = line.strip().split()
            # 将前面的数字转换为浮点数，并将字符串作为最后一个元素
            data.append([float(x) for x in parts[:-1]] + [parts[-1]])
    return data
#data = openreadtxt('D:\大地形变测量学\第二次作业说明\青藏高原GPS数据\gps_data.txt.txt')
#print(data[1])
