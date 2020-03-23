# 易班自动操作 从账号csv文件中导入账号密码，自动切换到登录，手动选择操作，可自动发布投票，自动发布话题，自动投票
import time
import datetime
from random import randint
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd


def login_yiban(account_str, password_str):
    url = "http://www.yiban.cn/"
    browser.get(url)
    time.sleep(2)

    browser.find_element_by_xpath('//*[@id="y-user-account"]/span/a[2]').click()

    browser.find_element_by_id('account-txt').send_keys(account_str)
    browser.find_element_by_id('password-txt').send_keys(password_str)
    browser.find_element_by_xpath('//*[@id="login-btn"]').click()  # 登录易班

    # code = input("请输入验证码")
    # browser.find_element_by_id('login-captcha').send_keys(code)
    # browser.find_element_by_xpath('//*[@id="login-btn"]').click()  # 登录易班
    """try:
        verifycode = browser.find_element_by_xpath('//*[@id="login-captcha"]')
        code = input("输入图片验证码：")
        verifycode.send_keys(str(code))
        browser.find_element_by_xpath('//*[@id="login-btn"]"]').click() # 登录易班
    except:pass"""
    browser.maximize_window()
    return


def publish_votes(user_name, n):
    for j in range(n):
        time.sleep(3)
        browser.find_element_by_id('y-publish').click()  # 点击发布按钮
        browser.find_element_by_xpath('//*[@id="i-publish"]/li[2]/a/i').click()
        current_window = browser.current_window_handle
        handles = browser.window_handles
        time.sleep(1)
        browser.switch_to_window(handles[3])
        print(browser.title)
        time.sleep(1)

        browser.find_element_by_xpath('/html/body/main/div/section/div[1]/div/div[1]/div[1]/input').send_keys(
            user_name + '今日话题之' + vote_topics[randint(0, 25)])
        browser.find_element_by_xpath('/html/body/main/div/section/div[1]/div/ul[1]/li[1]/div[1]/input').send_keys(vote_options[randint(0, 17)]*randint(1, 3))
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/main/div/section/div[1]/div/ul[1]/li[2]/div/input').send_keys(vote_options[randint(0, 17)]*randint(1, 3))
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/main/div/section/div[1]/div/ul[1]/li[3]/div/input').send_keys(vote_options[randint(0, 17)]*randint(1, 3))
        js = "var q=document.documentElement.scrollTop=100000"
        browser.execute_script(js)
        time.sleep(2)

        browser.find_element_by_xpath('/html/body/main/div/section/div[1]/div/div[3]/ul[1]/li[1]').click()  # 选择范围
        browser.find_element_by_xpath('/html/body/main/div/section/div[1]/div/p[4]/input').click()  # 选择截止时间

        # a = datetime.datetime.now().strftime('%Y-%m-%d')
        # b = int(a[8] + a[9])

        # browser.find_element_by_xpath(
        #     '/html/body/main/div/section/div[1]/div/p[4]/div/div[3]/table/tbody/tr[2]/td[' + str(b) + ']').click()
        # browser.find_element_by_xpath('/html/body/main/div/section/div[1]/div/p[4]/div/div[3]/table/tbody/tr[4]/td[7]').move_by_offset(0, -1).click()

        browser.find_element_by_xpath('/html/body/main/div/section/div[1]/div/p[4]/div/div[3]/table/tbody/tr[3]/td[7]').click()
        browser.find_element_by_xpath(
            '/html/body/main/div/section/div[1]/div/p[4]/div/div[2]/table/tbody/tr/td/span[24]').click()
        browser.find_element_by_xpath(
            '/html/body/main/div/section/div[1]/div/p[4]/div/div[1]/table/tbody/tr/td/span[12]').click()
        print("选择时间完成")

        browser.find_element_by_xpath('/html/body/main/div/section/div[1]/div/p[5]/label/div/ins').click()  # 选择匿名
        print("选择匿名完成")
        browser.find_element_by_xpath('/html/body/main/div/section/div[1]/div/p[6]/label/div/ins').click()  # 取消验证码
        print("取消验证码完成")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/main/div/section/div[2]/div/div/a').click()  # 发布投票
        print("第%d次发布投票完成" % (j+1))

        time.sleep(2)
        browser.find_element_by_class_name('btn_chs').click()  # 选择投票
        browser.find_element_by_xpath('//*[@id="fm_vote"]/a[1]').click()  # 点击投票
        print("投票完成")

        time.sleep(1)
        browser.find_element_by_xpath('/html/body/main/div/div/div[2]/aside/section/div/div/div/input').send_keys(
            comments[randint(0, 11)])  # 写评论
        browser.find_element_by_xpath('/html/body/main/div/div/div[2]/aside/section/div/div/div/a').click()  # 点击评论
        print("评论完成")
        time.sleep(2)
        browser.close()
        browser.switch_to_window(handles[0])
        print(browser.title+"第%d次操作完成！" % (j+1))

    browser.quit()
    return


