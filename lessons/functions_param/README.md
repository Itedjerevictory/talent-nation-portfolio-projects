A function can accept multiple parameters separated by commas inside its parentheses. These variables are local to the function and can be used anywhere inside its indented body.



Real-World Application
Flexible parameter architectures are the engine behind modern REST API integrations, such as weather data platforms (e.g., OpenWeatherMap API).

When an app requests weather data, it calls an API request function:

get_weather_report(location="Chicago", units="metric", language="en")
The developers of the API made the units and language parameters completely optional by assigning default values (units="metric", language="en"), because $90%$ of global queries want standard metric outputs in English. However, if a user in the United States needs Fahrenheit or a user in Spain needs Spanish text, they can explicitly override the defaults:

get_weather_report(location="Madrid", units="imperial", language="es")
If default parameters did not exist, every single developer would be forced to type out units="metric" and language="en" for every simple request. By setting clean defaults, we keep our APIs easy to use, while retaining the flexibility to adapt to specialty parameters on demand. This pattern is utilized across every major software SDK in the industry.