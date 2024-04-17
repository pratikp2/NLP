Chatbot for food orders online delivery using Dialogflow
===================
Build a chatbot for food orders online delivery using Google's Dialogflow ES. This bot supports two options,

1) New Order
2) Track Order

1) New Order: Sample Conversation

```
Bot: How can I help you? You can say things like (1) New Order (2) Track Order
User: New Order
Bot: What would you like to have? You can say things like 2 pizzas, one vada pav.
     Only order from this list: Vada Pav, Pav Bhaji, Mango Lassi, Pizza, Rava Dosa, Masala Dosa, Samosa
User: I would like to have 2 Rava Dosa and one plate of samosa
Bot: Added 2 Rava Dosa and 1 Samosa. Anything else?
User: Oh yes, add one mango lassi, please
Bot: Sure. Now we have 2 Rava Dosa, 1 Samosa and 1 Mango Lassi. Anything else?
User: Well, you know my cholesterol came high so let's remove Samosa
Bot: Sure. Now we have 2 Rava Dosa and 1 Mango Lassi. Anything else?
User: Nope. That's it
Bot: Awesome. Your order has been placed. Order id # 45. Your total bill is 19$ which you can pay at the time of delivery!
```

2) Track Order: Sample Conversation

```Bot: How can I help you? You can say things like (1) New Order (2) Track Order
User: Track Order
Bot: What is your order id?
User: 45
Bot: Order # 45, is in transit
User: How about 41
Bot: Order # 41 is delivered
```

Directory structure
===================
backend: Contains Python FastAPI backend code
db: contains the dump of the database. you need to import this into your MySQL db by using MySQL workbench tool
dialogflow_assets: this has training phrases etc. for our intents
frontend: website code

Install these modules
======================

pip install mysql-connector
pip install "fastapi[all]"

OR just run pip install -r backend/requirements.txt to install both in one shot

To start fast API backend server
================================
1. Go to the backend directory in your command prompt
2. Run this command: uvicorn main:app --reload

ngrok for https tunneling
================================
1. To install ngrok, go to https://ngrok.com/download and install ngrok version that is suitable for your OS
2. Extract the zip file and place ngrok.exe in a folder.
3. Open windows command prompt, go to that folder and run this command: ngrok http 80000

NOTE: ngrok can timeout. you need to restart the session if you see a session expired message.



================================
Steps to Run the Project : 
================================
1. Complete DialogFlow chatbot and enable web hook in Fullfillment section
2. Run Backend server using "python -m uvicorn main:app --reload" or "uvicorn main:app --reload" if dependencies are resolved.
3. pick the url given by uvicorn and paste it in webhook section it should be something like 127.0.0.1:<port number>, which is also localhost ip so you can simply copy and paste http://localhost:8000 .
4. You will encounter once problem that webhook accepts only https url so port forwarding to secure url is needed. we can use ngrok for that.
5. ngrok will take specified port number from localhost and forward it to a secure i.e, a "https" link and way to use it is "ngrok http <port number>" most probably "ngrok http 8000"
6. If using for 1st time it promp an error and tell you to create an account on ngrok and install auth token on device once that is done run command once again and it will generate https url. Pick it and past it in webhook section.