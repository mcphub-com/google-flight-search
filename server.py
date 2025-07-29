import os, requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP('serp-map')


serp_url = "https://serpapi.com/search"
serp_api_key = os.getenv("SERP_API_KEY")

@mcp.tool()
def search_flight(
                departure_id: Annotated[str, Field(description='Parameter defines the departure airport code or location kgmid.An airport code is an uppercase 3-letter code. You can search for it on Google Flights or IATA.For example, CDG is Paris Charles de Gaulle Airport and AUS is Austin-Bergstrom International Airport.A location kgmid is a string that starts with /m/. You can search for a location on Wikidata and use its "Freebase ID" as the location kgmid. For example, /m/0vzm is the location kgmid for Austin, TX.You can specify multiple departure airports by separating them with a comma. For example, CDG,ORY,/m/04jpl.')],
                arrival_id: Annotated[str, Field(description='Parameter defines the arrival airport code or location kgmid.An airport code is an uppercase 3-letter code. You can search for it on Google Flights or IATA.For example, CDG is Paris Charles de Gaulle Airport and AUS is Austin-Bergstrom International Airport.A location kgmid is a string that starts with /m/. You can search for a location on Wikidata and use its "Freebase ID" as the location kgmid. For example, /m/0vzm is the location kgmid for Austin, TX.You can specify multiple arrival airports by separating them with a comma. For example, CDG,ORY,/m/04jpl.')],
                type: Annotated[Union[int, None], Field(description="Parameter defines the type of the flights. Available options: 1 - Round trip (default) 2 - One way 3 - Multi-city . When this parameter is set to 3, use multi_city_json to set the flight information. To obtain the returning flight information for Round Trip (1), you need to make another request using a departure_token.")] = None,
                outbound_date: Annotated[Union[str, None], Field(description="Parameter defines the outbound date. The format is YYYY-MM-DD. e.g. 2025-06-24")] = None,
                return_date: Annotated[Union[str, None], Field(description="Parameter defines the return date. The format is YYYY-MM-DD. e.g. 2025-06-30. Parameter is required if type parameter is set to: 1 (Round trip)")] = None,
                travel_class: Annotated[Union[int, None], Field(description="Parameter defines the travel class. Available options: 1 - Economy (default) 2 - Premium economy 3 - Business 4 - First")] = None,
                multi_city_json: Annotated[Union[str, None], Field(description="""Parameter defines the flight information for multi-city flights. It's a JSON string containing multiple flight information objects. Each object should contain the following fields: departure_id - The departure airport code or location kgmid. The format is the same as the main departure_id parameter. arrival_id - The arrival airport code or location kgmid. The format is the same as the main arrival_id parameter. date - Flight date. The format is the same as the outbound_date parameter. times - Time range for the flight. The format is the same as the outbound_times parameter. This parameter is optional. Example: [{"departure_id":"CDG","arrival_id":"NRT","date":"2025-06-30"},{"departure_id":"NRT","arrival_id":"LAX,SEA","date":"2025-07-07"},{"departure_id":"LAX,SEA","arrival_id":"AUS","date":"2025-07-14","times":"8,18,9,23"}] The example is a multi-city flight from CDG to NRT on 2025-06-30, then from NRT to LAX or SEA on 2025-07-07, and finally from LAX or SEA to AUS on 2025-07-14. The last flight has a departure time range from 8:00 AM to 7:00 PM and an arrival time range from 9:00 AM to 12:00 AM (Midnight).""")] = None,
                adults: Annotated[Union[int, None], Field(description="Parameter defines the number of adults. Default to 1.")] = None,
                children: Annotated[Union[int, None], Field(description="Parameter defines the number of children. Default to 0.")] = None,
                infants_in_seat: Annotated[Union[int, None], Field(description="Parameter defines the number of infants_in_seat. Default to 0.")] = None,
                infants_on_lap: Annotated[Union[int, None], Field(description="Parameter defines the number of infants_on_lap. Default to 0.")] = None,
                sort_by: Annotated[Union[int, None], Field(description="Parameter defines the sorting order of the results. Available options: 1 - Top flights (default) 2 - Price 3 - Departure time 4 - Arrival time 5 - Duration 6 - Emissions")] = None,
                stops: Annotated[Union[int, None], Field(description="Parameter defines the number of stops during the flight. Available options: 0 - Any number of stops (default) 1 - Nonstop only 2 - 1 stop or fewer 3 - 2 stops or fewer")] = None,
                bags: Annotated[Union[int, None], Field(description="Parameter defines the number of carry-on bags. Default to 0.")] = None,
               max_price: Annotated[Union[float, None], Field(description="Parameter defines the maximum ticket price. Default to unlimited.")] = None,
                outbound_times: Annotated[Union[str, None], Field(description="Parameter defines the outbound times range. It's a string containing two (for departure only) or four (for departure and arrival) comma-separated numbers. Each number represents the beginning of an hour. For example:  4,18: 4:00 AM - 7:00 PM departure  0,18: 12:00 AM - 7:00 PM departure  19,23: 7:00 PM - 12:00 AM departure  4,18,3,19: 4:00 AM - 7:00 PM departure, 3:00 AM - 8:00 PM arrival  0,23,3,19: unrestricted departure, 3:00 AM - 8:00 PM arrival")] = None,
                return_times: Annotated[Union[str, None], Field(description="Parameter defines the return times range. It's a string containing two (for departure only) or four (for departure and arrival) comma-separated numbers. Each number represents the beginning of an hour. For example: 4,18: 4:00 AM - 7:00 PM departure 0,18: 12:00 AM - 7:00 PM departure 19,23: 7:00 PM - 12:00 AM departure 4,18,3,19: 4:00 AM - 7:00 PM departure, 3:00 AM - 8:00 PM arrival 0,23,3,19: unrestricted departure, 3:00 AM - 8:00 PM arrival Parameter should only be used when type parameter is set to: 1 (Round trip)")] = None,
                layover_duration: Annotated[Union[str, None], Field(description="Parameter defines the layover duration, in minutes. It's a string containing two comma-separated numbers. For example, specify 90,330 for 1 hr 30 min - 5 hr 30 min.")] = None,
                max_duration: Annotated[Union[int, None], Field(description="Parameter defines the maximum flight duration, in minutes. For example, specify 1500 for 25 hours.")] = None,
                departure_token: Annotated[Union[str, None], Field(description="Parameter is used to select the flight and get returning flights (for Round trip) or flights for the next leg of itinerary (for Multi-city). Find this token in the departure flight results.It cannot be used together with booking_token.")] = None,
               booking_token: Annotated[Union[str, None], Field(description="Parameter is used to get booking options for the selected flights. Find this token in the flight results.It cannot be used together with departure_token. When using this token, parameters related to date and parameters inside 'Advanced Filters' section won't affect the result.")] = None,
               emissions: Annotated[Union[int, None], Field(description="Parameter defines the emission level of the flight.Available options: 1 - Less emissions only")] = None,
                no_cache: Annotated[Union[bool, None], Field(description="Parameter will force SerpApi to fetch the Google Jobs results even if a cached version is already present. A cache is served only if the query and all parameters are exactly the same. Cache expires after 1h. Cached searches are free, and are not counted towards your searches per month. It can be set to false (default) to allow results from the cache, or true to disallow results from the cache. no_cache and async parameters should not be used together.")] = None,
                aasync: Annotated[Union[bool, None], Field(description="Parameter defines the way you want to submit your search to SerpApi. It can be set to false (default) to open an HTTP connection and keep it open until you got your search results, or true to just submit your search to SerpApi and retrieve them later. In this case, you'll need to use our Searches Archive API to retrieve your results. async and no_cache parameters should not be used together. async should not be used on accounts with Ludicrous Speed enabled.")] = None
            ):
    '''This tool allows you to scrape flight results from Google Flights.'''
    print(departure_id)
    payload = {
        'engine': "google_flights",
        'api_key': serp_api_key,
        'departure_id': departure_id,
        "arrival_id": arrival_id,
        'type': type,
        'outbound_date': outbound_date,
        'return_date': return_date,
        'travel_class': travel_class,
        'multi_city_json': multi_city_json,
        'adults': adults,
        'children': children,
        'infants_in_seat': infants_in_seat,
        'infants_on_lap': infants_on_lap,
        'sort_by': sort_by,
        'stops': stops,
        'bags': bags,
        'max_price': max_price,
        'outbound_times': outbound_times,
        'return_times': return_times,
        'layover_duration': layover_duration,
        'max_duration': max_duration,
        'departure_token': departure_token,
        'booking_token': booking_token,
        'emissions': emissions,
        "no_cache": no_cache,
        "async": aasync
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    print(payload)

    response = requests.get(serp_url, params=payload)
    print(response)
    return response.json()

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")