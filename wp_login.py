from selenium import webdriver
import unittest
import time

class WpLoginTest(unittest.TestCase):

	def setUp(self):
		print("*****start testing*****")
		self.dr = webdriver.Chrome()
		self.dr.get("http://47.107.76.72:8000/wp-login.php")
		self.dr.implicitly_wait(5)
		self.dr.maximize_window()

	def tearDown(self):
		print("*****end testing*****")
		self.dr.quit()


	def test_login_success(self):

		username = 'ZJM128'
		password = 'pass2word'

		self.by_id("user_login").send_keys(username)
		self.by_id("user_pass").send_keys(password)
		self.by_id("wp-submit").click()
		time.sleep(3)

		self.assertTrue('wp-admin' in self.dr.current_url)

	def by_id(self,the_id):
		return self.dr.find_element_by_id(the_id)



if __name__ == "__main__":
	unittest.main()

