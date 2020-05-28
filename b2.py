import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import flask
from flask import Flask
import time
import telebot
import telegram_send
from telebot import types
import os

API_TOKEN = '1131080433:AAGkWAIOcnZXRT2VpjUp47ks3s_7odVNr6A'

bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)
PORT = int(os.environ.get('PORT', '8443'))
l=[]
user_dict = {}


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    try:
        msg = bot.reply_to(message, """\
Hi...!!!
Hello.....!!!!!!
Namaste........!!!!!!!!
there, I am Covid_vs_health bot.
For direct information go to /info
To know how to use the bot use /command
To know the detail description about bot use /description
""")
    except Exception as e:
            bot.reply_to(message, 'oops')

@bot.message_handler(commands=["info"])
def on_info(message):
    bot.reply_to(message, "Thanks for response \n Hello peeps :) \n To use this we have to type commands , use the commands shown below \n To get the details about Covid type /Covid_detail \n about health tips use /health_tips \n"
                 "To get covid cases of a state and union territories use /state ")

@bot.message_handler(commands = ["Covid_detail"])
def on_info(message):
    bot.reply_to(message , "please choose the following optionsbelow: \n"
                            "\n"
                           "1. What is Coronavirus and what are its symptoms? \n 2. How to reduce risk of Corona ? \n"
                           "3. Positive Harmonies \n"
                           "4. Help desk(like phone numbers,links, go to this) \n to use this type /Number (e.g : /1 ) \n"
                           "5. Top Intresting Facts on Corona \n"
                           "Which you want or click on the number?")


@bot.message_handler(commands = ["1"])
def on_info(message):
    bot.reply_to(message,"Most common symptoms  :  fever,dry cough,tiredness \n"
                         "\n"
                         "Less common symptoms  :  aches and pains , sore throat, diarrhoea , conjunctivitis , headache , loss of taste or smell ,a rash on skin, or discolouration of fingers or toes \n"
                         "\n"
                         "Serious symptoms      : difficulty breathing or shortness of breath , chest pain or pressure , loss of speech or movement.\n"
                         "\n"
                         "What is Covid  :  Coronaviruses are a family of viruses that can cause illnesses such as the common cold, severe acute respiratory syndrome (SARS) and Middle East respiratory syndrome (MERS). In 2019, a new coronavirus was identified as the cause of a disease outbreak that originated in China.\n"
                         "\n"
                         "for more information visit this : https://www.mayoclinic.org/diseases-conditions/coronavirus/symptoms-causes/syc-20479963" )
                         

@bot.message_handler(commands = ["2"])
def on_info(message):
    bot.reply_to(message,"1.Clean your hands often. Use soap and water, or an alcohol-based hand rub.\n"
                        "2.Maintain a safe distance from anyone who is coughing or sneezing.\n"
                        "3.Don’t touch your eyes, nose or mouth.\n"
                        "4.Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n"
                        "5.Stay home if you feel unwell.\n"
                        "6.If you have a fever, cough and difficulty breathing, seek medical attention. Call in advance.\n"
                        "7.Follow the directions of your local health authority.\n"
                        "8.STAY HOME STAY SAFE.")


@bot.message_handler(commands = ["3"])
def on_info(message):
    bot.reply_to(message, "go to these links below For Positive Harmonies \n "
                          "\n"
                          "http://sagarmala.gov.in/media/awareness-covid-19/video \n"
                          "https://www.facebook.com/MyGovIndia/videos/india-fights-corona-positive-harmonies/1294169247439377/")




