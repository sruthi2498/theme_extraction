# theme_extraction
Extracting the outling theme from restuarant reviews using scikit.

# Difference between single and multiple classification :
	https://docs.google.com/document/d/1jfk09bXUUGAuir7bUkALJoU_fQdw135KgkauKI8TbOs/edit
	
# Working :

To run the python file :

	$ python categorize_rev_user.py 


To view the web front end :

	Set up localhost and open webpage.html

Creating a data set : Extracted 10000+ reviews from Zomato using Python Selenium :

	1)Installing selelnium : (http://selenium-python.readthedocs.io/installation.html)
		pip install selenium

Setting up scikit :

	1) http://ogrisel.github.io/scikit-learn.org/sklearn-tutorial/tutorial/text_analytics/setup.html

Theme extraction using scikit :

    1) Text analysis using scikit http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
    2) Creating a data set with categories (food,service,ambience,etc) 
      Target_names refer to the categories (size of target_names is size of categories, in this case, 5)
      Target has the index of the category for each review in the data set (size of target is size of total number of reviews)
      Data set is divided into training set and testing set.
    3) Training the data
      There are two classifiers : Naive Bayes and Support Vector Machines
      (Refer to tutorial)
    4) Predict for the test set and show accuracy.


