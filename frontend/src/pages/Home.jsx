import { useState } from "react";
import { generateContent } from "../services/contentService";
import {
  FiFileText,
  FiLinkedin,
  FiTwitter,
  FiInstagram,
  FiActivity,
  FiEdit3,
} from "react-icons/fi";

const CONTENT_TYPES = [
  { id: "blog", label: "Artículo / Blog", icon: <FiFileText /> },
  { id: "linkedin", label: "LinkedIn", icon: <FiLinkedin /> },
  { id: "twitter", label: "Twitter / X", icon: <FiTwitter /> },
  { id: "instagram", label: "Instagram", icon: <FiInstagram /> },
  { id: "scientific", label: "Científico (RAG)", icon: <FiActivity /> },
];

const Home = () => {
  const [contentType, setContentType] = useState(null);
  const [topic, setTopic] = useState("");
  const [audience, setAudience] = useState("");
  const [tone, setTone] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState("");

  const handleGenerate = async () => {
    if (!topic) return;

    setLoading(true);
    setResult("");

    try {
      const data = await generateContent({
        topic,
        audience,
        tone,
        platform: contentType,
      });

      setResult(data.content);
    } catch (err) {
      console.error(err);
      setResult("❌ Error generando contenido");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex-1 flex items-center justify-center px-10">
      <div className="w-full max-w-7xl grid grid-cols-12 gap-8 h-155">

        {/* PANEL IZQUIERDO */}
        <div className="col-span-4 bg-slate-900/80 backdrop-blur-xl rounded-2xl 
          border border-indigo-500/20 p-6
          shadow-[0_0_40px_rgba(79,70,229,0.25)] flex flex-col">

          <h2 className="text-white text-lg font-semibold mb-4">
            ¿Qué quieres generar?
          </h2>

          <div className="flex flex-col gap-3">
            {CONTENT_TYPES.map((type) => (
              <button
                key={type.id}
                onClick={() => setContentType(type.id)}
                className={`
                  flex items-center gap-3 px-4 py-4 rounded-xl text-sm font-medium
                  border transition-all duration-200
                  ${
                    contentType === type.id
                      ? "bg-indigo-600/30 border-indigo-400 text-white shadow-[0_0_25px_rgba(139,92,246,0.7)]"
                      : "bg-slate-950/60 border-white/10 text-white hover:bg-slate-800/60"
                  }
                `}
              >
                <span className="text-lg">{type.icon}</span>
                {type.label}
              </button>
            ))}
          </div>

          {/* INPUTS */}
          {contentType && (
            <div className="mt-6 space-y-3">
              <input
                className="w-full rounded-lg bg-slate-950/60 border border-white/10 
                  px-4 py-2 text-sm text-white placeholder-white/40
                  focus:outline-none focus:ring-2 focus:ring-indigo-500"
                placeholder="Tema"
                value={topic}
                onChange={(e) => setTopic(e.target.value)}
              />

              <input
                className="w-full rounded-lg bg-slate-950/60 border border-white/10 
                  px-4 py-2 text-sm text-white placeholder-white/40"
                placeholder="Audiencia"
                value={audience}
                onChange={(e) => setAudience(e.target.value)}
              />

              <input
                className="w-full rounded-lg bg-slate-950/60 border border-white/10 
                  px-4 py-2 text-sm text-white placeholder-white/40"
                placeholder="Tono"
                value={tone}
                onChange={(e) => setTone(e.target.value)}
              />

              <div className="bg-indigo-900/40 border border-indigo-500/30 
                rounded-lg p-3 text-xs text-indigo-200">
                💡 Cuanto más específico seas, mejor será el resultado.
              </div>

              <button
                onClick={handleGenerate}
                disabled={loading}
                className="w-full mt-2 py-3 rounded-xl font-semibold text-white
                  bg-linear-to-r from-indigo-600 to-violet-600
                  hover:from-indigo-700 hover:to-violet-700
                  shadow-[0_0_25px_rgba(99,102,241,0.8)]
                  transition-all"
              >
                {loading ? "Generando..." : "✨ Generar contenido"}
              </button>
            </div>
          )}
        </div>

        {/* PANEL DERECHO */}
        <div className="col-span-8 bg-slate-900/80 backdrop-blur-xl rounded-2xl 
          border border-indigo-500/20 flex items-center justify-center
          shadow-[0_0_40px_rgba(79,70,229,0.25)]
          relative overflow-hidden p-8">

          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(99,102,241,0.2),transparent_70%)]" />

          {!contentType && (
            <div className="relative z-10 text-center">
              <div className="w-20 h-20 mx-auto mb-6 rounded-2xl 
                bg-indigo-600/30 
                shadow-[0_0_30px_rgba(99,102,241,0.8)]
                flex items-center justify-center">
                <FiEdit3 className="text-indigo-300 w-10 h-10" />
              </div>

              <h3 className="text-white text-2xl font-semibold mb-2">
                Comienza a crear
              </h3>

              <p className="text-white/60 max-w-md mx-auto mb-6">
                Selecciona un tipo de contenido y rellena los campos para generar
                contenido optimizado con IA
              </p>

              <div className="grid grid-cols-2 gap-3 max-w-md mx-auto text-sm">
                <span className="bg-indigo-600/30 text-white py-2 rounded-lg">
                  ✓ Multi-plataforma
                </span>
                <span className="bg-violet-600/30 text-white py-2 rounded-lg">
                  ✓ Personalizable
                </span>
                <span className="bg-blue-600/30 text-white py-2 rounded-lg">
                  ✓ Varios modelos
                </span>
                <span className="bg-cyan-600/30 text-white py-2 rounded-lg">
                  ✓ IA Avanzada
                </span>
              </div>
            </div>
          )}

          {result && (
            <pre className="relative z-10 w-full h-full overflow-auto 
              bg-slate-950/60 rounded-xl p-6 text-sm text-white whitespace-pre-wrap">
              {result}
            </pre>
          )}
        </div>

      </div>
    </div>
  );
};

export default Home;
