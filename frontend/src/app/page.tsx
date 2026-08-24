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
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          
          {/* Left Column: Data & Analytics */}
          <div className="lg:col-span-2 space-y-6">
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* Evidence Panel */}
              <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 space-y-4">
                <h2 className="text-xl font-bold text-slate-800">Forecast Validation</h2>
                <div className="space-y-3 text-sm">
                  <div className="flex justify-between items-center border-b pb-2">
                    <span className="text-slate-500">Source Agreement</span>
                    <span className="bg-green-100 text-green-700 px-2 py-1 rounded font-bold">HIGH</span>
                  </div>
                  <div className="flex justify-between items-center border-b pb-2">
                    <span className="text-slate-500">Observation MAE</span>
                    <span className="font-mono">1.2°C</span>
                  </div>
                  <div className="flex justify-between items-center">
                    <span className="text-slate-500">Overall Confidence</span>
                    <span className="text-blue-600 font-bold">MODERATE (85%)</span>
                  </div>
                </div>
              </div>

              {/* Personal Weather Planner Panel */}
              <div className="bg-white p-6 rounded-2xl shadow-sm border border-blue-200 bg-gradient-to-br from-white to-blue-50 space-y-4">
                <h2 className="text-xl font-bold text-blue-800">📅 Weather Planner</h2>
                <div className="text-sm">
                  <p className="text-slate-600 mb-2">Event: <span className="font-semibold text-slate-900">Outdoor Event (6:00 PM)</span></p>
                  
                  {/* Visual Timeline */}
                  <div className="space-y-2 mt-4 font-mono text-xs">
                    <div className="flex items-center gap-2">
                      <span className="w-12 text-slate-500">4:00</span>
                      <div className="h-4 bg-orange-300 w-1/4 rounded"></div>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="w-12 text-green-600 font-bold">4:30</span>
                      <div className="h-4 bg-green-400 w-1/12 rounded relative">
                        <span className="absolute -right-12 text-green-700 font-bold">← BEST</span>
                      </div>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="w-12 text-slate-500">5:00</span>
                      <div className="h-4 bg-orange-400 w-1/3 rounded"></div>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="w-12 text-red-500 font-bold">6:00</span>
                      <div className="h-4 bg-red-500 w-3/4 rounded"></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* AI Chat Interface */}
            <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
              <Chat />
            </div>

          </div>

          {/* Right Column: Alerts & Live Stream */}
          <div className="space-y-6">
            <Alerts />
            
            <div className="bg-slate-800 text-slate-300 p-6 rounded-2xl shadow-sm space-y-3 font-mono text-xs">
              <h3 className="text-white font-bold mb-4 uppercase tracking-wider">System Logs</h3>
              <p>[INFO] Ingesting GFS 0.25deg...</p>
              <p>[INFO] Ingesting AWS Obs...</p>
              <p className="text-green-400">[SUCCESS] Multi-source Fusion Complete.</p>
              <p>[INFO] Uncertainty Engine: Score 25</p>
              <p>[INFO] Awaiting LLM Generation...</p>
              <p className="text-blue-400">[VALIDATOR] Output aligns with evidence.</p>
            </div>
          </div>

        </div>
      </div>
    </main>
  );
}
