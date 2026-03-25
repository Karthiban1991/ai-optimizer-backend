import { useState } from "react";
import { chat } from "../api";

export default function Chat() {
  const [msg, setMsg] = useState("");
  const [res, setRes] = useState("");

  const send = async () => {
    const r = await chat(msg);
    setRes(r.response);
  };

  return (
    <div>
      <input onChange={(e)=>setMsg(e.target.value)} />
      <button onClick={send}>Send</button>
      <p>{res}</p>
    </div>
  );
}
