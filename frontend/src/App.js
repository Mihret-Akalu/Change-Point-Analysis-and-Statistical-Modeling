import React, { useEffect, useState } from "react";
import PriceChart from "./components/PriceChart";
import EventList from "./components/EventList";
import { fetchPrices, fetchEvents } from "./api";

function App() {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetchPrices().then(setPrices);
    fetchEvents().then(setEvents);
  }, []);

  return (
    <div className="App">
      <h1>Brent Oil Price Dashboard</h1>
      <PriceChart prices={prices} />
      <EventList events={events} />
    </div>
  );
}

export default App;