def publish_topics(user_name, n):
    for j in range(n):
        time.sleep(3)
        browser.find_element_by_id('y-publish').click()  # 点击发布按钮
        browser.find_element_by_xpath('//*[@id="i-publish"]/li[1]/a/b').click()  # 点击话题

        current_window = browser.current_window_handle
        handles = browser.window_handles
        # time.sleep(3)
        # browser.switch_to_window(handles[0])
        # print(browser.title)

        # time.sleep(3)
        # browser.switch_to_window(handles[1])
        # print(browser.title)

        # time.sleep(3)
        # browser.switch_to_window(handles[2])
        # print(browser.title)

        time.sleep(3)
        browser.switch_to_window(handles[3])
        print(browser.title)

        browser.find_element_by_xpath('/html/body/main/div/section/div[1]/div/p/input').send_keys(user_name + '今日话题之'+ topics_[randint(0, 5)])

        iframe = browser.find_element_by_id('ueditor_0')
        browser.switch_to_frame(iframe)

        browser.find_element_by_xpath('/html/body').send_keys("好久不见，最近还好吗？\n 还没有内容喔~！")
        time.sleep(3)

        browser.switch_to.default_content()
        browser.find_element_by_xpath('/html/body/main/div/section/div[1]/div/div[3]/ul[1]/li[1]/label').click()
        browser.find_element_by_xpath('/html/body/main/div/section/div[2]/div/div/a[2]').click()  # 话题发布完成
        print("第%d条话题发布完成" % (j + 1))

        browser.implicitly_wait(5)
        # time.sleep(3)
        browser.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div[2]/a/span[1]').click()  # 点赞
        print("点赞完成")
        time.sleep(3)
        # 评论出现bug
        # browser.find_element_by_tag_name('textarea').send_keys("调试多次还是无法自动评论")
        #
        # browser.find_element_by_class_name('iconfont_forum').click()
        # browser.find_element_by_class_name('iconfont_forum').click()  # 评论
        # browser.implicitly_wait(5)
        #
        # time.sleep(2)
        # print("评论完成")
        browser.close()
        browser.switch_to_window(handles[0])
        print(browser.title)
    browser.quit()
    return


def load_account(filename):
    df = pd.read_csv(filename)
    length = df.shape[0]
    user_list = df['用户']
    account_list = df['账号']
    password_list = df['密码']
    return user_list, account_list, password_list


def user_vote(user_name, m):
    browser.find_element_by_class_name('guide-4').click()
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[@id="sub-nav"]/div/ul[1]/li[2]/a').click()
    browser.find_element_by_class_name('guide-delete').click()
    time.sleep(1.5)
    browser.find_element_by_xpath('//*[@id="waterfall"]/div/figure/figcaption/a/span').click()
    js1 = "var q=document.documentElement.scrollTop=100000"
    browser.execute_script(js1)
    time.sleep(0.5)

    browser.find_element_by_xpath('/html/body/main/div/div/div/div[1]/section[4]/header/a').click()
    time.sleep(2)
    current_window = browser.current_window_handle
    handles = browser.window_handles
    time.sleep(1)
    browser.switch_to_window(handles[3])
    print("3：" + browser.title)

    # js2 = "document.body.style.zoom='0.8'" # 缩小窗口
    # browser.execute_script(js2)
    for j in range(m):
        for i in range(1, 11):  # 从本页的第一个投票开始投起
            browser.find_element_by_xpath(
                '/html/body/main/div/div/div/div[1]/section[2]/ul/li[' + str(i) + ']/div/div[1]/span[1]/a').click()
            current_window = browser.current_window_handle
            handles = browser.window_handles
            time.sleep(1)
            browser.switch_to_window(handles[4])
            print("进入" + browser.title)
            browser.find_element_by_class_name('btn_chs').click()  # 选择投票 str(randint(1, 3))
            browser.find_element_by_xpath('//*[@id="fm_vote"]/a[1]').click()  # 点击投票
            print(browser.title + "投票完成")

            time.sleep(1)
            browser.find_element_by_xpath('/html/body/main/div/div/div[2]/aside/section/div/div/div/input').send_keys(
                comments[randint(0, 11)])  # 写评论
            browser.find_element_by_xpath('/html/body/main/div/div/div[2]/aside/section/div/div/div/a').click()  # 点击评论
            print(browser.title + "评论完成")
            time.sleep(1)
            browser.close()
            browser.switch_to_window(handles[3])
            time.sleep(0.5)

        print('第一页投票已完成')
        time.sleep(1)
        browser.switch_to_window(handles[3])
        browser.execute_script(js1)
        time.sleep(0.5)
        browser.find_element_by_class_name('next').click()
        time.sleep(2)

    browser.quit()
    print(user_name + '已完成%d页投票' % m)


