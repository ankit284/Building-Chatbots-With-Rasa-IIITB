# Building-Chatbots-With-Rasa-IIITB
Building Chatbots With Rasa

## Introduction
Welcome to the module on ‘Building Chatbots with Rasa’.

Chatbots have become popular in a large number of business domains. Companies are building chatbots for booking hotels, flights, movies etc., customer support, enquiring bus and train schedules, tax saving advice, accessing stock market information etc.

Why are they getting so much attention? The reason is simple: they help reduce the time, effort and cost required to get a task done (and if designed well, improve user experience also).  

There are two broad types of chatbots - generic chatbots and domain-specific chatbots.

Generic chatbots, also called virtual assistants, such as Google Assistant, Amazon’s Alexa, Microsoft’s Cortana or Apple’s Siri, are used to answer generic queries such as dialling a phone number, dropping a message to a contact, booking a calendar slot, fetching results from a web search, etc. These systems have been trained on massive amounts of user data, encyclopedias, conversational dialogues with humans etc.

The other type is the domain-specific, task-oriented chatbot. By domain-specific and task-oriented, we mean that it can handle queries pertaining to a particular domain or type of task. For example, a ‘weather bot’ can only tell weather predictions. It cannot book a table in a restaurant or set up an alarm. Similarly, a restaurant discovery bot can help you find restaurants in several cities, though it might not be able to answer general questions such as "Who is the prime minister of India?".

## In this Module
In this module, you will learn to build a domain-specific chatbot: a restaurant search chatbot. The bot will be able to 'talk' to users in English and will help them search for restaurants in several cities, of multiple cuisine types, budgets etc. You’re going to use an open source framework for building conversational bots  - Rasa.

Through this project, you will be able to deploy a real-world application on the web, and, in the process, learn many useful skills required to develop and deploy ML products. 

## Problem Statement
An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. You have been hired as the lead data scientist for creating this product.

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.

The bot takes the following inputs from the user:

City: Take the input from the customer as a text field. For example:

Bot: In which city are you looking for restaurants?

User: anywhere in Delhi

### Important Notes: 

Assume that Foodie works only in Tier-1 and Tier-2 cities. You can use the current HRA classification of the cities from here. Under the section 'current classification' on this page, the table categorizes cities as X, Y and Z. Consider 'X ' cities as tier-1 and 'Y' as tier-2. 
The bot should be able to identify common synonyms of city names, such as Bangalore/Bengaluru, Mumbai/Bombay etc.

Your chatbot should provide results for tier-1 and tier-2 cities only, while for tier-3 cities, it should reply back with something like "We do not operate in that area yet".

Cuisine Preference: Take the cuisine preference from the customer. The bot should list out the following six cuisine categories (Chinese, Mexican, Italian, American, South Indian & North Indian) and the customer can select any one out of that. Following is an example for the same:

Bot: What kind of cuisine would you prefer?

Chinese
Mexican
Italian
American
South Indian
North Indian
User: I’ll prefer Italian!

Average budget for two people: Segment the price range (average budget for two people) into three price categories: lesser than 300, 300 to 700 and more than 700. The bot should ask the user to select one of the three price categories. For example:

Bot: What price range are you looking at?

Lesser than Rs. 300
Rs. 300 to 700
More than 700
User: in range of 300 to 700

While showing the results to the user, the bot should display the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). The format should be: {restaurant_name} in {restaurant_address} has been rated {rating}.

Finally, the bot should ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot should ask for user’s email id and then send it over email. Else, just reply with a 'goodbye' message. The mail should have the following details for each restaurant:

Restaurant Name
Restaurant locality address
Average budget for two people
Zomato user rating
You can refer to the following links on how to send emails through Python:

Python Email Package
Python Flask Mail
(A heads up: You'll have to enable secure access on Gmail to allow Python to send emails).

You have been given some sample conversational stories in the ‘test’ file. Look at the stories and try to observe entities, intents, dialogue-flow which may be useful to train the NLU and also the dialogue flow.

## Goals of this Project
In this project, you will build a chatbot for ‘Foodie’ and then deploy it on Slack. The folder with starter codes has already been shared with you in session-1. You need to accomplish the following in the project:

NLU training: You can use rasa-nlu-trainer to create more training examples for entities and intents. Try using regex features and synonyms for extracting entities.

Build actions for the bot. Read through the Zomato API documentation to extract the features such as the average price for two people and restaurant’s user rating. You also need to build an ‘action’ for sending emails from Python.

Creating more stories: Use train_online.py file to create more stories. Refer to the sample conversational stories provided above.  Your bot will be evaluated on something similar to the test stories shared.
