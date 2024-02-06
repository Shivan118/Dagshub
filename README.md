# Project Completed


In data_transformation.py
Line 113 and 114

train_array = np.c_[input_feature_train_arr,np.array(target_feature_train_data).reshape(-1, 1) ] #Error 1
test_array = np.c_[input_feature_test_arr,np.array(target_feature_test_data).reshape(-1,1)] #Error 2

So, I changed it to

train_array = np.c_[input_feature_train_arr,np.array(target_feature_train_data).reshape(-1, 1) ]  
test_array = np.c_[input_feature_test_arr,np.array(target_feature_test_data).reshape(-1,1)] 

In this the input_feature_train_arr is changed to np array but the target_feature_train_data and target_feature_test_data is pandas series to we will use np.array and we will reshape it to make it a single column so that it will concatenate

In model_training.py
Line 10
This line was missing
from src.components.data_ingestion import DataIngestion, DataTransformation  # Error 2

This needs to be present to create an object of those classes

so after wrting this line I created and object and call using:
if __name__=="__main__":

    obj = DataIngestion()
    train_data_path,test_data_path = obj.initated_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initated_data_transformation(train_data_path, test_data_path)
    obj1=ModelTraning()
    obj1.initated_model_traning(train_arr,test_arr)



