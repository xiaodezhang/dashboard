from django.db import models

# Create your models here.
class order_list(models.Model):
    sales_type = models.CharField('销售类型',max_length = 50)
    store_name = models.CharField('店面名称',max_length = 200)
    order_state = models.CharField('订单状态',max_length = 50)
    payment_state = models.CharField('支付状态',max_length = 50)
    start_time = models.DateTimeField('下单时间')
    order_time = models.DateTimeField('支付时间')
    business_time = models.DateTimeField('营业时间')
    order_id = models.CharField('单据号',max_length = 200,primary_key = True)
    order_id_old = models.CharField('原单据号',max_length = 200)
    area = models.CharField('区域',max_length = 50)
    desk_number = models.CharField('桌台号',max_length = 50)
    repast_number = models.IntegerField('就餐人数')
    customer_name = models.CharField('顾客姓名',max_length = 150)
    customer_phone = models.CharField('顾客电话',max_length = 11)
    customer_sex = models.CharField('顾客性别',max_length = 5)
    receiver_name = models.CharField('收货人姓名',max_length = 150)
    receiver_phone = models.CharField('收货人电话',max_length = 11)
    repast_type = models.CharField('就餐类型',max_length = 50)
    waiter_name = models.CharField('服务员姓名',max_length = 150)
    cash_terminal = models.CharField('收银终端',max_length = 50)
    operator_name = models.CharField('操作人姓名',max_length = 150)
    order_source = models.CharField('订单来源',max_length = 100)
    dispatching_state = models.CharField('配送状态',max_length = 50)
    dispatchinger = models.CharField('配送方',max_length = 50)
    dispatching_address = models.CharField('配送地址',max_length = 200)
    order_money = models.DecimalField('订单金额(含押金)',max_digits = 8,
            decimal_places = 2)
    goods_money = models.DecimalField('商品总额',max_digits = 8,
            decimal_places = 2)
    extra_charge = models.DecimalField('附加费',max_digits = 8,
            decimal_places = 2)
    dispatching_money = models.DecimalField('配送费',max_digits = 8,
            decimal_places = 2)
    discount_summary= models.DecimalField('优惠总额',max_digits = 8,
            decimal_places = 2)
    should_payment = models.DecimalField('应付金额',max_digits = 8,
           decimal_places = 2) 
    actual_payment = models.DecimalField('实付金额',max_digits = 8,
           decimal_places = 2) 
    should_get = models.DecimalField('应收金额',max_digits = 8,
           decimal_places = 2) 
    actual_get = models.DecimalField('实收金额',max_digits = 8,
           decimal_places = 2) 
    refunds = models.DecimalField('退款',max_digits = 8,
           decimal_places = 2) 
    diposit_receive = models.DecimalField('押金',max_digits = 8,
           decimal_places = 2) 
    diposit_return = models.DecimalField('押金',max_digits = 8,
           decimal_places = 2) 
    diposit_over = models.DecimalField('押金溢收',max_digits = 8,
           decimal_places = 2) 
    ceil_over = models.DecimalField('四舍五入',max_digits = 8,
           decimal_places = 2) 
    floor_over = models.DecimalField('抹零',max_digits = 8,
           decimal_places = 2) 
    payment_over = models.DecimalField('支付溢收',max_digits = 8,
           decimal_places = 2) 
    over_summary = models.DecimalField('损溢小计',max_digits = 8,
           decimal_places = 2) 
    boss_consumption = models.DecimalField('老板消费',max_digits = 8,
           decimal_places = 2) 
    coupon = models.DecimalField('优惠券',max_digits = 8,
           decimal_places = 2) 
    stored_value_card = models.DecimalField('储值卡',max_digits = 8,
            decimal_places = 2)
    landlady_consumption = models.DecimalField('老板娘消费',max_digits = 8,
           decimal_places = 2) 
    weixin = models.DecimalField('微信',max_digits = 8,
           decimal_places = 2) 
    bank_card = models.DecimalField('银行卡',max_digits = 8,
           decimal_places = 2) 
    cash = models.DecimalField('现金',max_digits = 8,
           decimal_places = 2) 
 
 
 
 
 
 
















