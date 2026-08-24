"use client";

import { useState, useEffect, useRef } from "react";

export default function Chat() {
  const [query, setQuery] = useState("");
  const [userType, setUserType] = useState("general");
  const [activity, setActivity] = useState("");
  const [plannedTime, setPlannedTime] = useState("");
  const [messages, setMessages] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [isListening, setIsListening] = useState(false);
  
  const recognitionRef = useRef<any>(null);

  useEffect(() => {
    if (typeof window !== "undefined") {
      const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
      if (SpeechRecognition) {
        const recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        
        recognition.onresult = (event: any) => {
          const transcript = event.results[0][0].transcript;
          setQuery(transcript);
          setIsListening(false);
        };
        
        recognition.onerror = (event: any) => {
          console.error("Speech recognition error:", event.error);
          setIsListening(false);
        };
        
        recognition.onend = () => {
          setIsListening(false);
        };
        
        recognitionRef.current = recognition;
      }
    }
  }, []);

  const toggleListening = () => {
    if (isListening) {
      recognitionRef.current?.stop();
      setIsListening(false);
    } else {
      recognitionRef.current?.start();
      setIsListening(true);
    }
  };

  const speakText = (text: string) => {
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 1.0;
      window.speechSynthesis.speak(utterance);
    }
  };

  const sendMessage = async (overrideQuery?: string) => {
    const textToSend = overrideQuery || query;
    if (!textToSend.trim()) return;
    
    setMessages((prev) => [...prev, { role: "user", content: textToSend }]);
    setLoading(true);
    setQuery("");

    try {
      const res = await fetch("http://localhost:8000/api/chat/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          message: textToSend, 
          location: "New Delhi",
          lat: 28.6139,
          lon: 77.2090,
          user_type: userType,
          activity: activity || undefined,
          planned_time: plannedTime || undefined
        }),
      });
      const data = await res.json();
      
      setMessages((prev) => [...prev, { role: "ai", content: data.answer, evidence: data.evidence_payload }]);
      speakText(data.answer);
      
    } catch (error) {
      console.error(error);
      setMessages((prev) => [...prev, { role: "ai", content: "Sorry, an error occurred." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-[700px] bg-transparent">
      <div className="bg-gradient-to-r from-blue-700 to-blue-500 text-white p-4 font-bold flex justify-between items-center">
        <span>WeatherGPT Intelligence Engine</span>
        <span className="text-xs bg-white/20 px-2 py-1 rounded-full">Groq Grounded LLM</span>
      </div>
      
      <div className="p-3 bg-white/80 border-b border-blue-100 flex gap-2 text-sm flex-wrap items-center">
        <span className="font-semibold text-slate-700">Context:</span>
        <select className="border rounded p-1" value={userType} onChange={(e) => setUserType(e.target.value)}>
          <option value="general">General</option>
          <option value="farmer">Farmer</option>
          <option value="traveller">Traveller</option>
        </select>
        <input 
          type="text" placeholder="Activity (e.g. Picnic, Spraying)" 
          className="border rounded p-1 w-48"
          value={activity} onChange={(e) => setActivity(e.target.value)} 
        />
        <input 
          type="time" 
          className="border rounded p-1"
          value={plannedTime} onChange={(e) => setPlannedTime(e.target.value)} 
        />
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-white/40">
        {messages.map((msg, i) => (
          <div key={i} className={`flex flex-col ${msg.role === "user" ? "items-end" : "items-start"}`}>
            <div className={`p-3 rounded-2xl max-w-[80%] shadow-sm ${msg.role === "user" ? "bg-blue-600 text-white rounded-tr-sm" : "bg-white text-slate-800 rounded-tl-sm border border-blue-100"}`}>
              {msg.content}
            </div>
            
            {msg.evidence && (
              <div className="mt-2 text-xs w-[80%] space-y-2">
                <div className="flex gap-2">
                  <span className="bg-slate-200 text-slate-700 px-2 py-1 rounded">
                    Confidence: {msg.evidence.uncertainty?.confidence || "N/A"}
                  </span>
                  <span className="bg-red-100 text-red-700 px-2 py-1 rounded">
                    Risk Level: {msg.evidence.risk?.risk_level || "N/A"}
                  </span>
                </div>
                
                {msg.evidence.planner && msg.evidence.planner.status === "CONFLICT_DETECTED" && (
                  <div className="bg-orange-50 border border-orange-200 p-2 rounded text-orange-800">
                    <strong>📅 Planner Conflict:</strong> {msg.evidence.planner.message}
                  </div>
                )}
                {msg.evidence.planner && msg.evidence.planner.status === "SAFE" && (
                  <div className="bg-green-50 border border-green-200 p-2 rounded text-green-800">
                    <strong>📅 Planner:</strong> {msg.evidence.planner.message}
                  </div>
                )}
              </div>
            )}
          </div>
        ))}
        {loading && (
          <div className="flex justify-start">
            <div className="p-3 rounded-2xl bg-white text-blue-500 animate-pulse rounded-tl-sm shadow-sm border border-blue-100">Analyzing weather data & calculating risk...</div>
          </div>
        )}
      </div>
      
      <div className="p-4 bg-white/60 border-t border-blue-100 flex gap-2 items-center backdrop-blur-md">
        <button
          onClick={toggleListening}
          className={`p-3 rounded-full shadow-sm transition-all ${isListening ? 'bg-red-500 text-white animate-pulse' : 'bg-white text-blue-600 hover:bg-blue-50 border border-blue-200'}`}
          title="Voice Input"
        >
          🎤
        </button>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Ask about weather, travel risks, or farming advice..."
          className="flex-1 border border-blue-200 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-400 bg-white shadow-inner text-slate-700"
        />
        <button
          onClick={() => sendMessage()}
          disabled={loading}
          className="bg-blue-600 text-white px-6 py-3 rounded-xl font-bold shadow-md hover:bg-blue-700 transition-colors disabled:opacity-50"
        >
          Send
        </button>
      </div>
    </div>
  );
}
