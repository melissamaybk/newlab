#from django.test import TestCase

# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class ContactFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Chrome()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/')
    #find the elements you need to submit form
    contact_name = selenium.find_element_by_id('id_name')
    contact_job = selenium.find_element_by_id('id_job')
    contact_telephone = selenium.find_element_by_id('id_telephone')
    contact_mobile = selenium.find_element_by_id('id_mobile')

    submit = selenium.find_element_by_id('submit_button')

    #populate the form with data
    contact_name.send_keys('Melissa')
    contact_job.send_keys('student')
    contact_telephone.send_keys('04542243')
    contact_mobile.send_keys('76542485')

    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'Melissa' in selenium.page_source


