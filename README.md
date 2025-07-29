# Aigeon AI Google Flight Search

Aigeon AI Google Flight Search is a Python-based server application designed to interact with the Google Flights search API. This application allows users to search for flights based on various parameters, providing a flexible and comprehensive flight search experience.

## Features Overview

- **Flexible Flight Search**: Search flights using a variety of parameters such as departure and arrival locations, dates, travel class, and more.
- **Multi-city and Round Trip Support**: Supports complex itineraries including multi-city trips and round trips.
- **Customizable Search Options**: Customize searches with options for sorting, number of stops, and price limits.
- **Language and Country Customization**: Specify the language and country for the search to tailor results to specific locales.

## Main Features and Functionality

The application is built using the FastMCP framework, which facilitates the creation of tools and services. The core functionality revolves around the `search_flight` function, which is a tool that interfaces with the Google Flights API to perform flight searches based on user-defined parameters.

### Main Functions Description

#### `search_flight`

The `search_flight` function is the primary tool for searching flights. It accepts a wide range of parameters to tailor the search results to the user's needs:

- **departure_id**: Specifies the departure airport code or location kgmid. Multiple airports can be specified using commas.
- **arrival_id**: Specifies the arrival airport code or location kgmid. Multiple airports can be specified using commas.
- **gl**: Defines the country for the Google search using a two-letter country code.
- **hl**: Defines the language for the search using a two-letter language code.
- **type**: Defines the type of flight (1 for Round trip, 2 for One way, 3 for Multi-city).
- **outbound_date**: Specifies the outbound date in YYYY-MM-DD format.
- **return_date**: Specifies the return date in YYYY-MM-DD format (required for round trips).
- **travel_class**: Defines the travel class (1 for Economy, 2 for Premium economy, 3 for Business, 4 for First).
- **multi_city_json**: Provides flight information for multi-city flights in JSON format.
- **adults**: Specifies the number of adults (default is 1).
- **children**: Specifies the number of children (default is 0).
- **infants_in_seat**: Specifies the number of infants in a seat (default is 0).
- **infants_on_lap**: Specifies the number of infants on a lap (default is 0).
- **sort_by**: Defines the sorting order of results (options include Top flights, Price, Departure time, etc.).
- **stops**: Defines the number of stops during the flight (options include Nonstop only, 1 stop or fewer, etc.).
- **bags**: Specifies the number of carry-on bags (default is 0).
- **max_price**: Defines the maximum ticket price (default is unlimited).
- **outbound_times**: Specifies the outbound times range for departure and arrival.
- **return_times**: Specifies the return times range for round trips.
- **layover_duration**: Defines the layover duration in minutes.
- **max_duration**: Defines the maximum flight duration in minutes.
- **departure_token**: Used to select the flight and get returning flights for round trips or next leg for multi-city itineraries.
- **booking_token**: Used to get booking options for the selected flight.

This function integrates with the SerpAPI to fetch flight data, ensuring a robust and reliable search experience. The use of environment variables for API keys ensures secure and flexible configuration management.