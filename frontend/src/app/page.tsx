"use client";
import { useEffect, useRef, useState } from "react";

export default function Home() {
  const [messages, setMessages] = useState<{ sender: string; text: string }[]>([]);
  const [input, setInput] = useState("");
  const socketRef = useRef<WebSocket | null>(null);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/");
    socketRef.current = socket;

    socket.onmessage = (event) => {
      setMessages((prev) => [...prev, { sender: "Codey", text: event.data }]);
    };

    socket.onclose = () => {
      setMessages((prev) => [...prev, { sender: "System", text: "Session closed." }]);
    };

    return () => socket.close();
  }, []);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

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
    <div className="flex flex-col h-screen  text-white">
      <div className="flex-1 overflow-y-auto px-6 py-10 space-y-6">
        {messages.length === 0 ? (
          <div className="h-full flex items-center justify-center font-[family-name:var(--font-playfair_display)]">
            <h2 className="text-lg sm:text-2xl text-gray-300">
              <span className="text-orange-500 text-3xl">⚡</span> Yo! Codey in the house. Ready to debug, deploy, or just chat?
            </h2>
          </div>
        ) : (
          messages.map((msg, i) => (
            <div
              key={i}
              className={`max-w-2xl mx-auto px-4 py-3 rounded-xl whitespace-pre-wrap font-[family-name:var(--font-playfair_display)] ${
                msg.sender === "You"
                  ? "bg-[#FBF6E2] text-gray-800 self-end"
                  : msg.sender === "System"
                  ? "text-center text-gray-400 italic"
                  : "bg-[#E68369] text-gray-200"
              }`}
            >
              {msg.sender !== "System" && (
                <div className="text-xs text-black mb-1 italic">{msg.sender}</div>
              )}
              {msg.text}
            </div>
          ))
        )}
        <div ref={bottomRef} />
      </div>

      <div className="border-t border-white/10 px-6 py-4 bg-[#0A0A0A]">
        <div className="max-w-3xl mx-auto flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-4 py-2 backdrop-blur-md font-[family-name:var(--font-playfair_display)]">
          <input
            type="text"
            placeholder="Send a message..."
            className="flex-1 bg-transparent text-white placeholder-gray-400 focus:outline-none"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />
          <button
            onClick={sendMessage}
            className="text-lg px-3 py-1.5 rounded-md bg-orange-600 hover:bg-orange-700 transition"
          >
            ⋈
          </button>
        </div>
      </div>
    </div>
  );
}
