#任务1：身份验证，定义变量
name = "全萃灵"
student_ID = "25250516308"
_class = "25级金融科技3班"
partner = ['庄','吴','刘']
instructor = "胡凡"
print(f"团队相关信息\n姓名: {name}\n学号:{student_ID}\n班级：{_class}\n团队成员：{partner}\n课程老师:{instructor}")
#任务2：拼接字符串
blocks = "SJ1"
room_number = "106"
pinyin_name = "quancuiling"
date = "12.10.2025"
key = blocks + room_number + pinyin_name.upper() + date
print(key)
#任务3：if-else
# 中芯国际验证
price = float(input("输入今日股票价格："))
avg_price = float(input("输入平均股票价格："))
volume = float(input("输入成交量："))
avg_volume = float(input("输入平均成交量："))
if price > avg_price and volume > avg_volume:
    print("突破信号，考虑买入。")
elif price < avg_price and volume > avg_volume:
    print("下跌放量，注意风险！")
elif price > avg_price and volume < avg_volume:
    print("下跌放量，注意风险！")
else:
    print("无明显信号")
#任务4：新建字典，建成被破坏后的形式
# 把课程对应的老师修改成准确的名字
# 补充另外一门课
class_schedule = {"大心":"???",
                  "大英":"???",
                  "湾财":"???",
                  "大语":"???",
                  "高数":"???",
                  }
class_schedule["大心"] = "鞠鑫"
class_schedule["大英"] = "邵丹"
class_schedule["湾财"] = "严丽君"
class_schedule["大语"] = "施永秀"
class_schedule["高数"] = "马丽"
class_schedule["宝石学"] = "罗勇"
print(class_schedule)
#任务5：新建 main_food 和 dishes 两个列表
# 分别包含食堂中的部分主食和菜品
main_food = ['米饭','粉面','面包']
dishes = ['帝王蟹','青龙','佛跳墙','乌鸡海参']
choose_main_food = main_food[0]
choose_dishes = dishes[:3]
print(f"你选择的套餐如下：\n主食:{choose_main_food} \n菜品:{choose_dishes}")
#任务 6：使用 input() 完成奶茶点单
milk_tea = input("奶茶品种：")
milk_tea_size = input("请选择：大杯 / 小杯")
milk_tea_temp = input("请选择：热 / 温 / 去冰 / 少冰 / 常温")
milk_tea_sugar_content = input("请选择：无糖 / 三分糖 / 五分糖 / 七分糖 / 全糖")
milk_tea_add = input("请选择：珍珠 / 椰果 / 布丁 / 不加")
print(f"你的diy奶茶好了，\n奶茶品种：{milk_tea}\n杯型：{milk_tea_size}\n温度：{milk_tea_temp}\n甜度：{milk_tea_sugar_content}\n加料：{milk_tea_add}")
#构建金融函数 —— 未来价值 FV 的计算
# 请你们定义函数 future_value(PV, r, n)
def future_value(PV, r, n):
    FV = PV*(1+r)**n
    return FV
FV_result = future_value(10000, 0.015, 3)
print("未来价值：",FV_result)
#任务 8：大巴乘车验证建立一个大巴乘车名单列表（不包含你们的姓名）
# 使用 for 循环遍历名单，判断自己是否在其中
# 如果不在，为了继续任务，你们需要将四个人的姓名添加进入列表
check_name = [name] + partner
name_list = ['王','张']
found_name = False
for existing_name in check_name:
    if existing_name == name_list:
        found_name = True
    break
if found_name:
    name_list.append(existing_name)
#任务 9：嵌套循环多用户登录系统
# 输入“姓名”作为账号，输入“学号”作为密码
#若账号密码匹配成功，则门自动打开。
#若密码连续输错三次，系统锁定，无法开门。
#四个人都必须完成登录，门才会解锁。
check_ID = [student_ID]+['1','2','3']
logged_in_number = 0
attempt = 0
while logged_in_number < 4:
    user = check_name[logged_in_number]
    print(f"用户 {user} 登录")
    while attempt < 3:
        accout = input("请输入你的名字：")
        key = input("请输入你的学号：")
        if accout == user and key == check_ID[logged_in_number]:
            print("登录成功！")
            logged_in_number += 1
            break
        else:
            attempt += 1
            if attempt < 3:
                print(f"密码错误！还有 {3 - attempt} 次机会")
            else:
                print(f"密码连续错误三次，用户 {user}不可以再登录")
        break
#请修复以下无限循环：
tasks = ["身份验证", "字符串拼接", "循环练习", "列表点餐", "登录验证", "金融函数", "终极测试"]
i=0
while i < len(tasks):
    run_task = tasks[i]
    print(run_task)
    i+=1
    if i > len(tasks):
        break