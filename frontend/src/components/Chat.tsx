"use client";

import { useState, useEffect, useRef } from "react";

export default function Chat() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState<{ role: string; content: string }[]>([]);
  const [loading, setLoading] = useState(false);
  const [isListening, setIsListening] = useState(false);
  
  // Reference for the speech recognition instance
  const recognitionRef = useRef<any>(null);

  useEffect(() => {
    // Initialize Web Speech API for voice recognition if supported
    if (typeof window !== "undefined") {
      const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
      if (SpeechRecognition) {
        const recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        // Optional: Support hindi/hinglish context by setting lang if needed, e.g. recognition.lang = 'hi-IN';
        
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
      // Stop any ongoing speech
      window.speechSynthesis.cancel();
      
      const utterance = new SpeechSynthesisUtterance(text);
      // Optional: adjust voice, pitch, rate
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
      const res = await fetch("http://localhost:8000/api/v1/ai/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: textToSend, language: "english" }), // Could dynamically change language
      });
      const data = await res.json();
      
      setMessages((prev) => [...prev, { role: "ai", content: data.response }]);
      
      // AI speaks out the response
      speakText(data.response);
      
    } catch (error) {
      console.error(error);
      setMessages((prev) => [...prev, { role: "ai", content: "Sorry, an error occurred." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-[550px] bg-transparent">
      <div className="bg-gradient-to-r from-blue-700 to-blue-500 text-white p-4 font-bold flex justify-between items-center">
        <span>AI Intelligence Layer</span>
        <span className="text-xs bg-white/20 px-2 py-1 rounded-full">Groq LLM Powered</span>
      </div>
      <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-white/40">
        {messages.map((msg, i) => (
          <div key={i} className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
            <div className={`p-3 rounded-2xl max-w-[80%] shadow-sm ${msg.role === "user" ? "bg-blue-600 text-white rounded-tr-sm" : "bg-white text-slate-800 rounded-tl-sm border border-blue-100"}`}>
              {msg.content}
            </div>
          </div>
        ))}
        {loading && (
          <div className="flex justify-start">
            <div className="p-3 rounded-2xl bg-white text-blue-500 animate-pulse rounded-tl-sm shadow-sm border border-blue-100">Analyzing weather data...</div>
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
