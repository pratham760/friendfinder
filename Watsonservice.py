
from watson_developer_cloud import PersonalityInsightsV3
from watson_developer_cloud import NaturalLanguageUnderstandingV1 

url1="https://gateway-lon.watsonplatform.net/personality-insights/api"
key="WFx1XYgSCtuLqbJcciucd4-b7kujEv8zJ79sK9UbbM9r"
service = PersonalityInsightsV3(url=url1,iam_apikey=key,version='2017-10-13')

url2="https://gateway-lon.watsonplatform.net/natural-language-understanding/api"
key="CAodfBJl-BscGPOSm6UrBeRK9sbSlzDS13kgLf4g-69X"
nlu_service = NaturalLanguageUnderstandingV1(url=url2,iam_apikey=key,version='2017-10-13')

    


