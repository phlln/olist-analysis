import pandas as pd
import numpy as np
from olist.data import Olist


class Order:
    '''
    DataFrames containing all orders delivered as index,
    and various properties of these orders as columns
    '''

    def __init__(self):
        self.data = Olist().get_data()
        # The constructor of class Order assigns an attribute ".data" to all new instances of Order
        # i.e Order().data is defined

    def get_wait_time(self, is_delivered=True):
        """
        02-01 > Returns a DataFrame with:
        [order_id, wait_time, expected_wait_time, delay_vs_expected, order_status]
        filtering out non-delivered orders unless specified
        """
        # Within this instance method, you have access to the instance of the class Order in the variable self
        # make sure we don't create a "view" but a copy
        orders = self.data['orders'].copy()

        # filter delivered orders
        if is_delivered:
            orders = orders.query("order_status=='delivered'").copy()

        # handle datetime
        orders.loc[:, 'order_delivered_customer_date'] = \
            pd.to_datetime(orders['order_delivered_customer_date'])
        orders.loc[:, 'order_estimated_delivery_date'] = \
            pd.to_datetime(orders['order_estimated_delivery_date'])
        orders.loc[:, 'order_purchase_timestamp'] = \
            pd.to_datetime(orders['order_purchase_timestamp'])

        # compute delay vs expected
        orders.loc[:, 'delay_vs_expected'] = \
            (orders['order_estimated_delivery_date'] -
             orders['order_delivered_customer_date']) / np.timedelta64(24, 'h')

        def handle_delay(x):
            # We only want to keep delay where wait_time is longer than expected (not the other way around)
            # This is what drives customer dissatisfaction!
            if x < 0:
                return abs(x)
            return 0

        orders.loc[:, 'delay_vs_expected'] = \
            orders['delay_vs_expected'].apply(handle_delay)

        # compute wait time
        orders.loc[:, 'wait_time'] = \
            (orders['order_delivered_customer_date'] -
             orders['order_purchase_timestamp']) / np.timedelta64(24, 'h')

        # compute expected wait time
        orders.loc[:, 'expected_wait_time'] = \
            (orders['order_estimated_delivery_date'] -
             orders['order_purchase_timestamp']) / np.timedelta64(24, 'h')

        return orders[['order_id', 'wait_time', 'expected_wait_time',
                       'delay_vs_expected', 'order_status']]

    def get_review_score(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, dim_is_five_star, dim_is_one_star, review_score
        """
        # import data
        reviews = self.data['order_reviews']

        def dim_five_star(d):
            if d == 5:
                return 1
            return 0

        def dim_one_star(d):
            if d == 1:
                return 1
            return 0

        reviews.loc[:, 'dim_is_five_star'] =\
            reviews['review_score'].apply(dim_five_star)

        reviews.loc[:, 'dim_is_one_star'] =\
            reviews['review_score'].apply(dim_one_star)

        return reviews[['order_id', 'dim_is_five_star',
                        'dim_is_one_star', 'review_score']]

    def get_number_products(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, number_of_products
        """

        data = self.data
        products = \
            data['order_items']\
            .groupby('order_id',
                     as_index=False).agg({'order_item_id': 'count'})
        products.columns = ['order_id', 'number_of_products']
        return products

    def get_number_sellers(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, number_of_sellers
        """

        data = self.data
        sellers = \
            data['order_items']\
            .groupby('order_id')['seller_id'].nunique().reset_index()
        sellers.columns = ['order_id', 'number_of_sellers']

        return sellers

    def get_price_and_freight(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, price, freight_value
        """

        data = self.data
        price_freight = \
            data['order_items']\
            .groupby('order_id',
                     as_index=False).agg({'price': 'sum',
                                          'freight_value': 'sum'})

        return price_freight

    def get_training_data(self, is_delivered=True,
                          with_distance_seller_customer=False):
        """
        02-01 > Returns a clean DataFrame (without NaN), with the following
        columns: [order_id, wait_time, expected_wait_time, delay_vs_expected,
        dim_is_five_star, dim_is_one_star, review_score, number_of_products,
        number_of_sellers, price, freight_value]
        """
        # make sure to re-use your instance methods defined above
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

        return training_set.dropna()
