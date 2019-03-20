## greet story
* greet
    - utter_greet

## greet and default story
* greet
    - utter_greet
* default
    - utter_default
    - utter_goodbye
    - action_goodbye
    - export

## default story
* default
    - utter_default
    - utter_goodbye
    - action_goodbye
    - export

## location intent
* location
    - action_restaurant

## cuisine intent
* cuisine
    - action_restaurant

## budget intent
* budget
    - action_restaurant

## Goodbye story
* goodbye
    - utter_goodbye
    - action_goodbye
    - export

## Generated Story Mail
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "hyd"}
    - slot{"location": "hyd"}
    - utter_ask_cuisine
* cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"cuisine": "chinese"}
* cuisine{"budget": "300"}
    - slot{"budget": "300"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"lat": 33.8495}
    - slot{"lon": -87.2714}
    - slot{"city_id": 4067}
    - slot{"cuisine_key": "25"}
    - slot{"api_response": "{\"1\":[\"Sakura Japanese Restaurant\",\"300 Highway 78 W, Jasper\",\"25\",\"3.6\"],\"2\":[\"China Gourmet\",\"902 Highway 78 E, Jasper 35501\",\"10\",\"3.6\"],\"3\":[\"Lin Garden II\",\"300 Hwy 78, Jasper 35501\",\"10\",\"3.5\"],\"4\":[\"Golden Dragon\",\"1814 21st St, Haleyville 35565\",\"0\",\"3.7\"],\"5\":[\"China Gourmet\",\"42461 Hwy 195, Haleyville 35565\",\"0\",\"3.2\"],}"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - slot{"api_response": "{\"1\":[\"Sakura Japanese Restaurant\",\"300 Highway 78 W, Jasper\",\"25\",\"3.6\"],\"2\":[\"China Gourmet\",\"902 Highway 78 E, Jasper 35501\",\"10\",\"3.6\"],\"3\":[\"Lin Garden II\",\"300 Hwy 78, Jasper 35501\",\"10\",\"3.5\"],\"4\":[\"Golden Dragon\",\"1814 21st St, Haleyville 35565\",\"0\",\"3.7\"],\"5\":[\"China Gourmet\",\"42461 Hwy 195, Haleyville 35565\",\"0\",\"3.2\"],}"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@gmail.com"}
    - slot{"email": "test@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
* goodbye
    - utter_goodbye
    - action_goodbye
    - export

## Generated Story No-Mail
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "hyd"}
    - slot{"location": "hyd"}
    - utter_ask_cuisine
* cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"cuisine": "chinese"}
* cuisine{"budget": "300"}
    - slot{"budget": "300"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"lat": 33.8495}
    - slot{"lon": -87.2714}
    - slot{"city_id": 4067}
    - slot{"cuisine_key": "25"}
    - slot{"api_response": "{\"1\":[\"Sakura Japanese Restaurant\",\"300 Highway 78 W, Jasper\",\"25\",\"3.6\"],\"2\":[\"China Gourmet\",\"902 Highway 78 E, Jasper 35501\",\"10\",\"3.6\"],\"3\":[\"Lin Garden II\",\"300 Hwy 78, Jasper 35501\",\"10\",\"3.5\"],\"4\":[\"Golden Dragon\",\"1814 21st St, Haleyville 35565\",\"0\",\"3.7\"],\"5\":[\"China Gourmet\",\"42461 Hwy 195, Haleyville 35565\",\"0\",\"3.2\"],}"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - slot{"api_response": "{\"1\":[\"Sakura Japanese Restaurant\",\"300 Highway 78 W, Jasper\",\"25\",\"3.6\"],\"2\":[\"China Gourmet\",\"902 Highway 78 E, Jasper 35501\",\"10\",\"3.6\"],\"3\":[\"Lin Garden II\",\"300 Hwy 78, Jasper 35501\",\"10\",\"3.5\"],\"4\":[\"Golden Dragon\",\"1814 21st St, Haleyville 35565\",\"0\",\"3.7\"],\"5\":[\"China Gourmet\",\"42461 Hwy 195, Haleyville 35565\",\"0\",\"3.2\"],}"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
* goodbye
    - utter_goodbye
    - export

## Story with No service to city
* restaurant_search{"location": "raebareli"}
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"location": null}
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_restaurant
    - slot{"location": "faridabad"}
* cuisine{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "1500"}
    - slot{"budget": "1500"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": 28.3956}
    - slot{"lon": 77.319399}
    - slot{"city_id": 1}
    - slot{"cuisine_key": "50"}
    - slot{"api_response": "{\"1\":[\"Ministry Of Beer\",\"M 43, Outer Circle, Connaught Place, New Delhi\",\"1500\",\"4.9\"],\"2\":[\"Feel ALIVE\",\"SCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\",\"1200\",\"4.9\"],\"3\":[\"38 Barracks\",\"M-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\",\"1600\",\"4.8\"],\"4\":[\"Punjabi Angithi\",\"Shop 32-22, A-4, DDA Market, Paschim Vihar, New Delhi\",\"500\",\"4.8\"],\"5\":[\"The Hook\",\"SCO 30, Sector 29, Gurgaon\",\"1600\",\"4.8\"],\"6\":[\"Sanadige\",\"22/48, Commercial Centre, Chanakyapuri, New Delhi\",\"2200\",\"4.8\"],\"7\":[\"Phonebooth Reloaded\",\"G14b, Ground Floor, Vijay Nagar, Hudson lane, Delhi University-GTB Nagar, New Delhi\",\"1000\",\"4.8\"],\"8\":[\"Cafe Cones & Curries\",\"A44&44 Galaxybusiness park galactic court shop no 8\",\"400\",\"4.8\"],\"9\":[\"Mellow Garden\",\"J2/7, 2nd & 3rd Floor, BK Dutta Market, Rajouri Garden, New Delhi\",\"1200\",\"4.8\"],\"10\":[\"The Mughal Trail\",\"BK Dutt Market, Rajouri Garden, New Delhi\",\"500\",\"4.8\"]}"}
    - action_restaurant
    - slot{"location": "faridabad"}
    - slot{"api_response": "{\"1\":[\"Ministry Of Beer\",\"M 43, Outer Circle, Connaught Place, New Delhi\",\"1500\",\"4.9\"],\"2\":[\"Feel ALIVE\",\"SCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\",\"1200\",\"4.9\"],\"3\":[\"38 Barracks\",\"M-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\",\"1600\",\"4.8\"],\"4\":[\"Punjabi Angithi\",\"Shop 32-22, A-4, DDA Market, Paschim Vihar, New Delhi\",\"500\",\"4.8\"],\"5\":[\"The Hook\",\"SCO 30, Sector 29, Gurgaon\",\"1600\",\"4.8\"],\"6\":[\"Sanadige\",\"22/48, Commercial Centre, Chanakyapuri, New Delhi\",\"2200\",\"4.8\"],\"7\":[\"Phonebooth Reloaded\",\"G14b, Ground Floor, Vijay Nagar, Hudson lane, Delhi University-GTB Nagar, New Delhi\",\"1000\",\"4.8\"],\"8\":[\"Cafe Cones & Curries\",\"A44&44 Galaxybusiness park galactic court shop no 8\",\"400\",\"4.8\"],\"9\":[\"Mellow Garden\",\"J2/7, 2nd & 3rd Floor, BK Dutta Market, Rajouri Garden, New Delhi\",\"1200\",\"4.8\"],\"10\":[\"The Mughal Trail\",\"BK Dutt Market, Rajouri Garden, New Delhi\",\"500\",\"4.8\"]}"}
    - slot{"budget": "1500"}
    - slot{"cuisine": "north indian"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@gmail.com"}
    - slot{"email": "test@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
* goodbye
    - utter_goodbye
    - export

## Generated Story No Cuisine Find send mail
* restaurant_search{"cuisine": "north indian", "location": "erode"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "erode"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"cuisine": null}
* cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "jpr.saurabh@gmail.com"}
    - slot{"email": "jpr.saurabh@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
* goodbye
    - utter_goodbye
    - export

## Generated Story No Cuisine Find send mail
* restaurant_search{"cuisine": "north indian", "location": "erode"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "erode"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"cuisine": null}
* cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
* goodbye
    - utter_goodbye
    - export

## Generated Story no cuisine found email not sent
* restaurant_search{"cuisine": "north indian", "location": "erode"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "erode"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"cuisine": null}
* cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
* goodbye
    - utter_goodbye
    - export

## Generated Story -3065047515619587552 Mail  with no reset
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_restaurant
    - slot{"cuisine": "pune"}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "600"}
    - slot{"budget": "600"}
    - slot{"lat": 18.520469}
    - slot{"lon": 73.85662}
    - slot{"city_id": 5}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Laa Unico\",\"Arihant Aura Building, Above Comet Stationery, Next to Sujay Garden, Commercial Complex, Near Laxmi Narayan Theatre, Mukundnagar, Swargate, Pune\",\"1100\",\"4.8\"],\"2\":[\"Chili's American Grill & Bar\",\"UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune\",\"1400\",\"4.8\"],\"3\":[\"Agent Jack's\",\"Ground Floor, Kapila Matrix, Koregaon Park Annexe, Mundhwa, Pune\",\"1300\",\"4.7\"],\"4\":[\"Cafe 1730\",\"21/1, Serene Bay, Lane 6, Off North Main Road, Koregaon Park, Pune\",\"1500\",\"4.6\"],\"5\":[\"Darshan\",\"759/60, Prabhat Road, Opposite Indian Bank, Deccan Gymkhana, Pune\",\"700\",\"4.6\"],\"6\":[\"Baraza Bars & Bites\",\"Unit 10, Pubtown, Creaticity Mall, Shastri Nagar, Yerawada, Pune\",\"1400\",\"4.6\"],\"7\":[\"Effingut Brewerkz\",\"End of Lane Number 6, Koregaon Park, Pune\",\"1700\",\"4.6\"],\"8\":[\"Hard Rock Cafe\",\"81/82, East Main Road, Koregaon Park Extension, Mundhwa, Pune\",\"2500\",\"4.6\"],\"9\":[\"Agent Jack's\",\"West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune\",\"1300\",\"4.6\"],\"10\":[\"GeoBistro\",\"Row House 2, Nand Gaon, Clover Park, Datta Mandir Chowk, Behind Phoenix Market City, Viman Nagar, Pune\",\"1300\",\"4.6\"]}"}
    - action_restaurant
    - slot{"location": "pune"}
    - slot{"api_response": "{\"1\":[\"Laa Unico\",\"Arihant Aura Building, Above Comet Stationery, Next to Sujay Garden, Commercial Complex, Near Laxmi Narayan Theatre, Mukundnagar, Swargate, Pune\",\"1100\",\"4.8\"],\"2\":[\"Chili's American Grill & Bar\",\"UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune\",\"1400\",\"4.8\"],\"3\":[\"Agent Jack's\",\"Ground Floor, Kapila Matrix, Koregaon Park Annexe, Mundhwa, Pune\",\"1300\",\"4.7\"],\"4\":[\"Cafe 1730\",\"21/1, Serene Bay, Lane 6, Off North Main Road, Koregaon Park, Pune\",\"1500\",\"4.6\"],\"5\":[\"Darshan\",\"759/60, Prabhat Road, Opposite Indian Bank, Deccan Gymkhana, Pune\",\"700\",\"4.6\"],\"6\":[\"Baraza Bars & Bites\",\"Unit 10, Pubtown, Creaticity Mall, Shastri Nagar, Yerawada, Pune\",\"1400\",\"4.6\"],\"7\":[\"Effingut Brewerkz\",\"End of Lane Number 6, Koregaon Park, Pune\",\"1700\",\"4.6\"],\"8\":[\"Hard Rock Cafe\",\"81/82, East Main Road, Koregaon Park Extension, Mundhwa, Pune\",\"2500\",\"4.6\"],\"9\":[\"Agent Jack's\",\"West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune\",\"1300\",\"4.6\"],\"10\":[\"GeoBistro\",\"Row House 2, Nand Gaon, Clover Park, Datta Mandir Chowk, Behind Phoenix Market City, Viman Nagar, Pune\",\"1300\",\"4.6\"]}"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@gmail.com"}
    - slot{"email": "test@gmail.com"}
    - action_send_email
    - slot{"email": "test@gmail.com"}
* goodbye
    - utter_goodbye
    - action_goodbye
    - export

## Generated Story 3157501464517625217
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"lat": 17.366}
    - slot{"lon": 78.476}
    - slot{"city_id": 6}
    - slot{"cuisine_key": "25"}
    - slot{"api_response": "{\"1\":[\"AB's - Absolute Barbecues\",\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1500\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"5\":[\"Exotica\",\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"1500\",\"4.7\"],\"6\":[\"Mekong - Marigold Hotel\",\"Green Lands, Begumpet, Hyderabad\",\"2500\",\"4.7\"],\"7\":[\"The Fisherman's Wharf\",\"304, Puppalaguda, Financial District,ISB - Outer Ring Road, Gachibowli, Hyderabad\",\"1500\",\"4.6\"],\"8\":[\"SodaBottleOpenerWala\",\"Unit 4, Ground Floor, Niharika Jubilee One, Road 1, Jubilee Hills, Hyderabad\",\"1400\",\"4.6\"],\"9\":[\"Barbeque Pride\",\"790, Rangoli Building, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.6\"],\"10\":[\"Prost Brew Pub\",\"882/A Road No 45, Jubilee Hills, Hyderabad\",\"2200\",\"4.6\"]}"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - slot{"api_response": "{\"1\":[\"AB's - Absolute Barbecues\",\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1500\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"5\":[\"Exotica\",\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"1500\",\"4.7\"],\"6\":[\"Mekong - Marigold Hotel\",\"Green Lands, Begumpet, Hyderabad\",\"2500\",\"4.7\"],\"7\":[\"The Fisherman's Wharf\",\"304, Puppalaguda, Financial District,ISB - Outer Ring Road, Gachibowli, Hyderabad\",\"1500\",\"4.6\"],\"8\":[\"SodaBottleOpenerWala\",\"Unit 4, Ground Floor, Niharika Jubilee One, Road 1, Jubilee Hills, Hyderabad\",\"1400\",\"4.6\"],\"9\":[\"Barbeque Pride\",\"790, Rangoli Building, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.6\"],\"10\":[\"Prost Brew Pub\",\"882/A Road No 45, Jubilee Hills, Hyderabad\",\"2200\",\"4.6\"]}"}
    - slot{"budget": "700"}
    - slot{"cuisine": "chinese"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye    
    - export

## Generated Story 2045042345727052638
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* cuisine{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "italian"}
    - slot{"lat": 17.366}
    - slot{"lon": 78.476}
    - slot{"city_id": 6}
    - slot{"cuisine_key": "55"}
    - slot{"api_response": "{\"1\":[\"Con\u00e7u\",\"Plot no 738, Road no. 37, Jubilee Hills, Hyderabad\",\"600\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"AB's - Absolute Barbecues\",\"8-2-618/10-11, 2nd Floor, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad\",\"1500\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.9\"],\"5\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"6\":[\"The Roastery Coffee House\",\"8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\",\"800\",\"4.8\"],\"7\":[\"Churrolto\",\"Ground Floor, Shop 3, Opposite IndusInd Bank, Madhapur Main Road, Madhapur, Hyderabad\",\"1200\",\"4.8\"],\"8\":[\"Natural Ice Cream\",\"Shop G2, Ground Floor, J.P.Tower, Next To Ashoka Bhopal Chamber , S P Road, Secunderabad\",\"200\",\"4.8\"],\"9\":[\"Coffee Cup\",\"E 89, 1rst floor, Above Canara Bank, Sainikpuri, Secunderabad\",\"800\",\"4.7\"],\"10\":[\"B-Dubs\",\"Plot 806, Axis Tower, Road Number 36, Jubilee Hills, Hyderabad\",\"1600\",\"4.7\"]}"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - slot{"api_response": "{\"1\":[\"Con\u00e7u\",\"Plot no 738, Road no. 37, Jubilee Hills, Hyderabad\",\"600\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"AB's - Absolute Barbecues\",\"8-2-618/10-11, 2nd Floor, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad\",\"1500\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.9\"],\"5\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"6\":[\"The Roastery Coffee House\",\"8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\",\"800\",\"4.8\"],\"7\":[\"Churrolto\",\"Ground Floor, Shop 3, Opposite IndusInd Bank, Madhapur Main Road, Madhapur, Hyderabad\",\"1200\",\"4.8\"],\"8\":[\"Natural Ice Cream\",\"Shop G2, Ground Floor, J.P.Tower, Next To Ashoka Bhopal Chamber , S P Road, Secunderabad\",\"200\",\"4.8\"],\"9\":[\"Coffee Cup\",\"E 89, 1rst floor, Above Canara Bank, Sainikpuri, Secunderabad\",\"800\",\"4.7\"],\"10\":[\"B-Dubs\",\"Plot 806, Axis Tower, Road Number 36, Jubilee Hills, Hyderabad\",\"1600\",\"4.7\"]}"}
    - slot{"budget": "300"}
    - slot{"cuisine": "italian"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "ankit284@gmail.com"}
    - slot{"email": "ankit284@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Generated Story 7347419674474469148
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "chennai", "budget": "600"}
    - slot{"budget": "600"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "chennai"}
    - slot{"location": "chennai"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": 13.083889}
    - slot{"lon": 80.27}
    - slot{"city_id": 7}
    - slot{"cuisine_key": "50"}
    - slot{"api_response": "{\"1\":[\"Coal Barbecues\",\"17-18, Rajalakshmi Nagar, 7th Cross Street, 100 Feet Bypass Road, Velachery, Chennai\",\"1400\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"45, GN Chetty Road, T. Nagar, Chennai\",\"1400\",\"4.9\"],\"3\":[\"Coal Barbecues\",\"40, 2nd Floor, Bazullah Road, T. Nagar, Chennai\",\"1400\",\"4.9\"],\"4\":[\"AB's - Absolute Barbecues\",\"5th Floor, Vivira Mall, Navallur, Chennai\",\"1400\",\"4.9\"],\"5\":[\"Bhangra\",\"Mayajaal Multiplex, Kanathur, Chennai\",\"800\",\"4.9\"],\"6\":[\"AB's - Absolute Barbecues\",\"1st Floor, 1, New Street, Parvathi Avenue, Sakthi Nagar, Porur, Chennai\",\"1400\",\"4.9\"],\"7\":[\"AB's - Absolute Barbecues\",\"Velachery Tharamani Link Road, Opposite TCS, Velachery, Chennai\",\"1400\",\"4.9\"],\"8\":[\"Alchemy Bar & Lounge\",\"180, TTK Road, Alwarpet, Chennai\",\"1500\",\"4.9\"],\"9\":[\"Chili's American Grill & Bar\",\"49 & 50 L, Express Avenue Mall, White's Road, Royapettah, Chennai\",\"1400\",\"4.8\"],\"10\":[\"Bombay Lassi\",\"8, Bahar Agan Street, Anna Salai, Ellis Road, Behind Devi Theatre, Triplicane, Chennai\",\"100\",\"4.8\"]}"}
    - action_restaurant
    - slot{"location": "chennai"}
    - slot{"api_response": "{\"1\":[\"Coal Barbecues\",\"17-18, Rajalakshmi Nagar, 7th Cross Street, 100 Feet Bypass Road, Velachery, Chennai\",\"1400\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"45, GN Chetty Road, T. Nagar, Chennai\",\"1400\",\"4.9\"],\"3\":[\"Coal Barbecues\",\"40, 2nd Floor, Bazullah Road, T. Nagar, Chennai\",\"1400\",\"4.9\"],\"4\":[\"AB's - Absolute Barbecues\",\"5th Floor, Vivira Mall, Navallur, Chennai\",\"1400\",\"4.9\"],\"5\":[\"Bhangra\",\"Mayajaal Multiplex, Kanathur, Chennai\",\"800\",\"4.9\"],\"6\":[\"AB's - Absolute Barbecues\",\"1st Floor, 1, New Street, Parvathi Avenue, Sakthi Nagar, Porur, Chennai\",\"1400\",\"4.9\"],\"7\":[\"AB's - Absolute Barbecues\",\"Velachery Tharamani Link Road, Opposite TCS, Velachery, Chennai\",\"1400\",\"4.9\"],\"8\":[\"Alchemy Bar & Lounge\",\"180, TTK Road, Alwarpet, Chennai\",\"1500\",\"4.9\"],\"9\":[\"Chili's American Grill & Bar\",\"49 & 50 L, Express Avenue Mall, White's Road, Royapettah, Chennai\",\"1400\",\"4.8\"],\"10\":[\"Bombay Lassi\",\"8, Bahar Agan Street, Anna Salai, Ellis Road, Behind Devi Theatre, Triplicane, Chennai\",\"100\",\"4.8\"]}"}
    - slot{"budget": "600"}
    - slot{"cuisine": "north indian"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@gmail.com"}
    - slot{"email": "test@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - utter_goodbye
    - export


## Generated Story 6306051370544604132
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "delhi", "budget": "600"}
    - slot{"budget": "600"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "delhi"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "south indian"}
    - slot{"lat": 28.625789}
    - slot{"lon": 77.210276}
    - slot{"city_id": 1}
    - slot{"cuisine_key": "85"}
    - slot{"api_response": "{\"1\":[\"Sanadige\",\"22/48, Commercial Centre, Chanakyapuri, New Delhi\",\"2200\",\"4.8\"],\"2\":[\"Indian Grill Room\",\"315, 3rd Floor, Suncity Business Tower, Golf Course Road, Gurgaon\",\"1800\",\"4.7\"],\"3\":[\"Masala House\",\"4, Sunder Nagar, New Delhi\",\"1800\",\"4.7\"],\"4\":[\"Verandah Moonshine\",\"2/85, Third Floor, West Punjabi Bagh Club Road, Punjabi Bagh, New Delhi\",\"1500\",\"4.6\"],\"5\":[\"Zambar\",\"Address: Shop Number 310, 3rd floor Ambience mall DLF Phase 3, Gurgaon Haryana\",\"1500\",\"4.5\"],\"6\":[\"Bikkgane Biryani\",\"252, Shahpur Jat, New Delhi\",\"800\",\"4.5\"],\"7\":[\"Carnatic Cafe\",\"32nd Milestone, NH 8, Sector 15, Gurgaon\",\"500\",\"4.5\"],\"8\":[\"Decode\",\"J2/1 ,BK Dutta Market, Rajouri Garden, New Delhi\",\"1200\",\"4.4\"],\"9\":[\"Sankalp\",\"House 4, Vaishali Enclave, Pitampura, New Delhi\",\"750\",\"4.4\"],\"10\":[\"Juggernaut\",\"HS-16, Main Market, Kailash Colony, New Delhi\",\"600\",\"4.4\"]}"}
    - action_restaurant
    - slot{"location": "delhi"}
    - slot{"api_response": "{\"1\":[\"Sanadige\",\"22/48, Commercial Centre, Chanakyapuri, New Delhi\",\"2200\",\"4.8\"],\"2\":[\"Indian Grill Room\",\"315, 3rd Floor, Suncity Business Tower, Golf Course Road, Gurgaon\",\"1800\",\"4.7\"],\"3\":[\"Masala House\",\"4, Sunder Nagar, New Delhi\",\"1800\",\"4.7\"],\"4\":[\"Verandah Moonshine\",\"2/85, Third Floor, West Punjabi Bagh Club Road, Punjabi Bagh, New Delhi\",\"1500\",\"4.6\"],\"5\":[\"Zambar\",\"Address: Shop Number 310, 3rd floor Ambience mall DLF Phase 3, Gurgaon Haryana\",\"1500\",\"4.5\"],\"6\":[\"Bikkgane Biryani\",\"252, Shahpur Jat, New Delhi\",\"800\",\"4.5\"],\"7\":[\"Carnatic Cafe\",\"32nd Milestone, NH 8, Sector 15, Gurgaon\",\"500\",\"4.5\"],\"8\":[\"Decode\",\"J2/1 ,BK Dutta Market, Rajouri Garden, New Delhi\",\"1200\",\"4.4\"],\"9\":[\"Sankalp\",\"House 4, Vaishali Enclave, Pitampura, New Delhi\",\"750\",\"4.4\"],\"10\":[\"Juggernaut\",\"HS-16, Main Market, Kailash Colony, New Delhi\",\"600\",\"4.4\"]}"}
    - slot{"budget": "600"}
    - slot{"cuisine": "south indian"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export


## Generated Story 8093714130561034807
* greet
    - utter_greet
* restaurant_search{"location": "Durg-BhilaiNagar", "cuisine": "south indian", "budget": "300"}
    - slot{"budget": "300"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Durg-BhilaiNagar"}
    - slot{"location": "durg-bhilainagar"}
    - slot{"cuisine": "south indian"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "ankit284@gmail.com"}
    - slot{"email": "ankit284@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - action_goodbye
    - export

## Generated Story 8093714130561034804
* greet
    - utter_greet
* restaurant_search{"location": "Durg-BhilaiNagar", "cuisine": "south indian", "budget": "300"}
    - slot{"budget": "300"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Durg-BhilaiNagar"}
    - slot{"location": "durg-bhilainagar"}
    - slot{"cuisine": "south indian"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Generated Story 1437510786200084872
* greet
    - utter_greet
* restaurant_search{"location": "raipur", "budget": "500", "cuisine": "north indian"}
    - slot{"budget": "500"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "raipur"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": 21.251703}
    - slot{"lon": 81.629684}
    - slot{"city_id": 11310}
    - slot{"cuisine_key": "50"}
    - slot{"api_response": "{\"1\":[\"Barbeque Nation\",\"Magneto Mall, Jevan Vihar, Shankar Nagar, Raipur\",\"1500\",\"4.6\"],\"2\":[\"Hotel Moon Darbar\",\"Mehbubiya Chowk, Gol Bazar, Moudhapara\",\"300\",\"4.3\"],\"3\":[\"Naivedya\",\"Jail Road, Raipur, Devendra Nagar, Raipur\",\"500\",\"4.2\"],\"4\":[\"Urban Grill\",\"Opposite Marine Drive, Telibandha, Civil Lines, Raipur\",\"700\",\"4.2\"],\"5\":[\"Yaaran Da Adda\",\"Opposite AIIMS Gate 5, Main Road, Tatibandh\",\"600\",\"4.2\"],\"6\":[\"Anna Punjabi\",\"Pachpedi Naka Chowk, Beside Nest, Mahaveer Nagar, Raipur\",\"600\",\"4.2\"],\"7\":[\"Girnar Restaurant\",\"Jaistambh Chowk, GE Road, Raipur (CG)\",\"500\",\"4.1\"],\"8\":[\"Vishvas Bhojanalaya\",\"Rathod Chowk, Ramsagar Pada, Jawahar Nagar, Raipur\",\"200\",\"4.1\"],\"9\":[\"Indian Coffee House\",\"Shyam Square Market, Pandri, Devendra Nagar Raipur\",\"500\",\"4.1\"],\"10\":[\"The Arabian Oasis\",\"Sixth Floor, Colors Mall, Pachpedi Naka, Mahaveer Nagar, Raipur\",\"800\",\"4.1\"]}"}
    - action_restaurant
    - slot{"location": "raipur"}
    - slot{"api_response": "{\"1\":[\"Barbeque Nation\",\"Magneto Mall, Jevan Vihar, Shankar Nagar, Raipur\",\"1500\",\"4.6\"],\"2\":[\"Hotel Moon Darbar\",\"Mehbubiya Chowk, Gol Bazar, Moudhapara\",\"300\",\"4.3\"],\"3\":[\"Naivedya\",\"Jail Road, Raipur, Devendra Nagar, Raipur\",\"500\",\"4.2\"],\"4\":[\"Urban Grill\",\"Opposite Marine Drive, Telibandha, Civil Lines, Raipur\",\"700\",\"4.2\"],\"5\":[\"Yaaran Da Adda\",\"Opposite AIIMS Gate 5, Main Road, Tatibandh\",\"600\",\"4.2\"],\"6\":[\"Anna Punjabi\",\"Pachpedi Naka Chowk, Beside Nest, Mahaveer Nagar, Raipur\",\"600\",\"4.2\"],\"7\":[\"Girnar Restaurant\",\"Jaistambh Chowk, GE Road, Raipur (CG)\",\"500\",\"4.1\"],\"8\":[\"Vishvas Bhojanalaya\",\"Rathod Chowk, Ramsagar Pada, Jawahar Nagar, Raipur\",\"200\",\"4.1\"],\"9\":[\"Indian Coffee House\",\"Shyam Square Market, Pandri, Devendra Nagar Raipur\",\"500\",\"4.1\"],\"10\":[\"The Arabian Oasis\",\"Sixth Floor, Colors Mall, Pachpedi Naka, Mahaveer Nagar, Raipur\",\"800\",\"4.1\"]}"}
    - slot{"budget": "500"}
    - slot{"cuisine": "north indian"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "ankit284@gmail.com"}
    - slot{"email": "ankit284@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Generated Story 1437510786200084872
* greet
    - utter_greet
* restaurant_search{"location": "raipur", "budget": "500", "cuisine": "north indian"}
    - slot{"budget": "500"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "raipur"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": 21.251703}
    - slot{"lon": 81.629684}
    - slot{"city_id": 11310}
    - slot{"cuisine_key": "50"}
    - slot{"api_response": "{\"1\":[\"Barbeque Nation\",\"Magneto Mall, Jevan Vihar, Shankar Nagar, Raipur\",\"1500\",\"4.6\"],\"2\":[\"Hotel Moon Darbar\",\"Mehbubiya Chowk, Gol Bazar, Moudhapara\",\"300\",\"4.3\"],\"3\":[\"Naivedya\",\"Jail Road, Raipur, Devendra Nagar, Raipur\",\"500\",\"4.2\"],\"4\":[\"Urban Grill\",\"Opposite Marine Drive, Telibandha, Civil Lines, Raipur\",\"700\",\"4.2\"],\"5\":[\"Yaaran Da Adda\",\"Opposite AIIMS Gate 5, Main Road, Tatibandh\",\"600\",\"4.2\"],\"6\":[\"Anna Punjabi\",\"Pachpedi Naka Chowk, Beside Nest, Mahaveer Nagar, Raipur\",\"600\",\"4.2\"],\"7\":[\"Girnar Restaurant\",\"Jaistambh Chowk, GE Road, Raipur (CG)\",\"500\",\"4.1\"],\"8\":[\"Vishvas Bhojanalaya\",\"Rathod Chowk, Ramsagar Pada, Jawahar Nagar, Raipur\",\"200\",\"4.1\"],\"9\":[\"Indian Coffee House\",\"Shyam Square Market, Pandri, Devendra Nagar Raipur\",\"500\",\"4.1\"],\"10\":[\"The Arabian Oasis\",\"Sixth Floor, Colors Mall, Pachpedi Naka, Mahaveer Nagar, Raipur\",\"800\",\"4.1\"]}"}
    - action_restaurant
    - slot{"location": "raipur"}
    - slot{"api_response": "{\"1\":[\"Barbeque Nation\",\"Magneto Mall, Jevan Vihar, Shankar Nagar, Raipur\",\"1500\",\"4.6\"],\"2\":[\"Hotel Moon Darbar\",\"Mehbubiya Chowk, Gol Bazar, Moudhapara\",\"300\",\"4.3\"],\"3\":[\"Naivedya\",\"Jail Road, Raipur, Devendra Nagar, Raipur\",\"500\",\"4.2\"],\"4\":[\"Urban Grill\",\"Opposite Marine Drive, Telibandha, Civil Lines, Raipur\",\"700\",\"4.2\"],\"5\":[\"Yaaran Da Adda\",\"Opposite AIIMS Gate 5, Main Road, Tatibandh\",\"600\",\"4.2\"],\"6\":[\"Anna Punjabi\",\"Pachpedi Naka Chowk, Beside Nest, Mahaveer Nagar, Raipur\",\"600\",\"4.2\"],\"7\":[\"Girnar Restaurant\",\"Jaistambh Chowk, GE Road, Raipur (CG)\",\"500\",\"4.1\"],\"8\":[\"Vishvas Bhojanalaya\",\"Rathod Chowk, Ramsagar Pada, Jawahar Nagar, Raipur\",\"200\",\"4.1\"],\"9\":[\"Indian Coffee House\",\"Shyam Square Market, Pandri, Devendra Nagar Raipur\",\"500\",\"4.1\"],\"10\":[\"The Arabian Oasis\",\"Sixth Floor, Colors Mall, Pachpedi Naka, Mahaveer Nagar, Raipur\",\"800\",\"4.1\"]}"}
    - slot{"budget": "500"}
    - slot{"cuisine": "north indian"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export



## Generated Story 7606754564755978893
* greet
    - utter_greet
* restaurant_search{"budget": "700", "location": "Warangal", "cuisine": "north indian"}
    - slot{"budget": "700"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Warangal"}
    - slot{"location": "warangal"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": 17.405465888889}
    - slot{"lon": 78.588814411111}
    - slot{"city_id": 6}
    - slot{"cuisine_key": "50"}
    - slot{"api_response": "{\"1\":[\"AB's - Absolute Barbecues\",\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1500\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"AB's - Absolute Barbecues\",\"8-2-618/10-11, 2nd Floor, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad\",\"1500\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"5\":[\"The Roastery Coffee House\",\"8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\",\"800\",\"4.8\"],\"6\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.8\"],\"7\":[\"Nimrah Cafe And Bakery\",\"Beside Mecca Masjid, Charminar Road, Charminar, Hyderabad\",\"100\",\"4.8\"],\"8\":[\"Exotica\",\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"1500\",\"4.7\"],\"9\":[\"Farzi Cafe\",\"1200, Road 59, Jubilee Hills, Hyderabad\",\"1800\",\"4.7\"],\"10\":[\"Sahib\u2019s Barbeque by Ohri\u2019s\",\"Ohris Cyber Grub, Plot 4/1 & 4/2, 64, Huda Techno Enclave, Mind Space Centre, Madhapur\",\"1400\",\"4.7\"]}"}
    - action_restaurant
    - slot{"location": "Warangal"}
    - slot{"api_response": "{\"1\":[\"AB's - Absolute Barbecues\",\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1500\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"AB's - Absolute Barbecues\",\"8-2-618/10-11, 2nd Floor, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad\",\"1500\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"5\":[\"The Roastery Coffee House\",\"8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\",\"800\",\"4.8\"],\"6\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.8\"],\"7\":[\"Nimrah Cafe And Bakery\",\"Beside Mecca Masjid, Charminar Road, Charminar, Hyderabad\",\"100\",\"4.8\"],\"8\":[\"Exotica\",\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"1500\",\"4.7\"],\"9\":[\"Farzi Cafe\",\"1200, Road 59, Jubilee Hills, Hyderabad\",\"1800\",\"4.7\"],\"10\":[\"Sahib\u2019s Barbeque by Ohri\u2019s\",\"Ohris Cyber Grub, Plot 4/1 & 4/2, 64, Huda Techno Enclave, Mind Space Centre, Madhapur\",\"1400\",\"4.7\"]}"}
    - slot{"budget": "700"}
    - slot{"cuisine": "north indian"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "ankit276@gmail.com"}
    - slot{"email": "ankit276@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Generated Story 7606754564755978894
* greet
    - utter_greet
* restaurant_search{"budget": "700", "location": "Warangal", "cuisine": "north indian"}
    - slot{"budget": "700"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Warangal"}
    - slot{"location": "warangal"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": 17.405465888889}
    - slot{"lon": 78.588814411111}
    - slot{"city_id": 6}
    - slot{"cuisine_key": "50"}
    - slot{"api_response": "{\"1\":[\"AB's - Absolute Barbecues\",\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1500\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"AB's - Absolute Barbecues\",\"8-2-618/10-11, 2nd Floor, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad\",\"1500\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"5\":[\"The Roastery Coffee House\",\"8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\",\"800\",\"4.8\"],\"6\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.8\"],\"7\":[\"Nimrah Cafe And Bakery\",\"Beside Mecca Masjid, Charminar Road, Charminar, Hyderabad\",\"100\",\"4.8\"],\"8\":[\"Exotica\",\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"1500\",\"4.7\"],\"9\":[\"Farzi Cafe\",\"1200, Road 59, Jubilee Hills, Hyderabad\",\"1800\",\"4.7\"],\"10\":[\"Sahib\u2019s Barbeque by Ohri\u2019s\",\"Ohris Cyber Grub, Plot 4/1 & 4/2, 64, Huda Techno Enclave, Mind Space Centre, Madhapur\",\"1400\",\"4.7\"]}"}
    - action_restaurant
    - slot{"location": "Warangal"}
    - slot{"api_response": "{\"1\":[\"AB's - Absolute Barbecues\",\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1500\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"AB's - Absolute Barbecues\",\"8-2-618/10-11, 2nd Floor, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad\",\"1500\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"5\":[\"The Roastery Coffee House\",\"8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\",\"800\",\"4.8\"],\"6\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.8\"],\"7\":[\"Nimrah Cafe And Bakery\",\"Beside Mecca Masjid, Charminar Road, Charminar, Hyderabad\",\"100\",\"4.8\"],\"8\":[\"Exotica\",\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"1500\",\"4.7\"],\"9\":[\"Farzi Cafe\",\"1200, Road 59, Jubilee Hills, Hyderabad\",\"1800\",\"4.7\"],\"10\":[\"Sahib\u2019s Barbeque by Ohri\u2019s\",\"Ohris Cyber Grub, Plot 4/1 & 4/2, 64, Huda Techno Enclave, Mind Space Centre, Madhapur\",\"1400\",\"4.7\"]}"}
    - slot{"budget": "700"}
    - slot{"cuisine": "north indian"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export


## Generated Story -5953351654077632332
* greet
    - utter_greet
* restaurant_search{"budget": "700", "cuisine": "mexican", "location": "pune"}
    - slot{"budget": "700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "pune"}
    - slot{"location": "pune"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": 18.520469}
    - slot{"lon": 73.85662}
    - slot{"city_id": 5}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Laa Unico\",\"Arihant Aura Building, Above Comet Stationery, Next to Sujay Garden, Commercial Complex, Near Laxmi Narayan Theatre, Mukundnagar, Swargate, Pune\",\"1100\",\"4.8\"],\"2\":[\"Chili's American Grill & Bar\",\"UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune\",\"1400\",\"4.8\"],\"3\":[\"Agent Jack's\",\"Ground Floor, Kapila Matrix, Koregaon Park Annexe, Mundhwa, Pune\",\"1300\",\"4.7\"],\"4\":[\"Cafe 1730\",\"21/1, Serene Bay, Lane 6, Off North Main Road, Koregaon Park, Pune\",\"1500\",\"4.6\"],\"5\":[\"Darshan\",\"759/60, Prabhat Road, Opposite Indian Bank, Deccan Gymkhana, Pune\",\"700\",\"4.6\"],\"6\":[\"Effingut Brewerkz\",\"End of Lane Number 6, Koregaon Park, Pune\",\"1700\",\"4.6\"],\"7\":[\"Baraza Bars & Bites\",\"Unit 10, Pubtown, Creaticity Mall, Shastri Nagar, Yerawada, Pune\",\"1400\",\"4.6\"],\"8\":[\"Hard Rock Cafe\",\"81/82, East Main Road, Koregaon Park Extension, Mundhwa, Pune\",\"2500\",\"4.6\"],\"9\":[\"The Urban Foundry\",\"B-3, Ground Floor, Cerebrum IT Park, Near Marigold Complex, Kalyani Nagar, Pune\",\"1500\",\"4.6\"],\"10\":[\"Agent Jack's\",\"West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune\",\"1300\",\"4.6\"]}"}
    - action_restaurant
    - slot{"location": "pune"}
    - slot{"api_response": "{\"1\":[\"Laa Unico\",\"Arihant Aura Building, Above Comet Stationery, Next to Sujay Garden, Commercial Complex, Near Laxmi Narayan Theatre, Mukundnagar, Swargate, Pune\",\"1100\",\"4.8\"],\"2\":[\"Chili's American Grill & Bar\",\"UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune\",\"1400\",\"4.8\"],\"3\":[\"Agent Jack's\",\"Ground Floor, Kapila Matrix, Koregaon Park Annexe, Mundhwa, Pune\",\"1300\",\"4.7\"],\"4\":[\"Cafe 1730\",\"21/1, Serene Bay, Lane 6, Off North Main Road, Koregaon Park, Pune\",\"1500\",\"4.6\"],\"5\":[\"Darshan\",\"759/60, Prabhat Road, Opposite Indian Bank, Deccan Gymkhana, Pune\",\"700\",\"4.6\"],\"6\":[\"Effingut Brewerkz\",\"End of Lane Number 6, Koregaon Park, Pune\",\"1700\",\"4.6\"],\"7\":[\"Baraza Bars & Bites\",\"Unit 10, Pubtown, Creaticity Mall, Shastri Nagar, Yerawada, Pune\",\"1400\",\"4.6\"],\"8\":[\"Hard Rock Cafe\",\"81/82, East Main Road, Koregaon Park Extension, Mundhwa, Pune\",\"2500\",\"4.6\"],\"9\":[\"The Urban Foundry\",\"B-3, Ground Floor, Cerebrum IT Park, Near Marigold Complex, Kalyani Nagar, Pune\",\"1500\",\"4.6\"],\"10\":[\"Agent Jack's\",\"West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune\",\"1300\",\"4.6\"]}"}
    - slot{"budget": "700"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export


## Generated Story 6103824392072038547
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "budget": "500", "location": "nashik"}
    - slot{"budget": "500"}
    - slot{"cuisine": "italian"}
    - slot{"location": "nashik"}
    - slot{"cuisine": "italian"}
    - slot{"lat": 20}
    - slot{"lon": 73.78}
    - slot{"city_id": 16}
    - slot{"cuisine_key": "55"}
    - slot{"api_response": "{\"1\":[\"Sula Vineyards\",\"Gat 36/2, Govardhan Village, Off Gangapur-Savargaon Road, Nashik, Maharashtra\",\"1500\",\"4.6\"],\"2\":[\"White X Sky Lounge\",\"3rd floor, 726 Ikon building, above Westside, Yeolekar Mala, off College road, Nashik\",\"1000\",\"4.4\"],\"3\":[\"The Foundry- Industrial Bar & Sport\",\"BLVD, 2nd Level, P-20, Trimbak Road, Satpur MIDC, Satpur, Nashik\",\"1000\",\"4.2\"],\"4\":[\"Little Italy\",\"36/2, Govardhan Village, Off Gangapur-Savargaon Road, Satpur, Nashik\",\"800\",\"4.1\"],\"5\":[\"12-TO-12\",\"Shop 10, Ramrajya Building 7, Samarth Nagar, Near Bhonsala bhawan, mahatma nagar road, next to samarth nagar bust stops and water tank, Nashik\",\"400\",\"4.0\"],\"6\":[\"Pick a Pizza\",\"Shop 6, Atreya Appartment, Near Water Tank, Parijat Nagar, Nashik\",\"300\",\"4.0\"],\"7\":[\"Charcoal Eats\",\"Shop 1, Roongta Castle Apartment, Wadala Road, Khode Nagar, Nashik\",\"500\",\"3.9\"],\"8\":[\"Domino's Pizza\",\"Shop 5, Ground Floor, Satvik Hotel, Nashik Pune Road, Near Purnima Bus Depot, College Road, Nashik\",\"700\",\"3.8\"],\"9\":[\"Urban Flavours\",\"Shop 6, 7, 8, Ramrajya-7, Samarth Nagar, Besides Water Tank, College Road, Nashik\",\"500\",\"3.8\"],\"10\":[\"Fannito Pizza\",\"Shop 6, Shreeji Krupa Apartmant, Opposite Nashik Cambridge School, Indiranagar, Pathardi Phata, Nashik\",\"250\",\"3.7\"]}"}
    - action_restaurant
    - slot{"location": "nashik"}
    - slot{"api_response": "{\"1\":[\"Sula Vineyards\",\"Gat 36/2, Govardhan Village, Off Gangapur-Savargaon Road, Nashik, Maharashtra\",\"1500\",\"4.6\"],\"2\":[\"White X Sky Lounge\",\"3rd floor, 726 Ikon building, above Westside, Yeolekar Mala, off College road, Nashik\",\"1000\",\"4.4\"],\"3\":[\"The Foundry- Industrial Bar & Sport\",\"BLVD, 2nd Level, P-20, Trimbak Road, Satpur MIDC, Satpur, Nashik\",\"1000\",\"4.2\"],\"4\":[\"Little Italy\",\"36/2, Govardhan Village, Off Gangapur-Savargaon Road, Satpur, Nashik\",\"800\",\"4.1\"],\"5\":[\"12-TO-12\",\"Shop 10, Ramrajya Building 7, Samarth Nagar, Near Bhonsala bhawan, mahatma nagar road, next to samarth nagar bust stops and water tank, Nashik\",\"400\",\"4.0\"],\"6\":[\"Pick a Pizza\",\"Shop 6, Atreya Appartment, Near Water Tank, Parijat Nagar, Nashik\",\"300\",\"4.0\"],\"7\":[\"Charcoal Eats\",\"Shop 1, Roongta Castle Apartment, Wadala Road, Khode Nagar, Nashik\",\"500\",\"3.9\"],\"8\":[\"Domino's Pizza\",\"Shop 5, Ground Floor, Satvik Hotel, Nashik Pune Road, Near Purnima Bus Depot, College Road, Nashik\",\"700\",\"3.8\"],\"9\":[\"Urban Flavours\",\"Shop 6, 7, 8, Ramrajya-7, Samarth Nagar, Besides Water Tank, College Road, Nashik\",\"500\",\"3.8\"],\"10\":[\"Fannito Pizza\",\"Shop 6, Shreeji Krupa Apartmant, Opposite Nashik Cambridge School, Indiranagar, Pathardi Phata, Nashik\",\"250\",\"3.7\"]}"}
    - slot{"budget": "500"}
    - slot{"cuisine": "italian"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test123@xyz.com"}
    - slot{"email": "test123@xyz.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Generated Story 6103824392072038547
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "budget": "500", "location": "nashik"}
    - slot{"budget": "500"}
    - slot{"cuisine": "italian"}
    - slot{"location": "nashik"}
    - slot{"cuisine": "italian"}
    - slot{"lat": 20}
    - slot{"lon": 73.78}
    - slot{"city_id": 16}
    - slot{"cuisine_key": "55"}
    - slot{"api_response": "{\"1\":[\"Sula Vineyards\",\"Gat 36/2, Govardhan Village, Off Gangapur-Savargaon Road, Nashik, Maharashtra\",\"1500\",\"4.6\"],\"2\":[\"White X Sky Lounge\",\"3rd floor, 726 Ikon building, above Westside, Yeolekar Mala, off College road, Nashik\",\"1000\",\"4.4\"],\"3\":[\"The Foundry- Industrial Bar & Sport\",\"BLVD, 2nd Level, P-20, Trimbak Road, Satpur MIDC, Satpur, Nashik\",\"1000\",\"4.2\"],\"4\":[\"Little Italy\",\"36/2, Govardhan Village, Off Gangapur-Savargaon Road, Satpur, Nashik\",\"800\",\"4.1\"],\"5\":[\"12-TO-12\",\"Shop 10, Ramrajya Building 7, Samarth Nagar, Near Bhonsala bhawan, mahatma nagar road, next to samarth nagar bust stops and water tank, Nashik\",\"400\",\"4.0\"],\"6\":[\"Pick a Pizza\",\"Shop 6, Atreya Appartment, Near Water Tank, Parijat Nagar, Nashik\",\"300\",\"4.0\"],\"7\":[\"Charcoal Eats\",\"Shop 1, Roongta Castle Apartment, Wadala Road, Khode Nagar, Nashik\",\"500\",\"3.9\"],\"8\":[\"Domino's Pizza\",\"Shop 5, Ground Floor, Satvik Hotel, Nashik Pune Road, Near Purnima Bus Depot, College Road, Nashik\",\"700\",\"3.8\"],\"9\":[\"Urban Flavours\",\"Shop 6, 7, 8, Ramrajya-7, Samarth Nagar, Besides Water Tank, College Road, Nashik\",\"500\",\"3.8\"],\"10\":[\"Fannito Pizza\",\"Shop 6, Shreeji Krupa Apartmant, Opposite Nashik Cambridge School, Indiranagar, Pathardi Phata, Nashik\",\"250\",\"3.7\"]}"}
    - action_restaurant
    - slot{"location": "nashik"}
    - slot{"api_response": "{\"1\":[\"Sula Vineyards\",\"Gat 36/2, Govardhan Village, Off Gangapur-Savargaon Road, Nashik, Maharashtra\",\"1500\",\"4.6\"],\"2\":[\"White X Sky Lounge\",\"3rd floor, 726 Ikon building, above Westside, Yeolekar Mala, off College road, Nashik\",\"1000\",\"4.4\"],\"3\":[\"The Foundry- Industrial Bar & Sport\",\"BLVD, 2nd Level, P-20, Trimbak Road, Satpur MIDC, Satpur, Nashik\",\"1000\",\"4.2\"],\"4\":[\"Little Italy\",\"36/2, Govardhan Village, Off Gangapur-Savargaon Road, Satpur, Nashik\",\"800\",\"4.1\"],\"5\":[\"12-TO-12\",\"Shop 10, Ramrajya Building 7, Samarth Nagar, Near Bhonsala bhawan, mahatma nagar road, next to samarth nagar bust stops and water tank, Nashik\",\"400\",\"4.0\"],\"6\":[\"Pick a Pizza\",\"Shop 6, Atreya Appartment, Near Water Tank, Parijat Nagar, Nashik\",\"300\",\"4.0\"],\"7\":[\"Charcoal Eats\",\"Shop 1, Roongta Castle Apartment, Wadala Road, Khode Nagar, Nashik\",\"500\",\"3.9\"],\"8\":[\"Domino's Pizza\",\"Shop 5, Ground Floor, Satvik Hotel, Nashik Pune Road, Near Purnima Bus Depot, College Road, Nashik\",\"700\",\"3.8\"],\"9\":[\"Urban Flavours\",\"Shop 6, 7, 8, Ramrajya-7, Samarth Nagar, Besides Water Tank, College Road, Nashik\",\"500\",\"3.8\"],\"10\":[\"Fannito Pizza\",\"Shop 6, Shreeji Krupa Apartmant, Opposite Nashik Cambridge School, Indiranagar, Pathardi Phata, Nashik\",\"250\",\"3.7\"]}"}
    - slot{"budget": "500"}
    - slot{"cuisine": "italian"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Generated Story -1224972267383338778
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "pune"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "pune"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - slot{"location": "pune"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": 18.520469}
    - slot{"lon": 73.85662}
    - slot{"city_id": 5}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Laa Unico\",\"Arihant Aura Building, Above Comet Stationery, Next to Sujay Garden, Commercial Complex, Near Laxmi Narayan Theatre, Mukundnagar, Swargate, Pune\",\"1100\",\"4.8\"],\"2\":[\"Chili's American Grill & Bar\",\"UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune\",\"1400\",\"4.8\"],\"3\":[\"Agent Jack's\",\"Ground Floor, Kapila Matrix, Koregaon Park Annexe, Mundhwa, Pune\",\"1300\",\"4.7\"],\"4\":[\"Cafe 1730\",\"21/1, Serene Bay, Lane 6, Off North Main Road, Koregaon Park, Pune\",\"1500\",\"4.6\"],\"5\":[\"Darshan\",\"759/60, Prabhat Road, Opposite Indian Bank, Deccan Gymkhana, Pune\",\"700\",\"4.6\"],\"6\":[\"Effingut Brewerkz\",\"End of Lane Number 6, Koregaon Park, Pune\",\"1700\",\"4.6\"],\"7\":[\"Baraza Bars & Bites\",\"Unit 10, Pubtown, Creaticity Mall, Shastri Nagar, Yerawada, Pune\",\"1400\",\"4.6\"],\"8\":[\"Hard Rock Cafe\",\"81/82, East Main Road, Koregaon Park Extension, Mundhwa, Pune\",\"2500\",\"4.6\"],\"9\":[\"The Urban Foundry\",\"B-3, Ground Floor, Cerebrum IT Park, Near Marigold Complex, Kalyani Nagar, Pune\",\"1500\",\"4.6\"],\"10\":[\"Agent Jack's\",\"West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune\",\"1300\",\"4.6\"]}"}
    - action_restaurant
    - slot{"location": "pune"}
    - slot{"api_response": "{\"1\":[\"Laa Unico\",\"Arihant Aura Building, Above Comet Stationery, Next to Sujay Garden, Commercial Complex, Near Laxmi Narayan Theatre, Mukundnagar, Swargate, Pune\",\"1100\",\"4.8\"],\"2\":[\"Chili's American Grill & Bar\",\"UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune\",\"1400\",\"4.8\"],\"3\":[\"Agent Jack's\",\"Ground Floor, Kapila Matrix, Koregaon Park Annexe, Mundhwa, Pune\",\"1300\",\"4.7\"],\"4\":[\"Cafe 1730\",\"21/1, Serene Bay, Lane 6, Off North Main Road, Koregaon Park, Pune\",\"1500\",\"4.6\"],\"5\":[\"Darshan\",\"759/60, Prabhat Road, Opposite Indian Bank, Deccan Gymkhana, Pune\",\"700\",\"4.6\"],\"6\":[\"Effingut Brewerkz\",\"End of Lane Number 6, Koregaon Park, Pune\",\"1700\",\"4.6\"],\"7\":[\"Baraza Bars & Bites\",\"Unit 10, Pubtown, Creaticity Mall, Shastri Nagar, Yerawada, Pune\",\"1400\",\"4.6\"],\"8\":[\"Hard Rock Cafe\",\"81/82, East Main Road, Koregaon Park Extension, Mundhwa, Pune\",\"2500\",\"4.6\"],\"9\":[\"The Urban Foundry\",\"B-3, Ground Floor, Cerebrum IT Park, Near Marigold Complex, Kalyani Nagar, Pune\",\"1500\",\"4.6\"],\"10\":[\"Agent Jack's\",\"West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune\",\"1300\",\"4.6\"]}"}
    - slot{"budget": "700"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export


## Generated Story -6015144187504342826
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "budget": "700"}
    - slot{"budget": "700"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": 22.572646}
    - slot{"lon": 88.363895}
    - slot{"city_id": 2}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Chili's Grill & Bar\",\"Acropolis Mall, 1858, Rajdanga Main Road, Kasba, Kolkata\",\"1700\",\"4.8\"],\"2\":[\"Auda Cafe & Club\",\"2,12, Hungerford Street, Theatre Road, Kolkata\",\"1000\",\"4.8\"],\"3\":[\"My Big Fat Belly\",\"22, Sarat Bose Road, Sreepally, Bhawanipur, Kolkata\",\"1200\",\"4.7\"],\"4\":[\"Chili's Grill & Bar\",\"375, 2nd Floor, South City Mall, Prince Anwar Shah Road, Kolkata\",\"1700\",\"4.7\"],\"5\":[\"Chili's Grill & Bar\",\"4th Floor, Quest Mall, 33, Syed Ali Amir Avenue, Ballygunge, Kolkata\",\"1700\",\"4.7\"],\"6\":[\"Hakuna Matata\",\"Ground Floor, 12D,   Park Street Area, Park Street Area, Kolkata\",\"800\",\"4.6\"],\"7\":[\"The GRID\",\"Haute Street Corporate Park, 86A, Topsia Road (South), Kolkata\",\"2000\",\"4.6\"],\"8\":[\"Sly Fox Gastro Club\",\"Globsyn Crystals, Podium level, Block EP Sector V, Salt Lake City\",\"1250\",\"4.5\"],\"9\":[\"BJs Sports Restrau Cum Lounge\",\"104/1A, Sarat Bose Road, Near 85 Lansdowne, Hazra, Kolkata\",\"750\",\"4.5\"],\"10\":[\"What's Up\",\"122A, Southern Avenue, Kolkata\",\"1000\",\"4.4\"]}"}
    - action_restaurant
    - slot{"location": "kolkata"}
    - slot{"api_response": "{\"1\":[\"Chili's Grill & Bar\",\"Acropolis Mall, 1858, Rajdanga Main Road, Kasba, Kolkata\",\"1700\",\"4.8\"],\"2\":[\"Auda Cafe & Club\",\"2,12, Hungerford Street, Theatre Road, Kolkata\",\"1000\",\"4.8\"],\"3\":[\"My Big Fat Belly\",\"22, Sarat Bose Road, Sreepally, Bhawanipur, Kolkata\",\"1200\",\"4.7\"],\"4\":[\"Chili's Grill & Bar\",\"375, 2nd Floor, South City Mall, Prince Anwar Shah Road, Kolkata\",\"1700\",\"4.7\"],\"5\":[\"Chili's Grill & Bar\",\"4th Floor, Quest Mall, 33, Syed Ali Amir Avenue, Ballygunge, Kolkata\",\"1700\",\"4.7\"],\"6\":[\"Hakuna Matata\",\"Ground Floor, 12D,   Park Street Area, Park Street Area, Kolkata\",\"800\",\"4.6\"],\"7\":[\"The GRID\",\"Haute Street Corporate Park, 86A, Topsia Road (South), Kolkata\",\"2000\",\"4.6\"],\"8\":[\"Sly Fox Gastro Club\",\"Globsyn Crystals, Podium level, Block EP Sector V, Salt Lake City\",\"1250\",\"4.5\"],\"9\":[\"BJs Sports Restrau Cum Lounge\",\"104/1A, Sarat Bose Road, Near 85 Lansdowne, Hazra, Kolkata\",\"750\",\"4.5\"],\"10\":[\"What's Up\",\"122A, Southern Avenue, Kolkata\",\"1000\",\"4.4\"]}"}
    - slot{"budget": "700"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test123@gmail.com"}
    - slot{"email": "test123@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Generated Story -5036683267264705898
* deny
    - utter_goodbye
    - action_goodbye
* greet
    - utter_greet
* restaurant_search{"location": "bhopal", "budget": "700"}
    - slot{"budget": "700"}
    - slot{"location": "bhopal"}
    - utter_ask_cuisine
* cuisine{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"lat": 23.25}
    - slot{"lon": 77.4167}
    - slot{"city_id": 26}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test123@sdf.com"}
    - slot{"email": "test123@sdf.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Generated Story 5668497626520803220
* greet
    - utter_greet
* restaurant_search{"location": "kolkata", "cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "kolkata"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - slot{"location": "kolkata"}
    - slot{"cuisine": "south indian"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@yml.com"}
    - slot{"email": "test@yml.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Generated Story -7542363699331070789
* greet
    - utter_greet
* restaurant_search{"budget": "600", "cuisine": "north indian"}
    - slot{"budget": "600"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* location{"location": "surat"}
    - slot{"location": "surat"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": 21.17}
    - slot{"lon": 72.83}
    - slot{"city_id": 38}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - action_goodbye
    - export

## Generated Story 1748430531261910883
* greet
    - utter_greet
* restaurant_search{"budget": "700", "location": "amritsar"}
    - slot{"budget": "700"}
    - slot{"location": "amritsar"}
    - utter_ask_cuisine
* cuisine{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"lat": 31.64}
    - slot{"lon": 74.86}
    - slot{"city_id": 22}
    - slot{"cuisine_key": "85"}
    - slot{"api_response": "{\"1\":[\"EatAsia Food\",\"C Block Market, Ranjit Avenue, Amritsar\",\"700\",\"4.0\"],\"2\":[\"Shudh Restaurant\",\"Opposite Gurudwara Saragarhi, Near Dharm Singh Market Chowk, Fuwara, Town Hall, Amritsar\",\"600\",\"4.0\"],\"3\":[\"Chaupati Restaurant\",\"Ground Floor, 9-10, Nehru Shopping Complex, Lawrence Road, Amritsar\",\"600\",\"3.7\"],\"4\":[\"Lovely Champ\",\"100 Feet road, Amritsar\",\"500\",\"3.6\"],\"5\":[\"Grab N Go!\",\"C-Block Market, Near Bansal, Ranjit Avenue, Amritsar\",\"250\",\"3.4\"],\"6\":[\"Haveli\",\"G.T. Road, Amritsar - Jalandhar Highway, Amritsar\",\"450\",\"3.4\"],\"7\":[\"DOMO\",\"Lawrence Plaza Market, Opposite Selection Point, Near Jayson Fashion Fort, Lawrence Road, Amritsar\",\"150\",\"3.3\"],\"8\":[\"Just Mughlai\",\"63, A-Block Market, Ranjit Avenue, Amritsar\",\"300\",\"3.3\"],\"9\":[\"Radhe Radhe\",\"R S Tower, Hall Bazar, Town Hall, Amritsar\",\"600\",\"3.2\"],\"10\":[\"Hotel Raj Darbar\",\"Near Golden Temple,  Opposite Guru Ram Das Sarai, Town Hall, Amritsar\",\"500\",\"3.1\"]}"}
    - action_restaurant
    - slot{"location": "amritsar"}
    - slot{"api_response": "{\"1\":[\"EatAsia Food\",\"C Block Market, Ranjit Avenue, Amritsar\",\"700\",\"4.0\"],\"2\":[\"Shudh Restaurant\",\"Opposite Gurudwara Saragarhi, Near Dharm Singh Market Chowk, Fuwara, Town Hall, Amritsar\",\"600\",\"4.0\"],\"3\":[\"Chaupati Restaurant\",\"Ground Floor, 9-10, Nehru Shopping Complex, Lawrence Road, Amritsar\",\"600\",\"3.7\"],\"4\":[\"Lovely Champ\",\"100 Feet road, Amritsar\",\"500\",\"3.6\"],\"5\":[\"Grab N Go!\",\"C-Block Market, Near Bansal, Ranjit Avenue, Amritsar\",\"250\",\"3.4\"],\"6\":[\"Haveli\",\"G.T. Road, Amritsar - Jalandhar Highway, Amritsar\",\"450\",\"3.4\"],\"7\":[\"DOMO\",\"Lawrence Plaza Market, Opposite Selection Point, Near Jayson Fashion Fort, Lawrence Road, Amritsar\",\"150\",\"3.3\"],\"8\":[\"Just Mughlai\",\"63, A-Block Market, Ranjit Avenue, Amritsar\",\"300\",\"3.3\"],\"9\":[\"Radhe Radhe\",\"R S Tower, Hall Bazar, Town Hall, Amritsar\",\"600\",\"3.2\"],\"10\":[\"Hotel Raj Darbar\",\"Near Golden Temple,  Opposite Guru Ram Das Sarai, Town Hall, Amritsar\",\"500\",\"3.1\"]}"}
    - slot{"budget": "700"}
    - slot{"cuisine": "south indian"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "ankiy234@gmail.com"}
    - slot{"email": "ankiy234@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Generated Story -1271163316189610931
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "american"}
    - slot{"lat": 12.971606}
    - slot{"lon": 77.594376}
    - slot{"city_id": 4}
    - slot{"cuisine_key": "1"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Belgian Waffle Factory \",\"65, Markham Road, Ashok Nagar, Brigade Road, Bangalore\",\"250\",\"4.9\"],\"4\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"5\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"6\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"7\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"8\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"9\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"],\"10\":[\"The Globe Grub\",\"2nd Floor, Soul Space Paradigm,\nLandmark- Next to Innovative Multiplex, Above Bata Showroom, Outer Ring Road Marathahalli, Bangalore\",\"1300\",\"4.8\"]}"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Belgian Waffle Factory \",\"65, Markham Road, Ashok Nagar, Brigade Road, Bangalore\",\"250\",\"4.9\"],\"4\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"5\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"6\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"7\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"8\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"9\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"],\"10\":[\"The Globe Grub\",\"2nd Floor, Soul Space Paradigm,\nLandmark- Next to Innovative Multiplex, Above Bata Showroom, Outer Ring Road Marathahalli, Bangalore\",\"1300\",\"4.8\"]}"}
    - slot{"budget": "700"}
    - slot{"cuisine": "american"}
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - action_goodbye
    - export


## Generated Story -3332314660619586509
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* location{"location": "patna"}
    - slot{"location": "patna"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": 25.611}
    - slot{"lon": 85.144}
    - slot{"city_id": 40}
    - action_restaurant
    - slot{"location": "patna"}
    - slot{"cuisine": null}
* cuisine{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"lat": 25.611}
    - slot{"lon": 85.144}
    - slot{"city_id": 40}
    - slot{"cuisine_key": "85"}
    - slot{"api_response": "{\"1\":[\"Moti Mahal Delux \",\"Opposite Hotel Samrat International, Fraser Road, Patna\",\"800\",\"4.5\"],\"2\":[\"Basant Vihar\",\"1st Floor, Maurya Lok Complex, Fraser Road Area, Patna\",\"600\",\"4.4\"],\"3\":[\"Bansi Vihar Restaurant\",\"New Market Beside Buddha Park, Fraser Road Area, Patna\",\"400\",\"4.3\"],\"4\":[\"Spice Court - Hotel Maurya\",\"Hotel Maurya, South Gandhi Maidan, Lodipur, Patna\",\"1600\",\"4.3\"],\"5\":[\"Haldiram\",\"Rajeswar Commercial Complex, Main Road, Kankarbagh, Patna\",\"500\",\"4.2\"],\"6\":[\"Moti Mahal Delux\",\"Opposite Guinea Motors, Boring Canal Road, Kidwaipuri, Patna\",\"500\",\"3.9\"],\"7\":[\"Bell Pepper Restaurant - Hotel Windsor\",\"Hotel Windsor, Exhibition Road, Fraser Road Area, Patna\",\"1000\",\"3.9\"],\"8\":[\"Patna Rasoi\",\"Marwari Awas Griha Campus, Near Bank of India, Fraser Road Area, Patna\",\"550\",\"3.8\"],\"9\":[\"Raj Rasoi\",\"Twin Tower Hathwa, South Gandhi Maidan, Lodipur, Patna\",\"1200\",\"3.8\"],\"10\":[\"Haldiram\",\"Shyam Sundar Complex, Jagdeo Path, Bailey Road, Khajpura, Patna\",\"500\",\"3.7\"]}"}
    - action_restaurant
    - slot{"location": "patna"}
    - slot{"api_response": "{\"1\":[\"Moti Mahal Delux \",\"Opposite Hotel Samrat International, Fraser Road, Patna\",\"800\",\"4.5\"],\"2\":[\"Basant Vihar\",\"1st Floor, Maurya Lok Complex, Fraser Road Area, Patna\",\"600\",\"4.4\"],\"3\":[\"Bansi Vihar Restaurant\",\"New Market Beside Buddha Park, Fraser Road Area, Patna\",\"400\",\"4.3\"],\"4\":[\"Spice Court - Hotel Maurya\",\"Hotel Maurya, South Gandhi Maidan, Lodipur, Patna\",\"1600\",\"4.3\"],\"5\":[\"Haldiram\",\"Rajeswar Commercial Complex, Main Road, Kankarbagh, Patna\",\"500\",\"4.2\"],\"6\":[\"Moti Mahal Delux\",\"Opposite Guinea Motors, Boring Canal Road, Kidwaipuri, Patna\",\"500\",\"3.9\"],\"7\":[\"Bell Pepper Restaurant - Hotel Windsor\",\"Hotel Windsor, Exhibition Road, Fraser Road Area, Patna\",\"1000\",\"3.9\"],\"8\":[\"Patna Rasoi\",\"Marwari Awas Griha Campus, Near Bank of India, Fraser Road Area, Patna\",\"550\",\"3.8\"],\"9\":[\"Raj Rasoi\",\"Twin Tower Hathwa, South Gandhi Maidan, Lodipur, Patna\",\"1200\",\"3.8\"],\"10\":[\"Haldiram\",\"Shyam Sundar Complex, Jagdeo Path, Bailey Road, Khajpura, Patna\",\"500\",\"3.7\"]}"}
    - slot{"budget": "300"}
    - slot{"cuisine": "south indian"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export


## Generated Story 8349949859565899116
* greet
    - utter_greet
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - utter_ask_location
* location{"location": "Durg-BhilaiNagar"}
    - slot{"location": "Durg-BhilaiNagar"}
    - utter_ask_cuisine
* cuisine{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"location": "durg-bhilainagar"}
    - slot{"cuisine": "italian"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - action_goodbye
    - export

## greet story
* greet
    - utter_greet

## Default: Verfied Out of context message
* default
    - utter_default
* greet
    - utter_greet
    - export

## Story Default: Verified
* default
    - utter_default
    - export

## goodbye
* goodbye
    - action_goodbye
    - utter_goodbye

## Story location: Verified
* location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - export

## Story cuisine: Verfied
* cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - export

## Story budget: Verified
* budget{"budget": "1200"}
    - slot{"budget": "1200"}
    - action_restaurant
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": "1200"}
    - export

## restaurant search
* restaurant_search
    - action_restaurant

## Story -verified Happy path sending email
* greet
    - utter_greet
* restaurant_search{"location": "hyd"}
    - slot{"location": "hyd"}
    - slot{"location": "hyderabad"}
    - action_restaurant
    - slot{"location": "hyderabad"}
* cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"cuisine": "chinese"}
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"lat": 17.366}
    - slot{"lon": 78.476}
    - slot{"city_id": 6}
    - slot{"cuisine_key": "25"}
    - slot{"api_response": "{\"1\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.8\"],\"5\":[\"Exotica\",\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"1500\",\"4.7\"],\"6\":[\"Mekong - Marigold Hotel\",\"Green Lands, Begumpet, Hyderabad\",\"2500\",\"4.7\"],\"7\":[\"The Fisherman's Wharf\",\"304, Puppalaguda, Financial District,ISB - Outer Ring Road, Gachibowli, Hyderabad\",\"1500\",\"4.6\"],\"8\":[\"Barbeque Nation\",\"6-3-249/5/1, 1st Floor, ANR Centre, Road 1, Banjara Hills, Hyderabad\",\"1600\",\"4.6\"],\"9\":[\"Prost Brew Pub\",\"882/A Road No 45, Jubilee Hills, Hyderabad\",\"2200\",\"4.6\"],\"10\":[\"SodaBottleOpenerWala\",\"Unit 4, Ground Floor, Niharika Jubilee One, Road 1, Jubilee Hills, Hyderabad\",\"1400\",\"4.6\"]}"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - slot{"api_response": "{\"1\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.8\"],\"5\":[\"Exotica\",\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"1500\",\"4.7\"],\"6\":[\"Mekong - Marigold Hotel\",\"Green Lands, Begumpet, Hyderabad\",\"2500\",\"4.7\"],\"7\":[\"The Fisherman's Wharf\",\"304, Puppalaguda, Financial District,ISB - Outer Ring Road, Gachibowli, Hyderabad\",\"1500\",\"4.6\"],\"8\":[\"Barbeque Nation\",\"6-3-249/5/1, 1st Floor, ANR Centre, Road 1, Banjara Hills, Hyderabad\",\"1600\",\"4.6\"],\"9\":[\"Prost Brew Pub\",\"882/A Road No 45, Jubilee Hills, Hyderabad\",\"2200\",\"4.6\"],\"10\":[\"SodaBottleOpenerWala\",\"Unit 4, Ground Floor, Niharika Jubilee One, Road 1, Jubilee Hills, Hyderabad\",\"1400\",\"4.6\"]}"}
    - slot{"budget": "500"}
    - slot{"cuisine": "chinese"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "abcd@gmail.com"}
    - slot{"email": "abcd@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
* goodbye
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Story verified invalid cuisine correction mail sent
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "erode"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "erode"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "1200"}
    - slot{"budget": "1200"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - action_restaurant
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - slot{"budget": "1200"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "abcd@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - export
* goodbye
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

    
## Story VERIFIED Invalid Cuisine no mail
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "erode"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "erode"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "1200"}
    - slot{"budget": "1200"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - action_restaurant
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - slot{"budget": "1200"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
* goodbye
    - export

## Story -VERIFIED invalid location mail sent
* restaurant_search{"location": "raebareli"}
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"location": null}
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_restaurant
    - slot{"location": "hyderabad"}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - slot{"cuisine": "mexican"}
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": 17.366}
    - slot{"lon": 78.476}
    - slot{"city_id": 6}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"2\":[\"The Roastery Coffee House\",\"8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\",\"800\",\"4.8\"],\"3\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.8\"],\"4\":[\"Churrolto\",\"Ground Floor, Shop 3, Opposite IndusInd Bank, Madhapur Main Road, Madhapur, Hyderabad\",\"1200\",\"4.8\"],\"5\":[\"Coffee Cup\",\"E 89, 1rst floor, Above Canara Bank, Sainikpuri, Secunderabad\",\"800\",\"4.7\"],\"6\":[\"B-Dubs\",\"Plot 806, Axis Tower, Road Number 36, Jubilee Hills, Hyderabad\",\"1600\",\"4.7\"],\"7\":[\"Hard Rock Cafe\",\"Ground Floor, GVK One, Road 1, Banjara Hills, Hyderabad\",\"2000\",\"4.7\"],\"8\":[\"B-Dubs\",\"Plot 189 to 198, Survey 50, Gachibowli Village, Gachibowli, Hyderabad\",\"1600\",\"4.7\"],\"9\":[\"L\u00e9 Vantage Cafe Bar\",\"Plot 197/A & 197, Road 13, Jubilee Hills, Hyderabad\",\"1000\",\"4.6\"],\"10\":[\"Ciclo Cafe\",\"801, Road 36, Jubilee Hills, Hyderabad\",\"2100\",\"4.6\"]}"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - slot{"api_response": "{\"1\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"2\":[\"The Roastery Coffee House\",\"8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\",\"800\",\"4.8\"],\"3\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.8\"],\"4\":[\"Churrolto\",\"Ground Floor, Shop 3, Opposite IndusInd Bank, Madhapur Main Road, Madhapur, Hyderabad\",\"1200\",\"4.8\"],\"5\":[\"Coffee Cup\",\"E 89, 1rst floor, Above Canara Bank, Sainikpuri, Secunderabad\",\"800\",\"4.7\"],\"6\":[\"B-Dubs\",\"Plot 806, Axis Tower, Road Number 36, Jubilee Hills, Hyderabad\",\"1600\",\"4.7\"],\"7\":[\"Hard Rock Cafe\",\"Ground Floor, GVK One, Road 1, Banjara Hills, Hyderabad\",\"2000\",\"4.7\"],\"8\":[\"B-Dubs\",\"Plot 189 to 198, Survey 50, Gachibowli Village, Gachibowli, Hyderabad\",\"1600\",\"4.7\"],\"9\":[\"L\u00e9 Vantage Cafe Bar\",\"Plot 197/A & 197, Road 13, Jubilee Hills, Hyderabad\",\"1000\",\"4.6\"],\"10\":[\"Ciclo Cafe\",\"801, Road 36, Jubilee Hills, Hyderabad\",\"2100\",\"4.6\"]}"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* default
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Story VERIFIED Invalid location mail not sent
* restaurant_search{"cuisine": "north indian", "location": "raebareli"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "1500"}
    - slot{"budget": "1500"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": 12.971606}
    - slot{"lon": 77.594376}
    - slot{"city_id": 4}
    - slot{"cuisine_key": "50"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Punjab Grill\",\"26/1, Dr. Rajkumar Road, In Brigade Gateway Campus, Malleshwaram ,Bangalore\",\"2000\",\"4.9\"],\"4\":[\"AB's - Absolute Barbecues\",\"2nd Floor,I20-A2, EPIP Zone, Near Vydehi Hospital Whitefield, Bangalore\",\"1400\",\"4.9\"],\"5\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"6\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"7\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"8\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"9\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"10\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"]}"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Punjab Grill\",\"26/1, Dr. Rajkumar Road, In Brigade Gateway Campus, Malleshwaram ,Bangalore\",\"2000\",\"4.9\"],\"4\":[\"AB's - Absolute Barbecues\",\"2nd Floor,I20-A2, EPIP Zone, Near Vydehi Hospital Whitefield, Bangalore\",\"1400\",\"4.9\"],\"5\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"6\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"7\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"8\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"9\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"10\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"]}"}
    - slot{"budget": "1500"}
    - slot{"cuisine": "north indian"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Generated Story 5048231483003727086
* greet
    - utter_greet
* default
    - utter_default
* restaurant_search
    - action_restaurant
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
* location{"location": "raebareli"}
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"location": null}
* location{"location": "bnglr"}
    - slot{"location": "bnglr"}
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"location": "bangalore"}
* cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"cuisine": "chinese"}
* budget{"budget": "1200"}
    - slot{"budget": "1200"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"lat": 12.971606}
    - slot{"lon": 77.594376}
    - slot{"city_id": 4}
    - slot{"cuisine_key": "25"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"4\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"5\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"6\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"7\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"8\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"],\"9\":[\"The Globe Grub\",\"2nd Floor, Soul Space Paradigm,\nLandmark- Next to Innovative Multiplex, Above Bata Showroom, Outer Ring Road Marathahalli, Bangalore\",\"1300\",\"4.8\"],\"10\":[\"AB's - Absolute Barbecues\",\"100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore\",\"1400\",\"4.8\"]}"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"4\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"5\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"6\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"7\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"8\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"],\"9\":[\"The Globe Grub\",\"2nd Floor, Soul Space Paradigm,\nLandmark- Next to Innovative Multiplex, Above Bata Showroom, Outer Ring Road Marathahalli, Bangalore\",\"1300\",\"4.8\"],\"10\":[\"AB's - Absolute Barbecues\",\"100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore\",\"1400\",\"4.8\"]}"}
    - slot{"budget": "1200"}
    - slot{"cuisine": "chinese"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* default{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - export

## Story -VERIFIED All use cases with EMAIL response filtering
* greet
    - utter_greet
* default
    - utter_default
* restaurant_search
    - action_restaurant
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
* location{"location": "raebareli"}
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"location": null}
* location{"location": "bnglr"}
    - slot{"location": "bnglr"}
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"location": "bangalore"}
* cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"cuisine": "chinese"}
* budget{"budget": "1000"}
    - slot{"budget": "1000"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"lat": 12.971606}
    - slot{"lon": 77.594376}
    - slot{"city_id": 4}
    - slot{"cuisine_key": "25"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"4\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"5\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"6\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"7\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"8\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"],\"9\":[\"The Globe Grub\",\"2nd Floor, Soul Space Paradigm,\nLandmark- Next to Innovative Multiplex, Above Bata Showroom, Outer Ring Road Marathahalli, Bangalore\",\"1300\",\"4.8\"],\"10\":[\"AB's - Absolute Barbecues\",\"100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore\",\"1400\",\"4.8\"]}"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"4\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"5\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"6\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"7\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"8\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"],\"9\":[\"The Globe Grub\",\"2nd Floor, Soul Space Paradigm,\nLandmark- Next to Innovative Multiplex, Above Bata Showroom, Outer Ring Road Marathahalli, Bangalore\",\"1300\",\"4.8\"],\"10\":[\"AB's - Absolute Barbecues\",\"100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore\",\"1400\",\"4.8\"]}"}
    - slot{"budget": "1000"}
    - slot{"cuisine": "chinese"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "abcd@gmail.com"}
    - slot{"email": "abcd@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - export