Jupyter Notebook
JanaC
Last Checkpoint: a few seconds ago
(autosaved)
Current Kernel Logo
Python 3 
File
Edit
View
Insert
Cell
Kernel
Widgets
Help

Heroes Of Pymoli Data Analysis
Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).

Note
Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.
#---------------------------------------------------------------------#
#                      Dependencies and Setup                         #
#---------------------------------------------------------------------#
​
#---------------------------------------------------------------------#
# Import the pandas module b/c you're gonna need to use pandas
# Import the numpy module b/c you're gonna do some jazzy calculations
#---------------------------------------------------------------------#
import pandas as pd
import numpy as np
​
#---------------------------------------------------------------------#
# Now, identify the file path so the code can read the csv file
#---------------------------------------------------------------------#
purch_file = "Resources/purchase_data.csv"
​
#---------------------------------------------------------------------#
# Read/Review Purchasing File and store it into a Pandas data frame
# Use some encoding to avoid funky characters
# Format the Price column so the values include a $
#---------------------------------------------------------------------#
purchase_data_df = pd.read_csv(purch_file, encoding="utf-8")
purchase_data_df.describe()
purchase_data_df.count()
purchase_data_df.head()
​
# purchase_data_df["Price"] = purchase_data_df["Price"].map("${:.2f}".format)
# purchase_data_df.head()
Purchase ID	SN	Age	Gender	Item ID	Item Name	Price
0	0	Lisim78	20	Male	108	Extraction, Quickblade Of Trembling Hands	3.53
1	1	Lisovynya38	40	Male	143	Frenzied Scimitar	1.56
2	2	Ithergue48	24	Male	92	Final Critic	4.88
3	3	Chamassasya86	24	Male	100	Blindscythe	3.27
4	4	Iskosia90	23	Male	131	Fury	1.44
 
#---------------------------------------------------------------------#
#                           Total Players                             #
#---------------------------------------------------------------------#
​
#---------------------------------------------------------------------#
# Put the Total No. of Players from the Description into a data frame #
#---------------------------------------------------------------------#
players_df = pd.DataFrame({"Total Active Players": [1163]})
players_df
Total Active Players
0	1163
         #
#---------------------------------------------------------------------#
# Put the Total No. of Players from the CSV into a data frame         #
#---------------------------------------------------------------------#
tp_df = pd.DataFrame({"Total Players": [purchase_data_df["SN"].count()]})
tp_df
​
Total Players
0	780
Purchasing Analysis (Total)
Run basic calculations to obtain number of unique items, average price, etc.
Create a summary data frame to hold the results
Optional: give the displayed data cleaner formatting
Display the summary data frame
#---------------------------------------------------------------------#
#                      Purchasing Analysis                            #
#---------------------------------------------------------------------#
​
#---------------------------------------------------------------------#
# Get the Number of Unique Items                                      #
#---------------------------------------------------------------------#
unique_items = purchase_data_df["Item Name"].nunique()
unique_items
​
#---------------------------------------------------------------------#
# Get the Average Purchase Price                                      #
#---------------------------------------------------------------------#
avg_price = purchase_data_df["Price"].mean()
avg_price
​
#---------------------------------------------------------------------#
# Get the Total Number of Purchases                                 #
#---------------------------------------------------------------------#
total_purch = purchase_data_df["Purchase ID"].count()
total_purch
​
#---------------------------------------------------------------------#
#Get theTotal Revenue
#---------------------------------------------------------------------#
total_rev = total_purch*avg_price
total_rev
​
#---------------------------------------------------------------------#
# Now, put the results in a summary table
# Format Price and Total Revenue to include a $
#---------------------------------------------------------------------#
summary_table = pd.DataFrame({"Number of Unique Items": unique_items,
                                "Average Purchase Price": [avg_price],
                                 "Total Number of Purchases": [total_purch],
                                  "Total Revenue": [total_rev]})
