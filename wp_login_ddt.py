from selenium import webdriver
import unittest
import time
from ddt import ddt,data,file_data,unpack

@ddt
class WpLoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("start testing")
		cls.dr = webdriver.Chrome()
		cls.dr.get("http://47.107.76.72:8000/wp-login.php")
		cls.dr.implicitly_wait(5)
		cls.dr.maximize_window()

	@classmethod
	def tearDownClass(cls):
		print("end test")
		cls.dr.quit()

	def test_login_success(self):
		username = 'ZJM128'
		password = 'pass2word'
		self.by_id('user_login').clear()
		self.by_id("user_login").send_keys(username)
		self.by_id('user_pass').clear()
		self.by_id("user_pass").send_keys(password)
		self.by_id("wp-submit").click()
		time.sleep(3)
		self.assertTrue('wp-admin' in self.dr.current_url)

	@file_data("test_login.json")
	def test_login_failed(self,username,password,message):
		self.by_id('user_login').clear()
		self.by_id("user_login").send_keys(username)
		self.by_id('user_pass').clear()
		self.by_id("user_pass").send_keys(password)
		self.by_id("wp-submit").click()
		try:
			assert self.by_id("login_error").text
			try:
				err_msg = self.by_id("login_error").text
				print(err_msg)
				self.assertEqual(err_msg,message)
				time.sleep(1)
			except:
				print("提示信息与预期不符！")
		except:
			print("用户名和密码为空")

	def by_id(self,the_id):
		return self.dr.find_element_by_id(the_id)



if __name__ == "__main__":
	unittest.main()

