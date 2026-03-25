const API = "http://localhost:8000";

export const getPods = () => fetch(API + "/pods").then(r => r.json());
export const getCost = () => fetch(API + "/cost").then(r => r.json());
export const chat = (msg) =>
  fetch(API + "/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({prompt: msg})
  }).then(r => r.json());
