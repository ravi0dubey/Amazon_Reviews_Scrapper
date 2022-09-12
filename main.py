from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import mysql.connector as connection
import pandas as pd
import pymongo

app = Flask(__name__)

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","")
            amazon_url = "https://www.amazon.in/s?k=" + searchString
            print(amazon_url)
            response_website = uReq(amazon_url)
            amazon_response = response_website.read()
            response_website.close()
            beautifyed_html = bs(amazon_response, "html.parser")
            bigboxes = beautifyed_html.find_all("div", {"class": "sg-col sg-col-4-of-12 sg-col-4-of-16 sg-col-4-of-20 s-list-col-left"})
            # print(bigboxes)
            # for i in range(0,len(bigboxes)):
            #     box = bigboxes[i]
            #     productLink = "https://www.amazon.in" + box.div.a['href']
            #     print(f"Product Link first item : {productLink}")
            #
            box = bigboxes[0]
            productLink = "https://www.amazon.in" + box.div.a['href']
            print(f"Product Link actual : {productLink}")

                        # prodRes = requests.get(productLink)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

        # return render_template('results.html')

    else:
        return render_template('index.html')

if __name__ == "__main__":
# app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)

            #
            # print(len(bigbox))
            # print(bigbox[0])
            # product6 = "https://amazon.in" + bigbox[0].div.div.div.a['url']
            # print(product6)
            # product66 = requests.get(product6)
            # product66.encoding = 'utf-8'
            # product6_page = bs(product66.text, "html.parser")
            #
            # product_price1 = product6_page.find_all('div', {'class': "_30jeq3 _16Jk6d"})[0].text
            # product_name1 = product6_page.find_all('div', {'class': "aMaAEs"})[0].h1.text
            # overall_rating1 = product6_page.find_all('div', {'class': "_3LWZlK"})[0].text
            # total_Rating_count1 = product6_page.find_all('span', {'class': "_2_R_DZ"})[0].text.split('\xa0')[0]
            # total_review_count1 = product6_page.find_all('span', {'class': "_2_R_DZ"})[0].text.split('\xa0')[2]
            #
            # short_reviews = []
            # count_short_reviews = len(product6_page.find_all('div', {'class': "_16PBlm"}))
            # print(count_short_reviews)
            # for i in range(0, count_short_reviews - 1):
            #     short_reviews.append(product6_page.find_all('div', {'class': "_16PBlm"})[i].p.text)
            # # print(short_reviews)
            #
            #
            # long_reviews = []
            # count_long_reviews = len(product6_page.find_all('div', {'class': "t-ZTKy"}))
            # for i in range(0, count_long_reviews - 1):
            #     long_reviews.append(product6_page.find_all('div', {'class': "t-ZTKy"})[i].text)
            #
            # individual_ratings = []
            # count_individual_ratings = len(product6_page.find_all('div', {'class': "_3LWZlK _1BLPMq"}))
            # for i in range(0, count_individual_ratings - 1):
            #     individual_ratings.append(product6_page.find_all('div', {'class': "_3LWZlK _1BLPMq"})[i].text)
            #
            # users_list = []
            # count_users = len(product6_page.div.div.find_all('p', {'class': "_2sc7ZR _2V5EHH"}))
            # count_users
            # for i in range(0, count_users - 1):
            #     users_list.append(product6_page.div.div.find_all('p', {'class': "_2sc7ZR _2V5EHH"})[i].text)
            #
            # # print(users_list)
            #
            # feedback_date_list = []
            # count_date_user_given = len(product6_page.div.div.find_all('p', {'class': "_2sc7ZR"}))
            # count_date_user_given
            # for i in range(1, count_date_user_given - 1, 2):
            #     feedback_date_list.append(product6_page.div.div.find_all('p', {'class': "_2sc7ZR"})[i].text)
            #
            # try:
            #     mydb = connection.connect(host="localhost", database="projectdb", user="root", passwd="root", use_pure=True)
            #     cursor = mydb.cursor()
            #     # for i in short_reviews, long_reviews,individual_ratings,users_list,feedback_date_list:
            #     for i in range(0, count_short_reviews - 1):
            #         # print(users_list[i])
            #         # product_name =  product_name1
            #         # product_price= product_name1
            #         # overall_rating= product_name1
            #         # total_Rating_count  =total_Rating_count1
            #         # total_review_count=total_review_count1
            #         insert_query = f"insert into amazon_review values('{product_name1}','{product_price1}','{overall_rating1}','{total_Rating_count1}'," \
            #                        f"'{total_review_count1}','{users_list[i]}','{individual_ratings[i]}','{feedback_date_list[i]}','{short_reviews[i]}','{long_reviews[i]}');"
            #         print(insert_query)
            #         cursor.execute(insert_query)
            #         mydb.commit()
            #
            # except Exception as e:
            #     print(str(e))

            # return render_template('results.html')


