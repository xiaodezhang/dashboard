from django.db import models

# Create your models here.

#人员库
class people(models.Model):
    name = models.CharField('姓名',max_length = 150)
    phone_number = models.CharField('电话',max_length = 11,null = True)
    sex = models.CharField('性别',max_length = 5,null = True)

#人员基本信息表
class person(models.Model):
    name = models.CharField('姓名',max_length = 150)
    phone_number = models.CharField('电话',max_length = 11,null = True)
    sex = models.CharField('性别',max_length = 5,null = True)

#服务员信息
class waiter_info(models.Model):
    waiter = models.ForeignKey(person,on_delete = models.CASCADE,related_name = 'waiter_info')
    waiter_number = models.CharField('工号',max_length = 11)

#顾客信息
class customer_info(models.Model):
    customer = models.ForeignKey(person,on_delete = models.CASCADE,related_name = 'customer_info')

#区域管理信息
class area_management(models.Model):
    area_name = models.CharField('区域',max_length = 50)
    desk_number = models.CharField('桌台号',max_length = 50)
    area_customers_sum = models.IntegerField('区域容纳人数',null = True)

#收银终端
class cash_terminal(models.Model):
    cash_terminal_model = models.CharField('收银终端型号',max_length = 50,primary_key= True)

#收货人信息
class receiver_info(models.Model):
    receiver = models.ForeignKey(person,on_delete = models.CASCADE,related_name = 'receiver_info')

#配送人信息
class sender_info(models.Model):
    sender = models.ForeignKey(person,on_delete = models.CASCADE,related_name = 'sender_info')

#配送信息表
#TODO:address需要新建表
class shipping_info(models.Model):
    status = models.CharField('配送状态',max_length = 50,null = True)
    sender = models.ForeignKey(sender_info,on_delete = models.CASCADE)
    address = models.CharField('配送地址',max_length = 200,null = True)

#支付方式表
class payment_methods(models.Model):
    boss_consumption = models.DecimalField('老板消费',max_digits = 8,
           decimal_places = 2,null = True) 
    coupon = models.DecimalField('优惠券',max_digits = 8,
           decimal_places = 2,null = True) 
    stored_value_card = models.DecimalField('储值卡',max_digits = 8,
            decimal_places = 2,null = True)
    landlady_consumption = models.DecimalField('老板娘消费',max_digits = 8,
           decimal_places = 2,null = True) 
    weixin = models.DecimalField('微信',max_digits = 8,
           decimal_places = 2,null = True) 
    bank_card = models.DecimalField('银行卡',max_digits = 8,
           decimal_places = 2,null = True) 
    cash = models.DecimalField('现金',max_digits = 8,
           decimal_places = 2,null = True) 

#押金表,订单的子表
class diposit(models.Model):
    diposit_receive = models.DecimalField('收押金',max_digits = 8,
           decimal_places = 2,null = True) 
    diposit_return = models.DecimalField('退押金',max_digits = 8,
           decimal_places = 2,null = True) 
    diposit_over = models.DecimalField('押金溢收',max_digits = 8,
           decimal_places = 2,null = True) 
    ceil_over = models.DecimalField('四舍五入',max_digits = 8,
           decimal_places = 2,null = True) 
    floor_over = models.DecimalField('抹零',max_digits = 8,
           decimal_places = 2,null = True) 
 
#订单支付信息，订单表的子表
class order_payment(models.Model):   
    payment_method = models.ForeignKey(payment_methods,on_delete = models.CASCADE,related_name = 'order_payment')
    payment_state = models.CharField('支付状态',max_length = 50,null = True)
    order_time = models.DateTimeField('支付时间',null = True)
    should_payment = models.DecimalField('应付金额',max_digits = 8,
           decimal_places = 2,null = True) 
    actual_payment = models.DecimalField('实付金额',max_digits = 8,
           decimal_places = 2,null = True) 
    should_get = models.DecimalField('应收金额',max_digits = 8,
           decimal_places = 2,null = True) 
    actual_get = models.DecimalField('实收金额',max_digits = 8,
           decimal_places = 2,null = True) 
    refunds = models.DecimalField('退款',max_digits = 8,
           decimal_places = 2,null = True) 
    payment_over = models.DecimalField('支付溢收',max_digits = 8,
           decimal_places = 2,null = True) 
    over_summary = models.DecimalField('损溢小计',max_digits = 8,
           decimal_places = 2,null = True) 

#订单价格，订单表的子表
#TODO:discount设计为独立可维护的表，此表包含discount
class order_price(models.Model):
    order_money = models.DecimalField('订单金额(含押金)',max_digits = 8,
            decimal_places = 2,null = True)
    goods_money = models.DecimalField('商品总额',max_digits = 8,
            decimal_places = 2,null = True)
    extra_charge = models.DecimalField('附加费',max_digits = 8,
            decimal_places = 2,null = True)
    dispatching_money = models.DecimalField('配送费',max_digits = 8,
            decimal_places = 2,null = True)
    discount_summary= models.DecimalField('优惠总额',max_digits = 8,
            decimal_places = 2,null = True)

#就餐信息
class repast_info(models.Model):
    repast_number = models.IntegerField('就餐人数',null = True)
    repast_type = models.CharField('就餐类型',max_length = 50,null = True)
    area = models.ForeignKey(area_management,on_delete = models.CASCADE,related_name = 'repast_info') 


#门店信息
class store_info(models.Model):
    name = models.CharField('店面名称',max_length = 200)

#订单列表
class order_list(models.Model):
    order_id = models.CharField('单据号',max_length = 200,primary_key = True)
    order_type = models.CharField('订单类型',max_length = 50,null = True)
    order_status = models.CharField('订单状态',max_length = 50,null = True)
    start_time = models.DateTimeField('下单时间',null = True)
    business_time = models.DateField('营业时间',null = True)
    order_source = models.CharField('订单来源',max_length = 100,null = True)
    waiter = models.ForeignKey(waiter_info,on_delete = models.CASCADE,related_name = 'order_list')
    operator = models.ForeignKey(waiter_info,on_delete = models.CASCADE,related_name = 'order_list')
    customer = models.ForeignKey(customer_info,on_delete = models.CASCADE,related_name = 'order_list')
    cash_terminal = models.ForeignKey(cash_terminal,on_delete = models.CASCADE,related_name = 'order_list')
    receiver = models.ForeignKey(receiver_info,on_delete = models.CASCADE,related_name = 'order_list')
    payment = models.ForeignKey(order_payment,on_delete = models.CASCADE,related_name = 'order_list')
    store = models.ForeignKey(store_info,on_delete = models.CASCADE,related_name = 'order_list')
    diposit = models.ForeignKey(diposit,on_delete = models.CASCADE,related_name = 'order_list')
    repast = models.ForeignKey(repast_info,on_delete = models.CASCADE,related_name = 'order_list')
    shipping_info = models.ForeignKey(shipping_info,on_delete = models.CASCADE,related_name = 'order_list')
    order_price = models.ForeignKey(order_price,on_delete = models.CASCADE,related_name = 'order_list')

