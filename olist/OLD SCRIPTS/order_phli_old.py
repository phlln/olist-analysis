import os
import pandas as pd
import numpy as np
from olist.utils import haversine_distance
from olist.data import Olist


class Order:
    '''
    DataFrames containing all orders as index,
    and various properties of these orders as columns
    '''

    def __init__(self):
        # Assign an attribute ".data" to all new instances of Order
        self.data = Olist().get_data()

    def get_wait_time(self, is_delivered=True):
        """
        02-01 > Returns a DataFrame with:
        [order_id, wait_time, expected_wait_time, delay_vs_expected, order_status]
        and filtering out non-delivered orders unless specified
        """
        # Hint: Within this instance method, you have access to the instance of the class Order in the variable self, as well as all its attributes
        
        orders = self.data['orders'].copy() 
        
        # Filter dataframe on delivered orders
        
        if is_delivered:
            orders = orders.query("order_status=='delivered'")
        #orders = orders[orders['order_status'] == 'delivered']
        #orders.query("order_status == 'delivered'")


        # handle datetime
        change_to_datetime = ['order_purchase_timestamp', 'order_delivered_customer_date', 'order_estimated_delivery_date']
        for column in change_to_datetime:
            orders.loc[:, column] = pd.to_datetime(orders[column])

        # compute wait time
        orders['wait_time'] = orders['order_delivered_customer_date'] - orders['order_purchase_timestamp'] 

        #function to covert duration to float (days)
        def convert_to_float_days(duration_datetime):
            convert_to_min = duration_datetime.total_seconds() / 60.0
            convert_to_hour =  convert_to_min / 60.0
            convert_to_day = convert_to_hour / 24.0
            return convert_to_day

        orders['wait_time (days)'] = orders['wait_time'].apply(convert_to_float_days)

        # compute expected wait time
        orders['expected_wait_time'] = orders['order_estimated_delivery_date'] - orders['order_purchase_timestamp'] 
        orders['expected_wait_time (days)'] = orders['expected_wait_time'].apply(convert_to_float_days)

        # compute delay vs expected - carefully handles "negative" delays
        #delay_vs_expected (float) if the actual delivery date is later than the estimated delivery date, 
        #returns the absolute number of days between the two dates, otherwise return 0

        orders['delay_vs_expected'] = orders['order_estimated_delivery_date'] - orders['order_delivered_customer_date'] 
        orders['delay_vs_expected'] = orders['delay_vs_expected'].apply(convert_to_float_days)

        # orders.query("delay_vs_expected <= 0").[:,'delay_vs_expected'] = 0
        orders.delay_vs_expected = orders.delay_vs_expected.apply(lambda x: 0 if x <= 0 else x)
        
        
        
    def get_review_score(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, dim_is_five_star, dim_is_one_star, review_score
        """
        reviews = self.data['order_reviews'].copy()
        
        def dim_five_star(x):
            if x == 5:
                return 1
            return 0
                
        def dim_one_star(x):
            if x == 1:
                return 1
            return 0 

        reviews["dim_is_five_star"] = reviews["review_score"].map(dim_five_star) # --> Series([0, 1, 1, 0, 0, 1 ...])
        reviews["dim_is_one_star"] = reviews["review_score"].map(dim_one_star) # --> Series([0, 1, 1, 0, 0, 1 ...])


    def get_number_products(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, number_of_products
        """
        

        products = self.data['order_items'].copy() # good practice to be sure not to modify your `data` variable
        
        products = products.groupby('order_id')['order_item_id'].count()

        products.columns = ['order_id', 'number_of_products']
   
        return products
    
    

    def get_number_sellers(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, number_of_sellers
        """
        sellers = self.data['order_items'].copy()
        sellers['number_of_sellers'] = sellers.groupby('order_id').seller_id.nunique()
        sellers.columns = ['order_id', 'number_of_sellers']
        return sellers

    def get_price_and_freight(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, price, freight_value
        """
       
        price_freight = self.data['order_items'].copy()
        
        price_freight = order_items.groupby('order_id').agg({'price':'sum', 'freight_value': 'sum'})

        price_freight.columns=['price', 'freight_value']
        return price_freight


    def get_distance_seller_customer(self):
        """
        02-01 > Returns a DataFrame with order_id
        and distance between seller and customer
        """
        # Optional
        # Hint: you can use the haversine_distance logic coded in olist/utils.py



    def get_training_data(self, is_delivered=True,
                          with_distance_seller_customer=False):
        """
        02-01 > Returns a clean DataFrame (without NaN), with the following columns:
        [order_id, wait_time, expected_wait_time, delay_vs_expected, order_status,
        dim_is_five_star, dim_is_one_star, review_score, number_of_products,
        number_of_sellers, freight_value, distance_customer_seller]
        """
        # Hint: make sure to re-use your instance methods defined above

        data = self.data
        
        training_set =\
            self.get_wait_time(is_delivered)\
                .merge(
                self.get_review_score(), on='order_id'
               ).merge(
                self.get_number_products(), on='order_id'
               ).merge(
                self.get_number_sellers(), on='order_id'
               ).merge(
                self.get_price_and_freight(), on='order_id'
               )
        # Skip heavy computation of distance_seller_customer unless specified
        if with_distance_seller_customer:
            training_set = training_set.merge(
                self.get_distance_seller_customer(), on='order_id')

        return training_set.dropna()
        