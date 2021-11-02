from appium import webdriver
from time import sleep


desired_caps = {
    'platformName': 'Android',  # 手机测试平台
    'platformVersion': '10',     # 系统版本
    'deviceName': 'x',   # 设备名,127.0.0.1:62001 安卓手机可以随便填,模拟器不行
    'appPackage': 'com.sina.weibo',       # tv.danmaku.bili
    'appActivity': 'com.sina.weibo.SplashActivity',      # tv.danmaku.bili.MainActivityV2
    'unicodeKeyboard': False,
    'resetKeyBoard': False,
    'noReset': False,
    'newCommandTimeout': 6000
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
# 同意使用协议
try:
    protocol = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]')
except Exception:
    pass
else:
    if protocol:
        protocol.click()

# 跳过按钮
try:
    el1 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView')
except Exception:
    pass
else:
    if el1:
        el1.click()

# 访问
try:
    el2 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[2]')
except Exception:
    pass
else:
    if el2:
        el2.click()


# 登录按钮
login_btn = driver.find_element_by_id('titleBack')
login_btn.click()
# 用户协议
user_proto = driver.find_element_by_id('iv_login_view_protocol')
user_proto.click()
# qq
qq_btn = driver.find_element_by_id('iv_qq')
qq_btn.click()
qq1 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.ImageView')
qq1.click()
qq_authorization = driver.find_element_by_accessibility_id('QQ授权登录')
qq_authorization.click()

input('###')
driver.quit()

