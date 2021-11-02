from HTMLTestRunner import HTMLTestRunner
import unittest
import os
from threading import Thread


class LoginThread(Thread):
    def __init__(self, test_file, html_file, desc):
        super().__init__()
        self.test_file = test_file
        self.html_file = html_file
        self.desc = desc

    def run(self) -> None:
        runner = HTMLTestRunner.HTMLTestRunner(
            verbosity=1,
            title='登录测试',
            description=f'{self.desc}',
            stream=open(f'{self.html_file}', mode='w', encoding='utf-8')
        )

        runner.run(unittest.defaultTestLoader.discover(os.getcwd(), pattern=f'{self.test_file}'))


if __name__ == '__main__':
    login_weibo = LoginThread("test_weibo.py", '微博登录.html', 'appium登录微博')
    login_weibo.start()
    login_weibo.join()
