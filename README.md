Social network for bored people

Will this take traction?
- 

doubts: 
- too generic activities suggested that are not effective
- there are niche sites to help people waste time on: twitch, facebook, medium, youtube etc
- this is specifically for the community of bored people
- this is more like the google for bored people
    - people who just want random information
    
        recommendation based on other people like
            might want to recommend something not related people like too  much
            
            this is 

Overarching ideas:
(1) Bored people who list bored activities and get recommended activities by people who have similar
bored activities
(2) activities have suggested action plans 
(3) 

write cause for boredom (give a whole list of suggestions)
get a suggested activity
do it and report effectiveness, help other bored people who can rank you


Need to group activities together... how? show similar activities and prompt user to choose
Machine learning and see if similar in meaning.

Possible activities:
Youtube videos
stupid nonsense
by geographic
more specific the better
clustering?

each activity got likes and dislikes 

each reason got user and location
each action

examples of activities:


How is it different from reddit -> things to do
crowdsourced humour


Biggest causes of boredom


people who vote more successful activities are given
use machine learning to collect 


Tech Stack:
Postgres
django rest
django
haystack
mailgun (also for sending errors)

SSL certs
domain name
docker
nginx

In future
redis 


Structure:
models/
services: email, redis,
django shell task functions
Users (username, password, is_verified, email)
Categories (Many to Many with activities)
Boredom ()
Activites (activity name, description, link)
Time needed
Interests (Many to Many with users)
Activation Token
Point system
Reports



    
api
views
serializers