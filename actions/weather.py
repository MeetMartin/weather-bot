from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action

# https://pypi.org/project/weather-api/
from weather import Weather, Unit


class ActionGetWeather(Action):
    def name(self):
        return 'action_get_weather'

    def run(self, dispatcher, tracker, domain):
        weather = Weather(unit=Unit.CELSIUS)
        gpe = ('78735', tracker.get_slot('GPE'))[bool(tracker.get_slot('GPE'))]
        result = weather.lookup_by_location(gpe)
        if result:
            condition = result.condition
            city = result.location.city
            country = result.location.country
            dispatcher.utter_message('It\'s ' + condition.text + ' and ' + condition.temp + '°C in ' +
                                     city + ', ' + country + '.')
        else:
            dispatcher.utter_message('We did not find any weather information for ' + gpe + '. Search by a city name.')
        return
