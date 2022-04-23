from bs4 import BeautifulSoup
import requests
import pandas as pd

def country_stats(country):
    content = requests.get('https://www.countryreports.org/country/'+country+'.htm')
    soup = BeautifulSoup(content.content, 'html.parser')
    stats = soup.find_all('tr')
    stats_dic = dict()
    for i in stats: #create a dictionary of all country details
        index = 0
        for x in i.find_all('td'):
            if index in stats_dic:
                stats_dic[index].append((x.text.replace("\n\n", " ")).strip())
            else:
                stats_dic[index] = list()
                stats_dic[index].append((x.text.replace("\n\n", " ")).strip())
            index +=1 
    stats_name = (list(stats_dic.values()))[0]
    stats_val = (list(stats_dic.values()))[1]
    stats_df = pd.DataFrame(stats_val,stats_name).transpose()
    stats_df.index = [country]
    return stats_df

countries_lst = ['Mexico','China','Japan','KoreaSouth','Taiwan','India','Philippines'
                  ,'Thailand','France','Italy','Spain','Brazil','Israel','UnitedStatesofAmerica'
                ,'Algeria','Angola','Benin','Botswana','BurkinaFaso','Burundi','Cameroon','CapeVerde'
                ,'CentralAfricanRepublic','Chad','Comoros','CotedIvoire','DemocraticRepublicoftheCongo'
                ,'Guinea','GuineaBissau','Kenya','Lesotho','Liberia','Libya','Madagascar','Malawi','Mali'
                 ,'Rwanda','SaintHelena','SaoTomeandPrincipe','Senegal','Seychelles','Belize','CostaRica'  
                ,'ElSalvador','Guatemala','Anguilla','Honduras','AntiguaandBarbuda','Nicaragua','Aruba','Panama'
                ,'Barbados','Grenada','BritishVirginIslands','SaintLucia','CaymanIslands','Guadeloupe','Cuba'
                 ,'SaintVincentandtheGrenadines','Dominica','Haiti','DominicanRepublic','TheBahamas','Jamaica'
                 ,'PuertoRico','SaintKittsandNevis','SierraLeone','Somalia','SouthAfrica','SouthSudan','Sudan'
                 ,'Tanzania','TheGambia','Togo','Tunisia','Uganda','WesternSahara','Zambia','Zimbabwe'
                 ,'Afghanistan','Akrotiri','Albania','AmericanSamoa','Andorra','Argentina','Armenia','Australia'
                 ,'Austria','Azerbaijan','Bahrain','Bangladesh','Belarus','Belgium','Bermuda','Bhutan','Bolivia'
                 ,'BosniaandHerzegovina','Brunei','Bulgaria','Burma','Cambodia','Canada','Chile','ChristmasIsland'
                 ,'CocosKeelingIslands','Colombia','CookIslands','CoralSeaIslands','Croatia','Cyprus'
                 ,'CzechRepublic','Denmark','Dhekelia','Ecuador','Estonia','FalklandIslands','FaroeIslands'
                 ,'Fiji','Finland','FrenchGuiana','FrenchPolynesia','GazaStrip','Georgia','Germany','Gibraltar'
                 ,'Greece','Greenland','Guam','Guernsey','Guyana','HolySee','HongKong','Hungary','Iceland'
                 ,'Kosovo','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Liechtenstein','Lithuania'
                 ,'Luxembourg','Macau','Macedonia','Malaysia','Maldives','Malta','MarshallIslands','Micronesia'
                 ,'Moldova','Monaco','Mongolia','Montenegro','Nauru','Nepal','Netherlands','NewCaledonia','NewZealand'
                 ,'PapuaNewGuinea','Paraguay','Peru','PitcairnIslands','Poland','Portugal','Qatar','Romania','Russia'
                   ,'SaintPierreandMiquelon','Samoa','SanMarino','SaudiArabia','Serbia','Singapore','Slovakia'
                 ,'Slovenia','SolomonIslands','SriLanka','Suriname','Sweden','Switzerland','Syria','Tajikistan'
                 ,'TimorLeste','Tokelau','Tonga','Turkey','Turkmenistan','Tuvalu','Ukraine'
                  ,'UnitedArabEmirates','UnitedKingdom','Uruguay','Uzbekistan','Vanuatu','Venezuela'
                 ,'Vietnam','WakeIsland','WallisandFutuna','WestBank','Yemen','Djibouti',
                 'Egypt','EquatorialGuinea','Eritrea','Eswatini','Ethiopia','Gabon','Ghana'
             ,'Mauritania','Mayotte','Morocco','Mozambique','Namibia','Niger','Nigeria','RepublicoftheCongo'   
                 ,'TrinidadandTobago','Martinique','TurksandCaicosIslands','Montserrat','VirginIslands'
                 ,'Indonesia','Iran','Iraq','Ireland','Norway','Oman','Pakistan','Jersey','Jordan'
                ,'Niue','NorfolkIsland','NorthernMarianaIslands','Palau','Kazakhstan','Kiribati']
                
countries_stats = []  
for i in countries_lst:
                 countries_stats.append(country_stats(i))
countries_stats

