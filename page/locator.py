from selenium.webdriver.common.by import By

# 关闭弹窗按钮定位
class Pop_up_window(object):
    distmiss=(By.XPATH,'//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
    
# 登录页面信息定位
class Locator_Login(object):
    email=(By.ID,"email")
    password=(By.ID,"password")
    loginButton=(By.ID,"loginButton")
    Account=(By.ID,"navbarAccount")
    logoutButton=(By.ID,"navbarLogoutButton")

# 添加商品按钮定位
class Locator_Add_product(object):
    addproduct=(By.XPATH,'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/div[2]/mat-grid-list/div/mat-grid-tile[1]/div/mat-card/div[2]/button')

# 搜索商品部分定位
class Locator_Search(object):
    search=(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/mat-search-bar/span/mat-icon[2]")
    inputsearch=(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/mat-search-bar/mat-form-field/div/div[1]/div/input")

#进入购物车页面按钮定位
class Locator_shopping_basket(object):
    shopping_basket = (By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]")

# 增加商品数量
class Locatoe_increasenumbers(object):
    increatnumber = (By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-basket/mat-card/app-purchase-basket/mat-table/mat-row/mat-cell[3]/button[2]")


# 减少商品数量
class Locator_reducenumbers(object):
    reducenumbers=(By.XPATH,"html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-basket/mat-card/app-purchase-basket/mat-table/mat-row[1]/mat-cell[3]/button[1]")

# 删除商品
class Locator_deletep_product(object):
    delete_basket = (By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-basket/mat-card/app-purchase-basket/mat-table/mat-row/mat-cell[5]/button")