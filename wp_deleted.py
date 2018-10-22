from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class WpCreatePost(unittest.TestCase):

	def setUp(self):
		print("start testing")
		self.dr = webdriver.Chrome()
		self.dr.get('http://47.107.76.72:8000/wp-login.php')
		self.dr.implicitly_wait(5)
		self.dr.maximize_window()

	def tearDown(self):
		print("end test")
		self.dr.quit()

	def test_delete(self):
		self.login('ZJM128','pass2word')
		title = 'create post %s' %(time.strftime('%Y%m%d%H%M%S'))
		content = 'testing post body'
		post_id = self.get_postid(title,content)
		self.dr.get('http://47.107.76.72:8000/wp-admin/edit.php')
		time.sleep(1)
		row_id = 'post-'+ post_id
		delete_title = self.by_id(row_id)
		ActionChains(self.dr).move_to_element(delete_title).perform()
		delete_title.find_element_by_css_selector('a.submitdelete').click()

		with self.assertRaises(NoSuchElementException):
			self.by_css(row_id)



	def login(self,username,password):

		self.by_id("user_login").send_keys(username)
		self.by_id("user_pass").send_keys(password)
		self.by_id("wp-submit").click()
		time.sleep(2)

	def get_postid(self,title,content):
		self.create(title,content)
		return self.dr.current_url.split('=')[1].split('&')[0]

	def create(self,title,content):
		self.dr.get('http://47.107.76.72:8000/wp-admin/edit.php')
		self.by_css(".page-title-action").click()
		time.sleep(1)
		self.by_id("title").send_keys(title)
		self.set_content(content)
		self.by_id("publish").click()
		time.sleep(1)
		

	def set_content(self, content):
		js = 'document.getElementById("content_ifr").contentWindow.document.body.innerHTML="%s"' %(content)
		#print(js)
		self.dr.execute_script(js)

	

	def by_id(self,the_id):
		return self.dr.find_element_by_id(the_id)

	def by_css(self,selector):
		return self.dr.find_element_by_css_selector(selector)



if __name__ == "__main__":
	unittest.main()