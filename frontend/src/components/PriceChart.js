import React from "react";
import { Line } from "react-chartjs-2";

export default function PriceChart({ prices }) {
  const data = {
    labels: prices.map(p => p.Date),
    datasets: [
      {
        label: "Brent Price (USD)",
        data: prices.map(p => p.Price),
        borderColor: "rgba(75,192,192,1)",
        fill: false,
      },
    ],
  };

  return <Line data={data} />;
}
