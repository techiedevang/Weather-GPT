import Chat from "@/components/Chat";
import Alerts from "@/components/Alerts";
import WeatherWidget from "@/components/WeatherWidget";

export default function Home() {
  return (
    <div className="min-h-screen text-slate-800 relative overflow-hidden">
      {/* Background Clouds */}
      <div className="absolute top-10 left-10 opacity-30 text-8xl">☁️</div>
      <div className="absolute top-40 right-20 opacity-40 text-9xl">☁️</div>
      <div className="absolute bottom-20 left-1/4 opacity-20 text-9xl">☁️</div>
      
      <div className="relative z-10 max-w-7xl mx-auto p-4 sm:p-8 space-y-8">
        
        <header className="flex flex-col md:flex-row justify-between items-center bg-white/60 backdrop-blur-md p-6 rounded-2xl shadow-sm border border-white/50">
          <div>
            <h1 className="text-4xl font-extrabold text-blue-900 drop-shadow-sm flex items-center gap-3">
              <span className="text-5xl">🌩️</span> WeatherGPT
            </h1>
            <p className="text-blue-700 mt-1 font-medium">AI-Powered Meteorological Intelligence</p>
          </div>
          <div className="mt-4 md:mt-0 flex gap-2">
            <span className="px-3 py-1 bg-aqua-100 text-teal-800 bg-teal-100 rounded-full text-sm font-bold shadow-sm">SIH Internal Hackathon</span>
            <span className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm font-bold shadow-sm">MVP v1.0</span>
          </div>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
          
          {/* Left Column */}
          <div className="lg:col-span-8 space-y-8">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <WeatherWidget />
              <div className="bg-white/70 backdrop-blur-md rounded-2xl p-6 shadow-lg border border-white/50 flex flex-col justify-center">
                <h2 className="text-xl font-bold text-blue-900 mb-2">Location & Context</h2>
                <p className="text-slate-600 mb-4">
                  Currently tracking weather events in your area. Use the AI Chat below to get travel, farmer, or citizen advisories based on deterministic risk engines.
                </p>
                <div className="flex gap-2">
                  <span className="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-md">Hindi</span>
                  <span className="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-md">English</span>
                  <span className="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-md">Voice Enabled</span>
                </div>
              </div>
            </div>
            
            <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-xl border border-white/50 overflow-hidden">
               <Chat />
            </div>
          </div>

          {/* Right Column */}
          <div className="lg:col-span-4 space-y-8">
            <Alerts />
            
            <div className="bg-gradient-to-br from-teal-400 to-cyan-500 rounded-2xl shadow-xl p-6 text-white border border-teal-300 relative overflow-hidden">
              <div className="absolute -right-4 -bottom-4 opacity-20 text-8xl">🗺️</div>
              <h2 className="text-xl font-bold mb-2 relative z-10">Risk Map</h2>
              <div className="h-40 bg-black/10 rounded-xl flex items-center justify-center backdrop-blur-sm relative z-10 border border-white/20 mt-4">
                <p className="text-sm font-medium">Map integration ready for Phase 2</p>
              </div>
            </div>
          </div>
          
        </div>
      </div>
    </div>
  );
}