action = input('请输入您要进行的操作（发布话题、发布投票、投票）')

vote_topics = ['聚餐吃什咩呀', '英语阅读打卡', '每日读书打卡', '运动打卡', '每日跑步打卡', '每日呼吸打卡', '每日思考打卡', '开学后最想做什咩！', '英语四六级', '数值计算方法', '空间探测原理', '大学英语', '热力学与统计物理', '地球物理学基础', '空间物理学', 'C语言', 'Matlab', '高等数学', '线性代数', '数学物理方程', '数字电子技术', '数据结构与方法','思想道德修养', '大学计算机基础', '聚餐吃啥呀！', '每日一题']
vote_options = ["你好哇！", "有意思！", '有内味了！', "但我不能为你点赞QAQ", '666！', "三班最棒！", "吃了吗！", "好想你们哦~", "晚安安~", '空科！~', '999', '哇哈哈ૢ˃ꌂ˂ૢ)', 'A', 'B', 'C', 'D', '太难了！', '我不会！', '˃ꌂ˂ૢ)', 'A', 'B', 'C', 'D', '太难了！', '我不会！']
comments = ['赞赞赞！', '收到了！', '好的呢~',  '真好玩！', '你是魔鬼吧！', '嘿嘿嘿！', '猜猜我是谁', '有意思', '不错哦~~', 'good!', 'great!', 'nice!']
topics_ = ['每日暖心一句', '每日学英语', '每日故事分享', '每日一笑', '每日美食', '历史上的今天']


if action == '发布投票':
    n = int(input("请输入单个账号发布投票的次数："))
    user_list, account_list, password_list = load_account('account_data.csv')

    cnt = 0
    for i in range(5):
        user = user_list[i]
        account = account_list[i]
        password = password_list[i]
        print(user+"正在登录")

        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('lang = zh_CN.UTF-8')
        UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        chrome_options.add_argument('User-Agent =' + UserAgent)
        browser = webdriver.Chrome(chrome_options=chrome_options)

        login_yiban(str(account), str(password))
        print(user+'登录成功')
        publish_votes(user, n)
        print(user+"已完成%d次发布投票！" % n)
        print("——————————————————————————")
        print('正在切换账号......')
        print(user+"已下线！")
        cnt = cnt + 1
        time.sleep(4)

    print("已结束，共有%d个账号完成%d次投票发布！" % (cnt, n))
    print("此次累计egpa增长为：%f" % (0.04*cnt*n))

elif action == '发布话题':
    n = int(input("请输入单个账号发布话题的次数："))
    user_list, account_list, password_list = load_account('account_data.csv')

    cnt = 0
    for i in range(3):
        user = user_list[i]
        account = account_list[i]
        password = password_list[i]
        print(user + "正在登陆")

        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('lang = zh_CN.UTF-8')
        UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        chrome_options.add_argument('User-Agent =' + UserAgent)
        browser = webdriver.Chrome(chrome_options=chrome_options)

        login_yiban(str(account), str(password))
        print(user + '登录成功')
        publish_topics(user, n)
        print(user + "已完成%d次话题发布！" % n)
        print("——————————————————————————")
        print('正在切换账号......')
        print(user+"已下线！")
        cnt = cnt + 1
        time.sleep(4)

    print("已结束，共有%d个账号完成%d次话题发布！" % (cnt, n))
    print("此次累计egpa增长为：%f" % (0.02 * cnt * n))

elif action == '投票':
    n = int(input("请输入单个账号投票的页数："))
    user_list, account_list, password_list = load_account('account_data.csv')

    cnt = 0
    for i in range(3):
        user = user_list[i]
        account = account_list[i]
        password = password_list[i]
        print(user + "正在登陆")

        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('lang = zh_CN.UTF-8')
        UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        chrome_options.add_argument('User-Agent =' + UserAgent)
        browser = webdriver.Chrome(chrome_options=chrome_options)

        login_yiban(str(account), str(password))
        user_vote(user, n)
        print(user + "已完成%d次话题发布！" % n)
        print("——————————————————————————")
        print('正在切换账号......')
        print(user+"已下线！")
else:
    print('无此项操作！')

print("已成功结束,再见！")
