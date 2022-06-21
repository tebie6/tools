import ddddocr
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    login()


def login():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')                  # 无头模式
    browser = webdriver.Firefox(options=options)

    try:

        max_try = 1
        while max_try <= 3:

            print("第", max_try, "次尝试")

            # 打开页面
            browser.get("登录地址URL")
            print("打开页面")

            # 获取验证码
            captcha = browser.find_element(By.CSS_SELECTOR, '#imgcaptcha')
            # captcha.screenshot('/Users/liumingyu/project/tjprotnet_login/captcha.png')  # 将图片截屏并保存
            captcha.screenshot('/data/captcha.png')  # 将图片截屏并保存
            print("获取验证码")

            # 输入账号
            browser.find_element(By.CSS_SELECTOR, '#salingac2').clear()
            browser.find_element(By.CSS_SELECTOR, '#salingac2').send_keys('账号名称')
            print("输入账号")

            # 输入密码
            browser.find_element(By.CSS_SELECTOR, '#salingpd2').send_keys('密码')
            print("输入密码")

            # 输入验证码
            browser.find_element(By.CSS_SELECTOR, '#fmcaptcha').send_keys(verify_code_ocr())
            print("输入验证码")

            # 点击登录
            browser.find_element(By.CSS_SELECTOR, '#btnlogin').click()
            print("点击登录")

            time.sleep(2)

            # 保存cookie
            cookies = browser.get_cookies()

            cookie = {}
            for i in cookies:
                cookie[i["name"]] = i["value"]

            # 验证是否登录成功
            if cookie['ososid'] != "0":
                # with open("/Users/liumingyu/project/tjprotnet_login/cookies.txt", "w") as f:
                with open("/data/cookies.txt", "w") as f:
                    f.write(json.dumps(cookie))
                break

            max_try += 1

    except Exception as e:
        print(e)
    finally:
        browser.quit()
        print('OK')


def verify_code_ocr():
    ocr = ddddocr.DdddOcr(show_ad=False)

    # with open("/Users/liumingyu/project/tjprotnet_login/captcha.png", 'rb') as f:
    with open("/data/captcha.png", 'rb') as f:
        image = f.read()

    res = ocr.classification(image)
    print("识别验证码：" + res)

    return res


# 执行main函数
main()
