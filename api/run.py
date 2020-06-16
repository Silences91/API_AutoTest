import unittest
from api import Normal_01
import HTMLTestReportCN


if __name__ == '__main__':
    #第一种加载方式 单独加载  缺点：用例多的时候 加载不方便
    # suit = unittest.TestSuite()
    # suit.addTest(Normal_01.Normal_01('test_normal_01'))
    # suit.addTest(Normal_01.Normal_01('test_normal_02'))
    # suit.addTest(Normal_01.Normal_01('test_normal_03'))
    # suit.addTest(Normal_01.Normal_01('test_normal_04'))
    # unittest.TextTestRunner().run(suit)  #测试运行器-TestRunner
    # #第二种加载方式 按路径搜索加载
    #先将需要运行的用例.py文件修改为test开头的名称 再通过TestLoader搜索 加载运行用例
    # suit = unittest.defaultTestLoader.discover(start_dir='./')#测试加载器
    # unittest.TextTestRunner().run(suit)
    from xml.etree import ElementTree as ET  # 通过引用该方法可实现动态读取和写入xml
    et = ET.parse('./config.xml') #将xml文件读取成一个树形结构
    li = et.findall('./cases/*')#将读取的内容读取到一个列表
    suite = unittest.TestSuite()
    for i in li:
        class_name = i.tag.split('-')[0]
        method_name = i.tag.split('-')[1]
        exec('import %s' % class_name)#配置抽离  动态引包 动态加载配置 动态执行用例
        exec("suite.addTest(%s.%s('test_%s'))" % (class_name,class_name,method_name))  #文件名.类名.方法名
    # unittest.TextTestRunner().run(suite)
    HTMLTestReportCN.HTMLTestRunner(stream=open('./Demo_Report.html','wb'),verbosity=1,title ='接口自动化练习',description = '第一个接口自动化项目练习~',tester = 'chdongy').run(suite)

