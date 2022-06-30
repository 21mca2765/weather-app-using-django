from django.shortcuts import render
import json  # import json to load json data to python dictionary
import urllib.request  # urllib.request to make a request to api
  
  
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        city = city.replace(" ", "+")
        ''' api key might be expired use your own api_key
            place api_key in place of appid ="your_api_key_here "  '''
        # source contain JSON data from API
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=9a081eeac2df4daf845a7c58b1b656c8'+'&units=metric').read()
  
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
  
        # data for variable list_of_data
        data = {
            'city': city.replace("+", " "),
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "status": str(list_of_data['weather'][0]['main']),
            "icon": str(list_of_data['weather'][0]['icon']),
            "temp": str(list_of_data['main']['temp']) + '°C',
            "pressure": str(list_of_data['main']['pressure'])+'hPa',
            "humidity": str(list_of_data['main']['humidity'])+'%',
        }
        print(data)
    else:
        data ={}
    return render(request, "index.html", data)