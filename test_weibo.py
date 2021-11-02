from time import sleep
from unittest import TestCase
from appium import webdriver


class TestLogin(TestCase):

    def setUp(self) -> None:
        self.desired_caps = {
            'platformName': 'Android',  # 手机测试平台
            'platformVersion': '10',     # 系统版本
            'deviceName': 'x',   # 设备名,127.0.0.1:62001 安卓手机可以随便填,模拟器不行
            'appPackage': 'com.sina.weibo',       # tv.danmaku.bili
            'appActivity': 'com.sina.weibo.SplashActivity',      # tv.danmaku.bili.MainActivityV2
            'unicodeKeyboard': True,
            'resetKeyBoard': True,
            'noReset': False,
            'newCommandTimeout': 6000
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        sleep(5)
        self.driver.quit()

    def test_login(self):
        try:
            protocol = self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]')
        except Exception:
            pass
        else:
            if protocol:
                protocol.click()

        # 跳过按钮
        try:
            el1 = self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView')
        except Exception:
            pass
        else:
            if el1:
                el1.click()

        # 访问
        try:
            el2 = self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[2]')
        except Exception:
            pass
        else:
            if el2:
                el2.click()

        # 登录按钮
        login_btn = self.driver.find_element_by_id('titleBack')
        login_btn.click()
        # 用户协议
        user_proto = self.driver.find_element_by_id('iv_login_view_protocol')
        user_proto.click()
        # qq
        qq_btn = self.driver.find_element_by_id('iv_qq')
        qq_btn.click()
        qq1 = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.ImageView')
        qq1.click()
        qq_authorization = self.driver.find_element_by_accessibility_id('QQ授权登录')
        qq_authorization.click()
        sleep(5)
        switch = self.driver.find_element_by_accessibility_id('我')
        switch.click()
        sleep(3)
        expect = self.driver.find_element_by_android_uiautomator('.text("我的相册")')
        self.assertTrue(expect)
        # print(expect)




