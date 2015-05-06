# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:46:21 2015

@author: upendra
"""
import math
import os
import operator
import json
testfilename="C:/upendra/test.json"
testfilename1="C:/upendra/testtips.json"
testfilenamereviews="C:/upendra/testreviews.json"
testfilenameusers="C:/upendra/testusers.json"
testfilenamebusiness="C:/upendra/testbusiness.json"
reviewfilename="C:/upendra/masters/Course Data Mining/course project/yelp_dataset_challenge_academic_dataset/yelp_dataset_challenge_academic_dataset/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json"
userfilename="C:/upendra/masters/Course Data Mining/course project/yelp_dataset_challenge_academic_dataset/yelp_dataset_challenge_academic_dataset/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_user.json"
busfilename="C:/upendra/masters/Course Data Mining/course project/yelp_dataset_challenge_academic_dataset/yelp_dataset_challenge_academic_dataset/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json"
checkinfilename="C:/upendra/masters/Course Data Mining/course project/yelp_dataset_challenge_academic_dataset/yelp_dataset_challenge_academic_dataset/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_checkin.json"
tipsfilename="C:/upendra/masters/Course Data Mining/course project/yelp_dataset_challenge_academic_dataset/yelp_dataset_challenge_academic_dataset/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_tip.json"
#
##############variables for old model##################

#for check-in json
cdb= {}
checkinbus=[]
checkininfo=[]
#for tips json
tdb={}
tips_bus_id=[]
tips_user_info = []
tip_text = []
tip_likes = []
#for reviews json
rdb={}
reviews_bus_id= []
reviews_user_info=[]
reviews_stars=[]
reviews_review_id= []

#######################################################
##############Creating the Data Model #################
#######################################################


###For Reviews.JSON#####################################
mfr={}#top level dictionary for business json model
#key is business id,value is a dictionary with all sorts of informaiton about that particular business
ridcounter=0
with open(reviewfilename) as json_file:
    for line in json_file.readlines():
        json_data=json.loads(line);
        bid=""
        ridcounter=ridcounter+1
        r_dict={}#changes for every iteration. Holds the value of particular record in a reviews.json file
        for keys, values in json_data.items():
            if keys=="business_id":
                reviews_bus_id.append(values)
                r_dict['reviews_bus_id']=values                
            if keys=="user_id":
                reviews_user_info.append(values)
                r_dict['reviews_user_info']=values
            if keys=="stars":
                reviews_stars.append(values)
                r_dict['reviews_stars']=values
            if keys=="review_id":
                reviews_review_id.append(values)
                r_dict['reviews_review_id']=values
                bid=str(ridcounter)
        mfr[ridcounter]=r_dict

#print (mfr[bid]['reviews_review_id'])#prints a particular record's review_id
#print(mfr[bid])#prints a particular record and all of its info.
#print(mfr)#prints all reviews.json records
#########################################################
#########################################################

###For check-in.JSON#####################################
checkinbus=[]
checkininfo=[]
cdb={}

mfc={}

#print("Building check-in.json data")
with open(testfilename) as json_file:
    checkinid=0
    for line in json_file.readlines():
#        print(line)
        chec_dict={}
        checkinid=checkinid+1
        cid=""
        cid=""+str(checkinid)
        json_data=json.loads(line)
        #print(type(json_data))
        for keys, values in json_data.items():
            if keys=="business_id":
                chec_dict['business_id']=values
            if keys=="checkin_info":
                chec_dict['checkin_info']=values
        mfc[cid]=chec_dict
#print(mfc)
####################users########################

users_uid=[]
users_uname=[]
users_review_count=[]
users_avg_stars=[]
users_friends=[]
mfu={}
#for users.json
#print("Building user.json data")
with open(userfilename) as json_file:
    for line in json_file.readlines():
        json_data=json.loads(line)
        uid=""
        user_dict={}#stores information of each record, resets to empty dictionary when the program reads new record from the file
        for keys, values in json_data.items():
            #checkindatabase.append(keys)
            #print(type(keys), 1, keys,  values)
            if keys=="user_id":      
                uid=values
                user_dict['user_id']=values
            if keys=="name":
                user_dict['name']=values
            if keys=="review_count":
                user_dict['review_count']=values
            if keys=="average_stars":
                user_dict['average_stars']=values
            if keys=="friends":
                user_dict['friends']=values
        mfu[uid]=user_dict
#print(mfu)
####################business########################
#for business.json
mfb={}
#print("Building business.json data")
with open(testfilenamebusiness) as json_file:
    for line in json_file.readlines():
        json_data=json.loads(line)
        bus_dict={}
        bid=""
        for keys, values in json_data.items():
            if keys=="business_id":
                bus_dict['business_id']=values
                bid=bus_dict['business_id']
            if keys=="name":
                bus_dict['name']=values
            if keys=="city":
                bus_dict['city']=values
            if keys=="state":
                bus_dict['state']=values
            if keys=="stars":
                bus_dict['stars']=values
            if keys=="review_count":
                bus_dict['review_count']=values
            if keys=="categories":
                bus_dict['categories']=values
            if keys=="open":
                bus_dict['open']=values
        mfb[bid]=bus_dict
#print(mfb)
####################tips########################
#for tips json
mft={}
#print("Building tips.json data")
with open(testfilename1) as json_file:
    tipsid=0
    for line in json_file.readlines():
#        print(line)
        json_data=json.loads(line)
        tips_dict={}
        tipsid=tipsid+1
        tid=""
        tid=""+str(tipsid)
        for keys, values in json_data.items():
            if keys=="business_id":
                tips_bus_id.append(values)
                tips_dict['business_id']=values
            if keys=="user_id":
                tips_user_info.append(values)
                tips_dict['user_id']=values
            if keys=="text":
                tip_text.append(values)
                tips_dict['text']=values
        mft[tid]=tips_dict
#    tdb['tips_b_ids']=tips_bus_id
#    tdb['tip_text']=tip_text
#    tdb['tips_user_info'] = tips_user_info
#print(mft)

#########################################################
#########################################################
dup_top_rest_from_rest_i_visited={}
#########################################################
#############Recommendation Engine Code##################
#########################################################
tempmfr={}
def getuservisitedplaces(userid):
    #retreive the user visits from review json model
    tempmfr=mfr
    uvisits=[]#It is the list of the businesses that user has visited
    for keys, values in tempmfr.items():
        uservisited=0
        #print(userid, " type is ", type(userid))
        for k,v in values.items():
            
            #print (v, type(v), keys,k)
            if k=='reviews_user_info' and v==userid:
                uservisited=1
                #print("I am here")
            if k=='reviews_bus_id' and uservisited==1:
                uvisits.append(keys)
    #print(uvisits)#prints number of times user visited restaurants
    return uvisits#has the list of businesses that user with user id "userid" has visited


def get_top_restaurants_from_rest_i_visited(uniq_rest_i_visited):
    temp_rest={}
    temp_list_bid=[]#bid is business id
    temp_list_bidvc=[]#vc visit count by a user to particular restaurant
    temp_rest=uniq_rest_i_visited
    temp_topvisit_counter=0#initially 0
    for k,v in temp_rest.items(): #sorts into top restraunt list
        if v >=temp_topvisit_counter:
            temp_list_bid=[k]+temp_list_bid
            temp_list_bidvc=[v]+temp_list_bidvc
            temp_topvisit_counter=v
        else:
            temp_list_bid=temp_list_bid+[k]
            temp_list_bidvc=temp_list_bidvc+[v]
    #print("temp_topvisit_counter : " , temp_topvisit_counter)
    toprestlist={}
    #print(len(temp_list_bid))
    #print(len(temp_list_bidvc))
    for i in range(len(temp_list_bid)):#bid is business id
        #print(temp_list_bid[i],temp_list_bidvc[i], type(temp_list_bidvc[i]))
        if temp_topvisit_counter==temp_list_bidvc[i]:
            toprestlist[temp_list_bid[i]]=temp_list_bidvc[i]#only sending top rest as output
            #print(temp_list_bid[i],temp_list_bidvc[i])
    return toprestlist

def get_unique_rest_names_from_uservisits(uvisits):
    uniq_rest={}
    for i in range(len(uvisits)):
        #print(mfr[uvisits[i]])
        temp={}
        temp=mfr[uvisits[i]]
        #print(mfr[uvisits[i]])
        #print(temp['reviews_bus_id'])
        if temp['reviews_bus_id'] not in uniq_rest.keys():
            uniq_rest[temp['reviews_bus_id']]=1
        else:
            addcounter=0
            addcounter=uniq_rest[temp['reviews_bus_id']]+1
            uniq_rest[temp['reviews_bus_id']]=addcounter
    return uniq_rest

def gettopfriends(userid):
    return ""

#########################################################
##############Accuracy of the model####################
#########################################################


def get_top_restaurants_from_rest_i_visited_eff(uniq_rest_i_visited):
    temp_rest={}
    temp_list_bid=[]#bid is business id
    temp_list_bidvc=[]#vc visit count by a user to particular restaurant
    temp_rest=uniq_rest_i_visited
    temp_topvisit_counter=0#initially 0
    counterforlength=0
    for k,v in temp_rest.items(): #sorts into top restraunt list
        counterforlength=counterforlength+1
    counterforlength=(80/100)*counterforlength
    counterforlength1=0
    for k,v in temp_rest.items():
        counterforlength1=counterforlength1+1
        if counterforlength1<=counterforlength:
            if v >=temp_topvisit_counter:
                temp_list_bid=[k]+temp_list_bid
                temp_list_bidvc=[v]+temp_list_bidvc
                temp_topvisit_counter=v
            else:
                temp_list_bid=temp_list_bid+[k]
                temp_list_bidvc=temp_list_bidvc+[v]
    #print("temp_topvisit_counter : " , temp_topvisit_counter)
    toprestlist={}
    
    #print(len(temp_list_bid))
    #print(len(temp_list_bidvc))
    for i in range(len(temp_list_bid)):#bid is business id
        #print(temp_list_bid[i],temp_list_bidvc[i], type(temp_list_bidvc[i]))
        if temp_topvisit_counter==temp_list_bidvc[i]:
            toprestlist[temp_list_bid[i]]=temp_list_bidvc[i]#only sending top rest as output
            #print(temp_list_bid[i],temp_list_bidvc[i])
    return toprestlist

def get_recommendations_for_accuracy():
    uq_rlist=[]    
    global uniq1_restaurants
    uq_rlist=uniq1_restaurants
    top_rest_from_rest_i_visited={}    
    top_rest_from_rest_i_visited=get_top_restaurants_from_rest_i_visited_eff(uq_rlist)#inp:dictionary output: list with top restaurants
    global dup_top_rest_from_rest_i_visited
    measure_accuracy(dup_top_rest_from_rest_i_visited,top_rest_from_rest_i_visited)
    print("The Recommendations for the user are below for 80% data")
    print(top_rest_from_rest_i_visited)
    return ""

def measure_accuracy(res1,res_eff):
    counterforeff=0
    counteracteff=0
    for k,v in res1.items():
        counteracteff=counteracteff+1
        if k in res_eff.keys():
            counterforeff=counterforeff+1
    print("Accuracy of the model",(counterforeff/counteracteff)*100)
    return ""


#########################################################
#########################################################






def getrecommendations(userid,location):
    u_visits=[]
    numvisits=0
    numvisits=len(u_visits)
    u_visits=getuservisitedplaces(userid)
    numvisits=len(u_visits)
    print("Number of overall visits: ", numvisits)
    uniq_restaurants={}    
    uniq_restaurants=get_unique_rest_names_from_uservisits(u_visits)#output : gives u a dictionary with the keys as unique restaurant ids and values as number of visits 
    global uniq1_restaurants
    uniq1_restaurants=uniq_restaurants
    countresta=0
    for k, v in uniq_restaurants.items():
        countresta=countresta+1
        #print(k,v)#prints unique restaurants that a user visited and how many times he visited
    print(countresta, "is the total count of restaurants u visited")
    top_rest_from_rest_i_visited={}    
    top_rest_from_rest_i_visited=get_top_restaurants_from_rest_i_visited(uniq_restaurants)#inp:dictionary output: list with top restaurants
    global dup_top_rest_from_rest_i_visited
    dup_top_rest_from_rest_i_visited=top_rest_from_rest_i_visited
    print("The Recommendations for the user are below")
    print(top_rest_from_rest_i_visited)
    get_recommendations_for_accuracy()
    return ""


getrecommendations("jE5xVugujSaskAoh2DRx3Q","")#takes random user id as input

#########################################################
#########################################################




