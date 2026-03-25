import { useEffect, useState } from "react";
import { getPods, getCost } from "../api";

export default function Dashboard() {
  const [pods, setPods] = useState([]);
  const [cost, setCost] = useState(0);

  useEffect(() => {
    getPods().then(setPods);
    getCost().then(d => setCost(d.total_cost));
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <h2>Cost: ₹ {cost}</h2>

      {pods.map((p, i) => (
        <div key={i}>{p.name}</div>
      ))}
    </div>
  );
}
