# api id of walfram alpha:  H64GRT-YJUAVG3QQY

import wolframalpha
import wikipedia


while True:
    user_input = raw_input("Question: ")
    try:
        app_id = "H64GRT-YJUAVG3QQY"
        client = wolframalpha.Client(app_id)
        result = client.query(user_input)
        answer = next(result.results).text
        print(answer)
    
    except:
        try:
            print(wikipedia.summary(user_input, sentences=2))
        except:
            print("I'm not aware of it.!")
