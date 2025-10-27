## Inventory Management System with Automated Web Testing using Python and Selenium
<small> This project is an Inventory Management System with Automated Web Testing that streamlines product tracking, stock updates, supplier management, and sales monitoring. The system ensures accuracy and efficiency through real-time inventory control and automated testing to validate core functionalities across workflows. This project has three types of users: admin, customer and employee. These are the features of this system for each type of users:
Customer: Buy products (three categories: clothes, electronics, food), add customer details.
Employee: Create new invoice, view all invoice list, delete invoice, view sales report, view due report, view out of stock product list. 
Admin: Add new product, view stock report.
Every type of user can do registration, login, logout, change Password and update profile. </small> 

Django follows the MVC (Model–View–Controller) pattern. Functionalities of view include displaying webpages, accepting requests from users, rendering webpages, etc. Functionalities of model include storing data in the database, fetching data from the database, deleting data, updating data, etc. The controller accepts the user request from the view. The controller fetches data from the model, and the model gives the requested data to the controller. The controller sends these requested data to the user through the view. The controller renders the requested webpage to the user through the view. In Django, urls.py performs the functionalities of the view of MVC, views.py performs both the functionalities of the view and controller of MVC, and models.py performs the functionalities of the model of MVC. In Django, when a user clicks on a link on a webpage, the system searches for that URL in the urls.py file. In the urls.py file, a function will be present corresponding to that URL. This function will be fully written in a particular views.py file. So, in Django, when a user clicks on a link on a webpage, the system finds that URL in urls.py, goes to its corresponding function (written in views.py), and performs the actions written in that function. 

### Final Result of Project
#### Login Page
<p align="center"><img src="./img/all/login1.jpg" alt="App Screenshot" style="height:370px; width:auto;"></p>
<p align="center"><img src="./img/all/login2.jpg" alt="App Screenshot" style="height:370px; width:auto;"></p>
django.contrib.auth is a built-in Django module that handles authentication related functionalities. auth_ views.LoginView is used to display the login form. This form will be shown in the login.html page when the user clicks on the login link.

#### Registration form for new users
<p align="center"><img src="./img/all/reg1.jpg" alt="App Screenshot" style="height:380px; width:auto;"></p>
<p align="center"><img src="./img/all/reg2.jpg" alt="App Screenshot" style="height:151px; width:auto;"></p>
In this registration page, when request.method=="POST", the data submitted through the form is received. UserRegistrationForm is used to take input from the user and if form. is_ valid() is true, the user information is saved in the database. The user type is also saved in the Usertype model. After that, the user is authenticated using authenticate (username =uname, password =psw) and the user is logged into the system using login (request, new_user), and finally redirected to the home page.

#### Front Page
<p align="center"><img src="./img/all/frontpg.jpg" alt="App Screenshot" style="height:300px; width:auto;"></p>

#### Update Profile
This page updates the user profile. Two forms are here in this page: UserUpdateForm and ProfileUpdateForm. When the form is submitted, request.method=="POST" checks whether the data is coming from the submitted form. Both forms are validated using is_valid() and then the submitted info are saved into the database. If there is any error, render (request, 'customer/ profileUpdate. html', context) is used to load the profile update page again and display the error.
<p align="center"><img src="./img/all/update_profile.jpg" alt="App Screenshot" style="height:300px; width:auto;"></p>

#### Change Password
django.contrib.auth is a built-in Django module that provides authentication functionalities such as login, logout, and password change. auth _views .PasswordChangeView is used to display the password change form and this form will be shown on the pass_change .html page when the user clicks on the 'change password' link. auth_ views .PasswordChangeDoneView is used to display the success message after the password is changed.
<p align="center"><img src="./img/all/chng_pass1.jpg" alt="App Screenshot" style="height:370px; width:auto;"></p>
<p align="center"><img src="./img/all/chng_pass2.jpg" alt="App Screenshot" style="height:250px; width:auto;"></p>

#### Log Out
django.contrib.auth is a built-in Django module that handles authentication functionalities. auth_ views.LogoutView is used to log the user out and it will show a logout message when the user clicks on the logout link.
<p align="center"><img src="./img/all/log_out.jpg" alt="App Screenshot" style="height:220px; width:auto;"></p>

### Admin
<p align="center"><img src="./img/admin/admin_work.jpg" alt="App Screenshot" style="height:300px; width:auto;"></p>

#### Adding New Product Form
<p align="center"><img src="./img/admin/add_new_product1.jpg" alt="App Screenshot" style="height:310px; width:auto;"></p>
<p align="center"><img src="./img/admin/add_new_product2.jpg" alt="App Screenshot" style="height:67px; width:200;"></p>

#### Stock Report
<p align="center"><img src="./img/admin/stock_report.jpg" alt="App Screenshot" style="height:300px; width:auto;"></p>

### Customer
#### Buy Products
<p align="center"><img src="./img/customer/buy_products.jpg" alt="App Screenshot" style="height:300px; width:auto;"></p>

#### Buy Clothes
<p align="center"><img src="./img/customer/buy_clothes.jpg" alt="App Screenshot" style="height:300px; width:auto;"></p>

#### Buy Electronics
<p align="center"><img src="./img/customer/buy_electronics.jpg" alt="App Screenshot" style="height:300px; width:auto;"></p>

#### Buy Food
<p align="center"><img src="./img/customer/buy_food.jpg" alt="App Screenshot" style="height:300px; width:auto;"></p>

#### Adding Customer Details Form
<p align="center"><img src="./img/customer/customer_info1.jpg" alt="App Screenshot" style="height:260px; width:auto;"></p>
<p align="center"><img src="./img/customer/customer_info2.jpg" alt="App Screenshot" style="height:175px; width:auto;"></p>

### Employee
<p align="center"><img src="./img/employee/emp_work.jpg" alt="App Screenshot" style="height:280px; width:auto;"></p>

#### Creating New Invoice Form
<p align="center"><img src="./img/employee/creating_invoice1.jpg" alt="App Screenshot" style="height:260px; width:auto;"></p>
<p align="center"><img src="./img/employee/creating_invoice2.jpg" alt="App Screenshot" style="height:204px; width:auto;"></p>

#### All Invoice List and Delete Invoice
<p align="center"><img src="./img/employee/all_invoice_list_and_del_invoice.jpg" alt="App Screenshot" style="height:310px; width:auto;"></p>

#### Sales Report
<p align="center"><img src="./img/employee/sales_report1.jpg" alt="App Screenshot" style="height:260px; width:auto;"></p>
<p align="center"><img src="./img/employee/sales_report2.jpg" alt="App Screenshot" style="height:180px; width:auto;"></p>

#### Due Report
<p align="center"><img src="./img/employee/due_report1.jpg" alt="App Screenshot" style="height:280px; width:auto;"></p>
<p align="center"><img src="./img/employee/due_report2.jpg" alt="App Screenshot" style="height:105px; width:auto;"></p>
<p align="center"><img src="./img/employee/due_report3.jpg" alt="App Screenshot" style="height:105px; width:auto;"></p>

#### Out of Stockn Product
<p align="center"><img src="./img/employee/out_of_stock_product1.jpg" alt="App Screenshot" style="height:280px; width:auto;"></p>
<p align="center"><img src="./img/employee/out_of_stock_product2.jpg" alt="App Screenshot" style="height:105px; width:auto;"></p>
<p align="center"><img src="./img/employee/out_of_stock_product3.jpg" alt="App Screenshot" style="height:110px; width:auto;"></p>