@bot.message_handler(commands = ["4"])
def on_info(message):
    bot.reply_to(message, "For any Emergency contact : phno : 011-23978046 \n"
                 "TollFree Number : 1075 \n"
                 "gmail : ncov2019@gov.in \n"
                 "\n"
                 "For Behavioural Health : psycho-social \n"
                 "phno : 08046110007 \n"
                 "\n"
                 "MHA Central control  room for covid \n"
                 "toll-free Number : 1930 \n"
                 "\n"
                 "For the safety of self,society and country , please download Aarogya Setu Mobile app and bluetooth on...!!! \n"
                 "https://web.swaraksha.gov.in/in/ \n"
                 "\n"
                 "Help Line Numbers of each state :\n"
"""S. No Name of the State  Helpline Nos.

    1  Andhra Pradesh      0866-2410978
    2  Arunachal Pradesh   9436055743
    3  Assam               6913347770
    4  Bihar               104
    5  Chhattisgarh        104
    6  Goa                 104
    7  Gujarat             104
    8  Haryana             8558893911
    9  Himachal Pradesh    104
    10 Jharkhand           104
    11 Karnataka           104
    12 Kerala              0471-2552056
    13 Madhya Pradesh      104
    14 Maharashtra         020-26127394
    15 Manipur             3852411668
    16 Meghalaya           108
    17 Mizoram             102
    18 Nagaland            7005539653
    19 Odisha              9439994859
    20 Punjab              104
    21 Rajasthan           0141-2225624
    22 Sikkim              104
    23 Tamil Nadu          044-29510500
    24 Telangana           104
    25 Tripura             0381-2315879
    26 Uttarakhand         104
    27 Uttar Pradesh       18001805145
    28 West Bengal         1800313444222, 03323412600

    
    S. No   Name of                        Helpline Nos
            Union Territory (UT)

    1       Andaman and Nicobar Islands     03192-232102
    2       Chandigarh                      9779558282
    3       Dadra and Nagar Haveli and
            Daman & Diu                      104
    4       Delhi                           011-22307145
    5       Jammu & Kashmir                 01912520982, 0194-2440283
    6       Ladakh                          01982256462
    7       Lakshadweep                     104
    8       Puducherry                      104""")




@bot.message_handler(commands = ["5"])
def on_info(message):
    bot.reply_to(message, "Fact 1. Covid-19 and SARS-CoV-2 are not the same thing. Covid-19 is a disease (D stands for disease) caused by a new coronavirus. SARS-CoV-2 is the name of the virus itself.\n"
                 "\n"
"Fact 2. CoV is short for CoronaVirus, Coronavirus. This is the name of the family of viruses (there are about 40 of them), which bear resemblance with the solar corona due to the spinous crests.\n"
"\n"
"Fact 3. The term new coronavirus (novel or nCoV) means that before neither scientists nor the cells met this virus before.\n"
"\n"
"Fact 4. Over 2 million years of evolution, our immune system has learned to deal with most known infections, but the new coronavirus catches it by surprise, this it’s so hard to cope with and quite easy to get infected.\n"
"\n"
"Fact 5. One of the most unusual symptoms of coronavirus is the loss of a sense of taste and/or smell.\n"
"\n"
"\n"
"Are you willing to know more facts go to below link\n"
"\n"
"https://112.international/society/78-facts-about-coronavirus-50113.htmlV \n"
                 "THANK YOU  /info")




@bot.message_handler(commands = ["health_tips"])
def on_info(message):
    bot.reply_to(message, "Ask your self first \n"
                 "What you think about health??? \n"
                 "Is good health means eating which like??? \n"
                 "And also that ask your self about R U A real foodie and also which type of foodie u r??? \n"
                 "Like Only to eat Fruits,Vegetables etc...,, or \n Likely to eat food u wanna \n"
                 
                 "These Questions will make u think about yourself health \n"
                 
                 "so here some tips :\n"
                                      "\n"
                                      "1.Eat a variety of foods \n "
                                      "2.Base your diet on plenty of foods rich in carbohydrates\n"
                                      "3.Replace saturated with unsaturated fat\n"
                                      "4.Enjoy plenty of fruits and vegetables\n"
                                      "5.Reduce salt and sugar intake\n"
                                      "6.Eat regularly, control the portion size\n"
                                      "7.Drink plenty of fluids\n"
                                      "8.Maintain a healthy body weight\n"
                                      "9.Get on the move, make it a habit!\n"
                                      " Start now! And keep changing gradually.\n"
                                      "\n"
                                      "\n"
                                      "I think with the help of health diet you need some thing more , So do u think it is /exercise then move click on the that with smile")
    


@bot.message_handler(commands = ["exercise"])
def on_exercise(message):
    bot.reply_to(message ,"Do we really need this ??? \n"
                          "I am not shore\n"
                          "so we directly go to this \n"
                          "\n"
                          "\n"
                         "https://www.healthline.com/health/fitness-exercise/at-home-workouts"
                         "https://www.acefitness.org/education-and-resources/lifestyle/blog/6593/top-25-at-home-exercises/ \n"
                         "\n"
                         "If we are doing some thing we should know benefits right so click here for /benefits_exercise \n")



