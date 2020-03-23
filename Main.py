import unittest
from base.HTMLTestRunner import HTMLTestRunner
import datetime
from base.Email import send_email

discover = unittest.defaultTestLoader.discover("./case/", pattern="TestCase_*.py")
file_path = './report/test_report_{0}.html'.format(datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S"))
with open(file_path, 'wb') as fp:
    runner = HTMLTestRunner(stream=fp, title='APP4.0 Test Report', description='****** Report Details ******')
    runner.run(discover)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    send_email("测试报告", content)
