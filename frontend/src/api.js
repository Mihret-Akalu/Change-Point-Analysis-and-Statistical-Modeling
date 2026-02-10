// frontend/src/api.js
import axios from "axios";

const BASE = "http://localhost:5000/api";

export const fetchPrices = (start, end) => {
  let url = `${BASE}/prices`;
  if (start || end) {
    const params = new URLSearchParams();
    if (start) params.append("start", start);
    if (end) params.append("end", end);
    url += "?" + params.toString();
  }
  return axios.get(url).then(res => res.data);
};

export const fetchEvents = () =>
  axios.get(`${BASE}/events`).then(res => res.data);

export const fetchChangePoints = () =>
  axios.get(`${BASE}/change_points`).then(res => res.data);
