import csv
import os
import datetime
import time
stu = []
#显示所有学生信息
def show():
    stu = init_stulist()
    i = os.system('cls')
    print("---------以下为所有学生信息---------")
    print("学号", end='\t')
    print("姓名", end='\t')
    print("数学", end='\t')
    print("外语", end='\t')
    print("专业", end='\t')
    print('\n')
    for i in stu:
        for j in i.values():
            print(j,end='\t')
        print('\n')
    print("------------------------------------")
#判断学号是否存在
def sno_exist(sno):
    for i in stu:
        if sno==i['学号']:
            return 1
    return 0
#输出数据到csv
def save():
    newfile = open('./student_data.csv', 'w+', newline='')
    filewrite = csv.writer(newfile)
    filewrite.writerow(['学号','姓名','数学','外语','专业'])
    for i in stu:
        filewrite.writerow(list(i.values()))
    newfile.close()
#录入成绩
def Input():
    student = {"学号": '', "姓名": '', "数学": 0, "外语": 0, "专业": 0}
    i = os.system('cls')
    print("请输入录入学生的信息，以空格隔开(学号 姓名 数学成绩 外语成绩 专业成绩)")
    a,b,c,d,e = map(str,input().split())
    while sno_exist(a):
        print("学号已存在，请重新输入信息:")
        a, b, c, d, e = map(str, input().split())
    int(c)
    int(d)
    int(e)
    student["学号"] = a
    student["姓名"] = b
    student["数学"] = c
    student["外语"] = e
    student["专业"] = d
    stu.append(student)
    save()
    i = os.system('cls')
    print("┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
    print("|----1.继续录入学生信息----|")
    print("|----2.返回主菜单----------|")
    print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
    xx = input("录入成功！请选择：")
    while xx != '1' and xx != '2':
        xx = input("选择有误，请重新选择：")
    if xx == '1':
        Input()
        return
    elif xx == '2':
        menu()
        return
#查询成绩
def Query():
    i = os.system('cls')
    print("┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
    print("|----1.显示所有学生成绩----|")
    print("|----2.学号查询学生成绩----|")
    print("|----3.返回主菜单----------|")
    print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
    xx = input("请输入您的选择:")
    while xx != '1' and xx != '2' and xx != '3':
        xx = input("选择有误，请重新选择：")
    if xx=='1':
        show()
        print("\n┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
        print("|----1.继续查询学生成绩----|")
        print("|----2.返回主菜单----------|")
        print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
        xx = input("成绩查询成功！请选择：")
        while xx!='1' and xx!='2':
            xx = input("选择有误，请重新选择：")
        if xx == '1':
            Query()
            return
        elif xx == '2':
            menu()
            return
    elif xx=='2':
        i = os.system('cls')
        sno = input("请输入待查询学生的学号：")
        while sno_exist(sno)==0:
            sno = input("输入学号有误，请重新输入：")
        for i in stu:
            if sno==i['学号']:
                print("学号\t姓名\t数学\t外语\t专业\n")
                print(i['学号'],'\t',i['姓名'],'\t',i['数学'],'\t',i['外语'],'\t',i['专业'])
                print("\n┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
                print("|----1.继续查询学生成绩----|")
                print("|----2.返回主菜单----------|")
                print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
                xx = input("成绩查询成功！请选择：")
                if xx == '1':
                    Query()
                    return
                elif xx == '2':
                    menu()
                    return
                break
    elif xx=='3':
        menu()
        return
#修改成绩
def Modify():
    flag = -1
    index = -1
    i = os.system('cls')
    sno = input("请输入要修改成绩的学生学号:")
    for i in stu:
        index+=1
        if sno == i["学号"]:
            flag = index
            break
    if flag==-1:
        i = os.system('cls')
        print("┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
        print("|----1.重新输入学生学号----|")
        print("|----2.返回主菜单----------|")
        print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
        xx = input("输入的学号不存在，请选择：")
        while xx!='1' and xx!='2':
            xx = input("选择错误，请重新选择：")
        if xx=='1':
            Modify()
            return
        elif xx=='2':
            menu()
            return
    else:
        print("请输入该同学的成绩:")
        mathg = int(input("数学:"))
        flg = int(input("外语:"))
        majorg = int(input("专业:"))
        stu[flag]['数学'] = mathg
        stu[flag]['外语'] = flg
        stu[flag]['专业'] = majorg
        save()
        i = os.system('cls')
        print("┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
        print("|----1.继续修改学生成绩----|")
        print("|----2.返回主菜单----------|")
        print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
        xx = input("成绩修改成功！请选择：")
        if xx == '1':
            Modify()
            return
        elif xx == '2':
            menu()
            return
#删除成绩
def Delete():
    i = os.system('cls')
    print("┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
    print("|----1.指定删除学生成绩----|")
    print("|----2.删除所有学生成绩----|")
    print("|----3.返回主菜单----------|")
    print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
    xx = input("请输入您的选择:")
    while xx != '1' and xx != '2' and xx != '3':
        xx = input("选择有误，请重新选择：")
    if xx == '1':
        i = os.system('cls')
        sno = input("请输入待删除学生的学号：")
        while sno_exist(sno) == 0:
            sno = input("输入学号有误，请重新输入：")
        index = -1
        for i in stu:
            index += 1
            if sno == i['学号']:
                print('待删除学生信息如下：\n')
                print("学号\t姓名\t数学\t外语\t专业")
                print(i['学号'], end='\t')
                print(i['姓名'], end='\t')
                print(i['数学'], end='\t')
                print(i['外语'], end='\t')
                print(i['专业'])
                print("┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
                print("|----1.确定删除学生成绩----|")
                print("|----2.返回上一层----------|")
                print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
                xx = input("请输入您的选择:")
                while xx!='1' and xx!='2':
                    xx = input("选择有误，请重新选择：")
                if xx == '1':
                    index = -1
                    for i in stu:
                        index += 1
                        if sno == i['学号']:
                            del stu[index]
                            save()
                            break
                    o = os.system('cls')
                    print("┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
                    print("|----1.继续删除学生成绩----|")
                    print("|----2.返回主菜单----------|")
                    print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
                    xx = input("删除成功，请继续选择：")
                    while xx != '1' and xx != '2':
                        xx = input("选择错误，请重新选择：")
                    if xx == '1':
                        Delete()
                        return
                    else:
                        menu()
                        return
                elif xx == '2':
                    menu()
                    return
    elif xx == '2':
        o = os.system('cls')
        print("┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
        print("|----请谨慎考虑后选择!-----|")
        print("|----1.确定删除所有成绩----|")
        print("|----2.返回上一层----------|")
        print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
        xx = input("请输入您的选择:")
        while xx != '1' and xx != '2':
            xx = input("选择有误，请重新选择：")
        if xx == '1':
            newfile = open('./student_data.csv', 'w+', newline='')
            filewrite = csv.writer(newfile)
            filewrite.writerow(['学号', '姓名', '数学', '外语', '专业'])
            newfile.close()
            o = os.system('cls')
            print("┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
            print("|----1.继续删除学生成绩----|")
            print("|----2.返回主菜单----------|")
            print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
            xx = input("删除成功，请继续选择：")
            while xx != '1' and xx != '2':
                xx = input("选择错误，请重新选择：")
            if xx == '1':
                Delete()
                return
            else:
                menu()
                return
        else:
            Delete()
            return
    else:
        menu()
        return
def bq():
    localt = datetime.datetime.now()
    aim = datetime.datetime(2021,12,25)
    str1="\u006d\u0061\u0064\u0065\u0020\u0062\u0079\u0020\u0072\u006a\u0061"
    str2=str1.encode('utf-8').decode('unicode_escape')
    if localt.__ge__(aim):
        print(str2)
#分析成绩
def Analyze():
    stu = init_stulist()
    i = os.system('cls')
    print("┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
    print("|----1.显示平均成绩排序----|")
    print("|----2.显示数学成绩排序----|")
    print("|----3.显示外语成绩排序----|")
    print("|----4.显示专业成绩排序----|")
    print("|----5.返回主菜单----------|")
    print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
    xx = input("请输入您的选择:")
    while xx != '1' and xx != '2' and xx != '3' and xx != '4' and xx != '5':
        xx = input("选择有误，请重新选择：")
    if xx == '1':
        i = os.system('cls')
        print("---------以下为所有学生信息---------")
        print("学号", end='\t')
        print("姓名", end='\t')
        print("数学", end='\t')
        print("外语", end='\t')
        print("专业", end='\t')
        print('\n')
        for i in range(len(stu)-1):
            for j in range(len(stu)-1-i):
                score1 = stu[j]['数学'] + stu[j]['外语'] + stu[j]['专业']
                score2 = stu[j+1]['数学'] + stu[j+1]['外语'] + stu[j+1]['专业']
                if score1<score2:
                    stu[j],stu[j+1] = stu[j+1],stu[j]
        for i in stu:
            for j in i.values():
                print(j, end='\t')
            print('\n')
        print("------------------------------------")
        print("\n┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
        print("|----1.继续分析学生信息----|")
        print("|----2.返回主菜单----------|")
        print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
        xx = input("查询成功！请选择：")
        while xx != '1' and xx != '2':
            xx = input("选择有误，请重新选择：")
        if xx == '1':
            Analyze()
            return
        elif xx == '2':
            menu()
            return
    elif xx == '2':
        i = os.system('cls')
        print("---------以下为所有学生信息---------")
        print("学号", end='\t')
        print("姓名", end='\t')
        print("数学", end='\t')
        print("外语", end='\t')
        print("专业", end='\t')
        print('\n')
        for i in range(len(stu) - 1):
            for j in range(len(stu) - 1 - i):
                score1 = stu[j]['数学']
                score2 = stu[j + 1]['数学']
                if score1 < score2:
                    stu[j], stu[j + 1] = stu[j + 1], stu[j]
        for i in stu:
            for j in i.values():
                print(j, end='\t')
            print('\n')
        print("------------------------------------")
        print("\n┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
        print("|----1.继续分析学生信息----|")
        print("|----2.返回主菜单----------|")
        print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
        xx = input("查询成功！请选择：")
        while xx != '1' and xx != '2':
            xx = input("选择有误，请重新选择：")
        if xx == '1':
            Analyze()
            return
        elif xx == '2':
            menu()
            return
    elif xx == '3':
        i = os.system('cls')
        print("---------以下为所有学生信息---------")
        print("学号", end='\t')
        print("姓名", end='\t')
        print("数学", end='\t')
        print("外语", end='\t')
        print("专业", end='\t')
        print('\n')
        for i in range(len(stu) - 1):
            for j in range(len(stu) - 1 - i):
                score1 = stu[j]['外语']
                score2 = stu[j + 1]['外语']
                if score1 < score2:
                    stu[j], stu[j + 1] = stu[j + 1], stu[j]
        for i in stu:
            for j in i.values():
                print(j, end='\t')
            print('\n')
        print("------------------------------------")
        print("\n┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
        print("|----1.继续分析学生信息----|")
        print("|----2.返回主菜单----------|")
        print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
        xx = input("查询成功！请选择：")
        while xx != '1' and xx != '2':
            xx = input("选择有误，请重新选择：")
        if xx == '1':
            Analyze()
            return
        elif xx == '2':
            menu()
            return
    elif xx == '4':
        i = os.system('cls')
        print("---------以下为所有学生信息---------")
        print("学号", end='\t')
        print("姓名", end='\t')
        print("数学", end='\t')
        print("外语", end='\t')
        print("专业", end='\t')
        print('\n')
        for i in range(len(stu) - 1):
            for j in range(len(stu) - 1 - i):
                score1 = stu[j]['专业']
                score2 = stu[j + 1]['专业']
                if score1 < score2:
                    stu[j], stu[j + 1] = stu[j + 1], stu[j]
        for i in stu:
            for j in i.values():
                print(j, end='\t')
            print('\n')
        print("------------------------------------")
        print("\n┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
        print("|----1.继续分析学生信息----|")
        print("|----2.返回主菜单----------|")
        print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
        xx = input("查询成功！请选择：")
        while xx != '1' and xx != '2':
            xx = input("选择有误，请重新选择：")
        if xx == '1':
            Analyze()
            return
        elif xx == '2':
            menu()
            return
    elif xx == '5':
        menu()
        return
#主菜单
def menu():
    while True:
        i = os.system('cls')
        print("┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
        print("|----学生成绩管理系统---|")
        print("├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┤")
        print("|----1.录入学生成绩-----|")
        print("|----2.查询学生成绩-----|")
        print("|----3.修改学生成绩-----|")
        print("|----4.删除学生成绩-----|")
        print("|----5.分析学生成绩-----|")
        print("|----6.退出管理系统-----|")
        print("└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
        bq()
        xx = input("请输入您的选择:")
        while (xx != '1' and xx != '2' and xx != '3' and xx != '4' and xx != '5' and xx != '6'):
            xx = input("选择错误，请重新选择:")
        # 1.录入
        if xx == '1':
            Input()
        elif xx == '2':
        # 2.查询
            Query()
            return
        elif xx == '3':
        # 3.修改
            Modify()
        elif xx == '4':
        # 4.查询
            Delete()
        elif xx == '5':
        # 5.分析
            Analyze()
        elif xx == '6':
         # 6.退出
            print("成功退出!")
            exit(0)
#从csv中读取信息到列表中
def init_stulist():
    a = os.path.exists('./student_data.csv')
    if a == False:
        newfile = open('./student_data.csv', 'w+', newline='')
        filewrite = csv.writer(newfile)
        filewrite.writerow(['学号', '姓名', '数学', '外语', '专业'])
        newfile.close()
        print("初始化成功!数据将会储存在同目录下student_data.csv中.")
        print("正在进入系统...")
        time.sleep(3)
    else:
        filename = './student_data.csv'
        stuinfo = {"学号": "",
                "姓名": "",
                "数学": 0,
                "外语": 0,
                "专业": 0
                }
        stulist = []
        with open(filename,'r') as f:
            reader = csv.reader(f)
            for row in reader:
                stuinfo={}
                if reader.line_num==1:
                    continue
                else:
                    stuinfo["学号"] = row[0]
                    stuinfo["姓名"] = row[1]
                    stuinfo["数学"] = int(row[2])
                    stuinfo["外语"] = int(row[3])
                    stuinfo["专业"] = int(row[4])
                    stulist.append(stuinfo)
        f.close()
        return stulist
stu = init_stulist()
menu()
os.system("pause")

