from django.db import models


class Gardner(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    social_number = models.CharField(max_length=20)
    nation_id = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.first_name



class Employee(models.Model):
    EMPLOYEE_TYPE = (
        ("M", "ماهوار"),
        ("K", "کونترات")
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    social_number = models.CharField(max_length=20)
    nation_id = models.CharField(max_length=20)
    salary_per_month = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True, blank=True)
    salary_per_work = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True, blank=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to="employee/image", default="employee.jpg")


    def __str__(self) -> str:
        return self.first_name
    


class Order(models.Model):
    UNIT = (
        ("kg", "کیلو گرام"),
        ("ser", "سیر"),
        ("man", "من"),
        ("boji", "بوجی"),
    )
    STATUS = (
        ("phase_1", "خریداری"), 
        ("phase_2", "دسته بندی"),
        ("phase_3", "فروش")
    )
    product_name = models.CharField(max_length=255)
    gardner = models.ForeignKey(Gardner, on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    qty = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    unit = models.CharField(max_length=10, choices=UNIT, default="kg")
    stauts =  models.CharField(max_length=20, choices=STATUS, default="phase_2")
    location = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(null=True, blank=True)


    def __str__(self) -> str:
        return self.product_name


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    UNIT = (
        ("kg", "کیلو گرام"),
        ("ser", "سیر"),
        ("man", "من"),
        ("boji", "بوجی"),
        ("cartoon", "کارتن"),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    qty = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    unit = models.CharField(max_length=20, choices=UNIT, default="kg")


    def __str__(self):
        return self.product_name


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    

    def __str__(self) -> str:
        return self.first_name


class Sale(models.Model):
    UNIT = (
        ("kg", "کیلو گرام"),
        ("ser", "سیر"),
        ("man", "من"),
        ("boji", "بوجی"),
        ("cartoon", "کارتن"),
    )
    EXCHANGE = (
        ("usd", "دالر"), 
        ("euro", "یورو"), 
        ("pk", "کلدار"), 
        ("ir", "تومن"), 
        ("afg", "افغانی"), 
        ("yen", "ین چین"), 
    )
    SALE_TYPE = (
        ("export", "صادرات"), 
        ("internal",  "داخلی")
    )
    sale_type = models.CharField(max_length=20, choices=SALE_TYPE, default="export")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    unit = models.CharField(max_length=20, choices=UNIT, default="kg")
    price_per_unit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    price_in_letter = models.CharField(max_length=200)
    get_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    unit_price = models.CharField(max_length=20, choices=EXCHANGE, default="afg")
    created_at = models.DateField()

