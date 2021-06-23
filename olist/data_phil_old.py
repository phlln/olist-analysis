import os
import pandas as pd
import ipdb

class Olist:

    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrame loaded from csv files
        """
        # Hints: Build csv_path as "absolute path" in order to call this method from anywhere.
        # Do not hardcode your path as it only works on your machine ('Users/username/code...')
        # Use __file__ as absolute path anchor independant of your computer
        # Make extensive use of `import ipdb; ipdb.set_trace()` to investigate what `__file__` variable is really
        # Use os.path library to construct path independent of Unix vs. Windows specificities

        data = {}
        
        target_path = os.path.dirname((os.path.dirname(__file__)))
    
        file_names = os.listdir(path='/Users/atat/code/phlln/data-challenges/04-Decision-Science/data/csv')
        file_names.remove('.DS_Store')
        file_names.remove('.gitkeep')
        file_names
    
    
        key_names=[]
        for item in file_names:
            item = item.replace('olist_', '') 
            item = item.replace('_dataset.csv','') 
            item = item.replace('.csv','')
            key_names.append(item)
        
    
        for k,f in zip(key_names, file_names):
            #target_path_2 = os.path.join(target_path, '/data/csv/' +f)
            target_path_2 = target_path + '/data/csv/' + f
            data[k] = pd.read_csv(target_path_2)
    
        return data



    def get_matching_table(self):
        """
        01-01 > This function returns a matching table between
        columns [ "order_id", "review_id", "customer_id", "product_id", "seller_id"]
        """

    def ping(self):
        """
        You call ping I print pong.
        """
        print('pong')
