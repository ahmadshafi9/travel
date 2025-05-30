Want a Mini-Vacay on a budget?

As an international student making those long flights between Dubai and Vancouver for vacations, I kept thinking: "There has to be a way to sneak in a cool, affordable stopover without totally blowing my budget or adding a ton of extra travel time."

Turns out, manually digging through flights and destination guides is a nightmare and usually expensive. So, I decided to build my own solution! This little web app uses some smart behind the scenes magic (graph algorithms, if you're curious!) to figure out the best places you can stop over. It focuses on spots that don't add much extra distance to your main trip, making it easier to find those hidden gems for a quick, wallet-friendly getaway. Think of it as turning your travel time into extra vacation time!

✨ Under the hood
    Frontend:
    HTML: Provides the foundational structure of the user interface.
    CSS: Styles the application, ensuring a clean, modern, and user-friendly experience (with a cool map background!).
    JavaScript: Handles all the dynamic interactions, input processing, and output rendering.
    Python
    
    Core Algorithm:
    Dijkstra's Algorithm: This classic shortest path algorithm is the brain of the operation, enabling the efficient calculation of optimal routes through the network of cities.
    Data Representation: City connections and distances are represented as a weighted graph, allowing for powerful algorithmic analysis.
    
  TripAdvisor Content API: Once potential stopover cities are identified, the application integrates with the TripAdvisor Content API. This integration allows you to pull in helpful information for suggested stopover locations, such as:
Basic Location Details: Name, address, and overall ratings for hotels, attractions, and restaurants.
Curated Content: Access to a limited number of recent reviews and photos to give you a quick glimpse into what the stopover city offers. This helps you quickly assess if a stopover aligns with your mini-vacay interests.

feel free to plan your next mini-vacay at ahmadshafi9.github.io/index.html
