from selenium import webdriver
import unittest
import time
import json

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

	'''
	def test_create(self):
		self.login('ZJM128','pass2word')
		self.dr.get('http://47.107.76.72:8000/wp-admin/edit.php')
		self.by_css(".page-title-action").click()
		time.sleep(1)
		set_title = "create post %s" %(time.strftime('%Y%m%d%H%M%S'))
		self.by_id("title").send_keys(set_title)
		self.set_content("this is the post body")
		time.sleep(1)
		self.by_id("publish").click()
		time.sleep(2)
		self.dr.get('http://47.107.76.72:8000/wp-admin/edit.php')
		post_list_title = self.by_css(".row-title").text
		self.assertTrue(post_list_title == set_title)
	'''

	def test_create_post(self):
		self.login('ZJM128','pass2word')
		self.goto_postlist_page()
		time.sleep(1)
		with open("test_data.json",'r') as data:
			load_list = json.load(data)
		for i in load_list:
			self.by_css(".page-title-action").click()
			time.sleep(1)
			post_title = i['title']
			post_content = i['content']
			self.by_id("title").send_keys(post_title)
			self.set_content(post_content)
			self.by_id("publish").click()
			time.sleep(2)
			self.goto_postlist_page()
			time.sleep(2)
			post_list_title = self.by_css(".row-title").text
			self.assertEqual(post_title,post_list_title)


	def goto_postlist_page(self):
		self.dr.get("http://47.107.76.72:8000/wp-admin/edit.php")

	def login(self,username,password):

		self.by_id("user_login").send_keys(username)
		self.by_id("user_pass").send_keys(password)
		self.by_id("wp-submit").click()
		time.sleep(2)

	def set_content(self, text):
		js = 'document.getElementById("content_ifr").contentWindow.document.body.innerHTML="%s"' %(text)
		self.dr.execute_script(js)


	def by_id(self,the_id):
		return self.dr.find_element_by_id(the_id)

	def by_css(self,selector):
		return self.dr.find_element_by_css_selector(selector)



if __name__ == "__main__":
	unittest.main()