@bot.message_handler(commands = ["benefits_exercise"])
def on_exercise(message):
    bot.reply_to(message ,"""1. Help you control your weight. Along with diet, exercise plays an important role in controlling your weight and preventing obesity. To maintain your weight, the calories you eat and drink must equal the energy you burn. To lose weight, you must use more calories than you eat and drink.
Reduce your risk of heart diseases.
2. Exercise strengthens your heart and improves your circulation. The increased blood flow raises the oxygen levels in your body.
3. This helps lower your risk of heart diseases such as high cholesterol, coronary artery disease, and heart attack.
4. Regular exercise can also lower your blood pressure and triglyceride levels.
5. Help your body manage blood sugar and insulin levels.
6. Exercise can lower your blood sugar level and help your insulin work better.
7. This can cut down your risk for metabolic syndrome and type 2 diabetes. And if you already have one of those diseases, exercise can help you to manage it.
8. Help you quit smoking. Exercise may make it easier to quit smoking by reducing your cravings and withdrawal symptoms.
9.It can also help limit the weight you might gain when you stop smoking.
10. During exercise, your body releases chemicals that can improve your mood and make you feel more relaxed.

            THANK YOU A LOT FOR SPENDING YOUR TIME ON THIS BOT i think so you got some information
                            THANK YOU..  /info:) :) :)""")

                 

#corona = br.find_all('div' , class_ = "field field-name-field-covid-statewise-data field-type-field-collection field-label-above")
    
@bot.message_handler(commands = ["state"])
def  process_details_step(message):
    br = RoboBrowser(user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')
    br.open('https://www.mygov.in/corona-data/covid19-statewise-status/')

    
    try:
        chat_id = message.chat.id
        state= message.text
        l.append(state)
        msg = bot.reply_to(message, """ Which state information do u need??? \n
            for moving back use /info \n
            After process of one state To get details of other state click on /state and then type another state name(eg : Telengana)
                           1.Andaman and Nicobar
                           2.Andhra Pradesh
                           3.Arunachal Pradesh
                           4.Assam
                           5.Bihar
                           6.Chandigarh
                           7.Chhattisgarh
                           8.Dadra and Nagar Haveli
                           9.Daman and Diu
                           10.Delhi
                           11.Goa
                           12.Gujarat
                           13.Haryana
                           14.Himachal Pradesh
                           15.Jammu and Kashmir
                           16.Jharkhand
                           17.Karnataka
                           18.Kerala
                           19.Ladakh
                           20.Lakshadweep
                           21.Maharashtra
                           22.Manipur
                           23.Meghalaya
                           24.Mizoram
                           25.Madhya Pradesh
                           26.Nagaland
                           27.Odisha
                           28.Puducherry
                           29.Punjab
                           30.Rajasthan
                           31.Sikkim
                           32.Tamil Nadu
                           33.Telengana
                           34.Tripura
                           35.Uttar Pradesh
                           36.Uttarakhand
                           37.West Bengal \n
                           \n
                           The above all are the states and union territories if you want any details on covid cases type the correct spelling in same as above
                           For more information on covid click on /Covid_detail""")



        
        bot.register_next_step_handler(msg, process_details1_step)
    except Exception as e:
        bot.reply_to(message , 'ooops')
   

def  process_details1_step(message):
                                                                         
    
    br = RoboBrowser(user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')
    br.open('https://www.mygov.in/corona-data/covid19-statewise-status/')
    print(l)
    soup = br.parsed
    
    order_tag = soup.find_all('div')
    state = message.text
    try:  
        for i in range(len(order_tag)):
            if (order_tag[i].text.strip()== state):
                index1 = int(i)
                bot.reply_to(message,order_tag[i].text.strip()+(order_tag[i+2].text.strip())
                             +(order_tag[i+6].text.strip())+(order_tag[i+10].text.strip())+(order_tag[i+14].text.strip()))
    except Exception as e:
        bot.reply_to(message, 'Spelling Mistake')
                            

@bot.message_handler(commands = ["command"])
def on_exercise(message):
    bot.reply_to(message ,"""   /start : to get start the bot
  /info  : to give information what they want and also how to move to the information
  /Covid_detail : this gives information about the covid
  /health_tips : this gives some health tips
  /state : it gives information about the covid cases of  particular state """)
                              

@bot.message_handler(commands = ["description"])
def on_exercise(message):
    bot.reply_to(message ,""" This Bot gives Information about Covid and also health tips \n
If u want to know how to use it type /command or click on that \n To get the Case details you have to type name  the  command state or click on that   """)

@server.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
  
  
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://covid-vs-health-bot.herokuapp.com/' + API_TOKEN)
    return "!", 200
  
  
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

bot.polling()
