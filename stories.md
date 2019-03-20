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
    - export

