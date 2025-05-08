"use client";
import { useEffect, useRef, useState } from "react";

export default function Home() {
  const [messages, setMessages] = useState<{ sender: string; text: string }[]>([]);
  const [input, setInput] = useState("");
  const socketRef = useRef<WebSocket | null>(null);

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/");
    socketRef.current = socket;

    socket.onmessage = (event) => {
      setMessages((prev) => [...prev, { sender: "AI", text: event.data }]);
    };

    socket.onclose = () => {
      setMessages((prev) => [...prev, { sender: "System", text: "Session closed." }]);
    };

    return () => socket.close();
  }, []);

  const sendMessage = () => {
    if (!input.trim() || socketRef.current?.readyState !== WebSocket.OPEN) return;

    socketRef.current.send(input);
    setMessages((prev) => [...prev, { sender: "You", text: input }]);
    if (["bye", "exit"].includes(input.toLowerCase())) {
      socketRef.current.close();
    }
    setInput("");
  };

  return (
    <main className="p-6 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">AI Developer Assistant</h1>
      <div className="border h-96 overflow-y-auto p-4 bg-white shadow mb-4 rounded">
        {messages.map((msg, i) => (
          <div key={i} className={msg.sender === "You" ? "text-blue-700" : "text-green-700"}>
            <strong>{msg.sender}:</strong> {msg.text}
          </div>
        ))}
      </div>
      <div className="flex gap-2">
        <input
          type="text"
          className="flex-1 border p-2 rounded"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button onClick={sendMessage} className="bg-blue-600 text-white px-4 py-2 rounded">
          Send
        </button>
      </div>
    </main>
  );
}