​
# summary_table['Average Purchase Price'] = summary_table['Average Purchase Price'].map('${0:,.2f}'.format)
# summary_table['Total Revenue'] = summary_table['Total Revenue'].map('${0:,.2f}'.format)
​
summary_table
Number of Unique Items	Average Purchase Price	Total Number of Purchases	Total Revenue
0	179	3.050987	780	2379.77
Gender Demographics
#---------------------------------------------------------------------#
# Now, put the Gender Demos into a dataframe and format the percents  #
#---------------------------------------------------------------------#
#---------------------------------------------------------------------#
#                         Get the Gender Demos                        #
#---------------------------------------------------------------------#
​
#---------------------------------------------------------------------#
# Get the counts
#---------------------------------------------------------------------#
total_players = purchase_data_df["SN"].count()
total_players
​
male_count = purchase_data_df.groupby(["Gender", "SN"]).SN.nunique().Male.count()
male_count
​
female_count = purchase_data_df.groupby(["Gender", "SN"]).SN.nunique().Female.count()
female_count
​
ond_count = purchase_data_df.groupby(["Gender", "SN"]).SN.nunique()['Other / Non-Disclosed'].count()
ond_count
​
#---------------------------------------------------------------------#
# Get the Percentages                                                 #
#---------------------------------------------------------------------#
​
male_percent = male_count / total_players
male_percent
​
female_percent = female_count / total_players
female_percent
​
ond_percent = ond_count / total_players
ond_percent
​
#---------------------------------------------------------------------#
# Now, put the Gender Demos into a dataframe and format the percents  #
#---------------------------------------------------------------------#
​
gender_demos = {
    "Gender": ["Male", "Female", "Other/Non-Disclosed"],
    "Counts": [male_count, female_count, ond_count],
    "Percentages": [male_percent, female_percent, ond_percent],}
​
gender_demos_df = pd.DataFrame(gender_demos).set_index("Gender")
gender_demos_df
​
gender_demos_df["Percentages"] = gender_demos_df["Percentages"].map('{:.2%}'.format)
gender_demos_df
Counts	Percentages
Gender		
Male	484	62.05%
Female	81	10.38%
Other/Non-Disclosed	11	1.41%
Purchasing Analysis (Gender)
Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
Create a summary data frame to hold the results
Optional: give the displayed data cleaner formatting
Display the summary data frame
#---------------------------------------------------------------------#
#                    Purchasing Analysis (Gender)                     #
#---------------------------------------------------------------------#
​
gender_df = purchase_data_df.groupby("Gender")
gender_df.head()
​
#---------------------------------------------------------------------#
# Purchase Count                                                      #
#---------------------------------------------------------------------#
​
purchase_count = purchase_data_df.groupby(["Gender"]).count()["Price"]
​
#---------------------------------------------------------------------#
# Average Purchase Price                                              #
#---------------------------------------------------------------------#
​
avgpp = purchase_data_df.groupby(["Gender"]).mean()["Price"]
​
#---------------------------------------------------------------------#
# Total Purchase Value                                                #
#---------------------------------------------------------------------#
​
tpv = purchase_data_df.groupby(["Gender"]).sum()["Price"]
​
#---------------------------------------------------------------------#
# Average Purchase Total per Person by Gender                         #
#---------------------------------------------------------------------#
​
avg_purch_total = tpv / gender_demos_df["Counts"]
​
​
#---------------------------------------------------------------------#
# Now, put the Purchase data into a dataframe and format to show $    #
#---------------------------------------------------------------------#
​
purchase_analysis = pd.DataFrame({"Purchase Count": purchase_count, 
                            "Average Purchase Price": avgpp, 
                            "Total Purchase Value": tpv, 
                            "Average Purchase Total": avg_purch_total})
