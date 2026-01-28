import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // FastAPI
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 60000,
});

export default api;
