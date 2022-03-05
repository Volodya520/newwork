import os
import sys
import yaml
from selenium import webdriver
import pytest, time
from newwork.page.main import LoginPage, Searchproduct, Addproduct, Increasenumbers, Locatorreducenumbers, DeleteBasket,Shoppingbasket
import allure

# def get_par_path():
#     return os.path.abspath(os.path.join(os.getcwd(),"../"))
#     # root_path = os.path.abspath("../")
#     # 返回的就是根路径
# sys.path.append(get_par_path())

# print(get_par_path())
@pytest.fixture(scope="module")
def driver():
    # a = get_par_path() + "\chromedriver.exe"
    # print(get_par_path() + "\chromedriver.exe")
    driver1 = webdriver.Chrome(r"E:\\python2104\\自动化代码\newwork\\test_page\\chromedriver.exe")
    driver1.implicitly_wait(15)
    yield driver1
    driver1.quit()
# @pytest.mark.parametrize("test_data1",yaml.safe_load(open(get_par_path()+"\\test_page\\test_main.yml")))

@allure.epic("登陆")
@pytest.mark.parametrize("test_data1",yaml.safe_load(open(r"E:\python2104\自动化代码\newwork\test_page\test_main.yml")))
# 初始化登录页面
def test_login(driver,test_data1):
    Login_page=LoginPage(driver)
    driver.get("http://124.223.23.70:3000/#/login")
    with allure.step("去掉弹窗"):
        Login_page.popclick()
    with allure.step("输入账号"):
        Login_page.input_email(test_data1["email"])
    with allure.step("输入密码"):
        Login_page.input_password(test_data1["password"])
    with allure.step("点击按钮"):
        Login_page.input_click()

@allure.epic("搜索")
# 搜索产品
# @pytest.mark.parametrize("test_data1",yaml.safe_load(open(get_par_path()+"\\test_page\\test_main.yml")))
@pytest.mark.parametrize("test_data1",yaml.safe_load(open("test_main.yml")))
def test_searchproduct(driver, test_data1):
    searchproduct = Searchproduct(driver)
    searchproduct.searchproduct1(test_data1["search_items"])
    # allure.attach.file("1.png",attachment_type=allure.attachment_type.PNG)

@allure.epic("添加产品")
# 添加产品
def test_addproduct(driver):
    add_product = Addproduct(driver)
    add_product.add_product()

@allure.epic("点击购物车")
# 点击购物车
def test_Shoppingbasket(driver):
    put_basket0=Shoppingbasket(driver)
    put_basket0.cat_shopping()

@allure.epic("增加商品数量")
# 增加商品数量
def test_increateBasket(driver):
    put_Basket1 = Increasenumbers(driver)
    put_Basket1.increat_numbers()

@allure.epic("减少商品数量")
def test_reduceBasket(driver):
    put_Basket2 = Locatorreducenumbers(driver)
    put_Basket2.reduce_numbers()

@allure.epic("删除商品")
# 删除
def test_delete_product(driver):
    delete_product =DeleteBasket(driver)
    delete_product.deletebasket()