​
​
purchase_analysis
# purchase_analysis["Purchase Count"] = purchase_analysis["Purchase Count"].map("{:,}".format)
# purchase_analysis["Average Purchase Price"] = purchase_analysis["Average Purchase Price"].map("${:,.2f}".format)
# purchase_analysis["Total Purchase Value"] = purchase_analysis["Total Purchase Value"].map("${:,.2f}".format)
# purchase_analysis["Average Purchase Total"] = purchase_analysis["Average Purchase Total"].map("${:,.2f}".format)
# purchase_analysis = purchase_analysis.loc[:, ["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Average Purchase Total"]]
# purchase_analysis
​
​
​
​
# male_purch = gender_df.count().Age.Male
# male_purch
​
# female_purch = gender_df.count().Age.Female
# female_purch
​
# ond_purch = gender_df.count().Age["Other / Non-Disclosed"]
# ond_purch
#avgpurprice_male = gender_df.mean().Price.Male
# avgpurprice_male
​
# avgpurprice_female= gender_df.mean().Price.Female
# avgpurprice_female
​
# avgpurprice_ond = gender_df.mean().Price["Other / Non-Disclosed"]
# avgpurprice_ond
​
# totpurval_male = gender_df.sum().Price.Male
# totpurval_male
​
# totpurval_female = gender_df.sum().Price.Female
# totpurval_female
​
# totpurval_ond = gender_df.sum().Price["Other / Non-Disclosed"]
# totpurval_ond
​
# total_purch_value = gender_df.sum()
# total_purch_value
# avgpurvalue = totpurval_male + totpurval_female + totpurval_ond/3
# avgpurvalue
​
​
Purchase Count	Average Purchase Price	Total Purchase Value	Average Purchase Total
Female	113.0	3.203009	361.94	4.468395
Male	652.0	3.017853	1967.64	4.065372
Other / Non-Disclosed	15.0	3.346000	50.19	NaN
Other/Non-Disclosed	NaN	NaN	NaN	NaN
..## Age Demographics
Establish bins for ages
Categorize the existing players using the age bins. Hint: use pd.cut()
Calculate the numbers and percentages by age group
Create a summary data frame to hold the results
Optional: round the percentage column to two decimal points
Display Age Demographics Table
​
Total Count	Percentage of Players
<10	17	2.95
10-14	22	3.82
15-19	107	18.58
20-24	258	44.79
25-29	77	13.37
30-34	52	9.03
35-39	31	5.38
40+	12	2.08
Purchasing Analysis (Age)
Bin the purchase_data data frame by age
Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
Create a summary data frame to hold the results
Optional: give the displayed data cleaner formatting
Display the summary data frame
​
Purchase Count	Average Purchase Price	Total Purchase Value	Avg Total Purchase per Person
10-14	28	$2.96	$82.78	$3.76
15-19	136	$3.04	$412.89	$3.86
20-24	365	$3.05	$1,114.06	$4.32
25-29	101	$2.90	$293.00	$3.81
30-34	73	$2.93	$214.00	$4.12
35-39	41	$3.60	$147.67	$4.76
40+	13	$2.94	$38.24	$3.19
<10	23	$3.35	$77.13	$4.54
Top Spenders
Run basic calculations to obtain the results in the table below
Create a summary data frame to hold the results
Sort the total purchase value column in descending order
Optional: give the displayed data cleaner formatting
Display a preview of the summary data frame
​
Purchase Count	Average Purchase Price	Total Purchase Value
SN			
Lisosia93	5	$3.79	$18.96
Idastidru52	4	$3.86	$15.45
Chamjask73	3	$4.61	$13.83
Iral74	4	$3.40	$13.62
Iskadarya95	3	$4.37	$13.10
Most Popular Items
Retrieve the Item ID, Item Name, and Item Price columns
Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
Create a summary data frame to hold the results
Sort the purchase count column in descending order
Optional: give the displayed data cleaner formatting
Display a preview of the summary data frame
​
Purchase Count	Item Price	Total Purchase Value
Item ID	Item Name			
178	Oathbreaker, Last Hope of the Breaking Storm	12	$4.23	$50.76
145	Fiery Glass Crusader	9	$4.58	$41.22
108	Extraction, Quickblade Of Trembling Hands	9	$3.53	$31.77
82	Nirvana	9	$4.90	$44.10
19	Pursuit, Cudgel of Necromancy	8	$1.02	$8.16
Most Profitable Items
Sort the above table by total purchase value in descending order
Optional: give the displayed data cleaner formatting
Display a preview of the data frame
​
Purchase Count	Item Price	Total Purchase Value
Item ID	Item Name			
178	Oathbreaker, Last Hope of the Breaking Storm	12	$4.23	$50.76
82	Nirvana	9	$4.90	$44.10
145	Fiery Glass Crusader	9	$4.58	$41.22
92	Final Critic	8	$4.88	$39.04
103	Singed Scalpel	8	$4.35	$34.80