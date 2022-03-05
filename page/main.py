from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait




# 关闭弹窗按钮定位
from page.basepage1 import BasePage
from page.locator import Pop_up_window, Locator_Login, Locator_Search, Locator_Add_product, Locator_shopping_basket, \
    Locatoe_increasenumbers, Locator_reducenumbers, Locator_deletep_product


class LoginPage(BasePage):
    def popclick(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*Pop_up_window.distmiss)
        )
        self.driver.find_element(*Pop_up_window.distmiss).click()

    # 输入邮箱
    def input_email(self, data1):
        # def dw(driver):
        # return self.driver.find_element(By.ID, "lsdjf")
        # WebDriverWait(self.driver, 10).until(dw(self))
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*Locator_Login.email)
        )
        element = self.driver.find_element(*Locator_Login.email)
        element.click()
        element.clear()
        element.send_keys(data1)

    # 输入密码
    def input_password(self, data1):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*Locator_Login.password)
        )
        element = self.driver.find_element(*Locator_Login.password)
        element.click()
        element.send_keys(data1)

    # 点击登录
    def input_click(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*Locator_Login.loginButton)
        )
        self.driver.find_element(*Locator_Login.loginButton).click()


# 搜索商品
class Searchproduct(BasePage):
    def searchproduct1(self, data1):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*Locator_Search.search)
        )
        self.driver.find_element(*Locator_Search.search).click()
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*Locator_Search.inputsearch)
        )
        self.driver.find_element(*Locator_Search.inputsearch).send_keys(data1)
        self.driver.find_element(*Locator_Search.inputsearch).send_keys(Keys.ENTER)


# 添加商品
class Addproduct(BasePage):
    def add_product(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*Locator_Add_product.addproduct)
        )
        self.driver.find_element(*Locator_Add_product.addproduct).click()


#进入购物车页面按钮定位
class Shoppingbasket(BasePage):
    def cat_shopping(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*Locator_shopping_basket.shopping_basket)
        )
        self.driver.find_element(*Locator_shopping_basket.shopping_basket).click()


# 增加商品数量
class Increasenumbers(BasePage):

    def increat_numbers(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*Locatoe_increasenumbers.increatnumber)
        )
        self.driver.find_element(*Locatoe_increasenumbers.increatnumber).click()

# 减少商品数量
class Locatorreducenumbers(BasePage):
    def reduce_numbers(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*Locator_reducenumbers.reducenumbers)
        )
        self.driver.find_element(*Locator_reducenumbers.reducenumbers).click()
       
# 删除商品
class DeleteBasket(BasePage):
    def deletebasket(self):
        WebDriverWait(self.driver,10).until(
            lambda driver:self.driver.find_element(*Locator_deletep_product.delete_basket)
        )
        self.driver.find_element(*Locator_deletep_product.delete_basket).click()
        