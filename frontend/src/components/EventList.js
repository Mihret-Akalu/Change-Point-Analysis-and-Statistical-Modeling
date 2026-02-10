import React from "react";

export default function EventList({ events }) {
  return (
    <div>
      <h3>Market Events</h3>
      <ul>
        {events.map((ev, i) => (
          <li key={i}>
            {ev.Date}: <strong>{ev.Event}</strong> — {ev.Category}
          </li>
        ))}
      </ul>
    </div>
  );
}
