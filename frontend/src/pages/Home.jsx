import { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import api from "../services/api";
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
  const [checkingImage, setCheckingImage] = useState(false);
  const [result, setResult] = useState(null);

  const handleGenerate = async () => {
    if (!topic) return;

    setLoading(true);
    setResult(null);

    try {
      const data = await generateContent({
        topic,
        audience,
        tone,
        platform: contentType,
      });

      // Normalizar estructura de respuesta: soportar { content }, { answer }, string, etc.
      let contentText = "";
      if (!data) {
        contentText = "";
      } else if (typeof data === "string") {
        contentText = data;
      } else {
        contentText = data.content || data.answer || data.text || data.result || "";
      }

      // Buscar posible referencia a la imagen en varios campos
      const imageField = data?.image || data?.image_url || data?.image_filename || data?.filename || data?.file;

      let imageUrl = null;
      if (imageField) {
        if (typeof imageField === "string") {
          if (imageField.startsWith("http")) {
            imageUrl = imageField;
          } else if (imageField.startsWith("/")) {
            imageUrl = `${api.defaults.baseURL}${imageField}`;
          } else {
            imageUrl = `${api.defaults.baseURL}/images/${imageField}`;
          }
        }
      }

      setResult({ content: contentText, image_url: imageUrl });
    } catch (err) {
      console.error(err);
      setResult({ content: "❌ Error generando contenido" });
    } finally {
      setLoading(false);
    }
  };

  const handleCheckImage = async () => {
    setCheckingImage(true);

    try {
      // Intentar pedir al backend la imagen asociada al último tema
      const res = await axios.get(`${api.defaults.baseURL}/api/image`, {
        params: { tema: topic },
      });

      const imageField = res.data?.image || res.data?.image_url || res.data?.image_filename || res.data?.filename;
      if (imageField) {
        let imageUrl = imageField;
        if (!imageUrl.startsWith("http")) {
          if (imageUrl.startsWith("/")) imageUrl = `${api.defaults.baseURL}${imageUrl}`;
          else imageUrl = `${api.defaults.baseURL}/images/${imageUrl}`;
        }

        setResult((prev) => ({ ...prev, image_url: imageUrl }));
      }
    } catch (err) {
      console.error("Error cargando imagen", err);
    } finally {
      setCheckingImage(false);
    }
  };

  return (
    <div className="flex-1 flex items-center justify-center px-10">
      <div className="w-full max-w-7xl grid grid-cols-12 gap-8 h-[85vh]">

        {/* PANEL IZQUIERDO */}
        <div className="col-span-4 bg-slate-900/80 backdrop-blur-xl rounded-2xl 
          border border-indigo-500/20 p-6 shadow-[0_0_40px_rgba(79,70,229,0.25)]">

          <h2 className="text-white text-lg font-semibold mb-4">
            ¿Qué quieres generar?
          </h2>

          <div className="flex flex-col gap-3">
            {CONTENT_TYPES.map((type) => (
              <button
                key={type.id}
                onClick={() => setContentType(type.id)}
                className={`flex items-center gap-3 px-4 py-4 rounded-xl text-sm font-medium
                  border transition-all
                  ${
                    contentType === type.id
                      ? "bg-indigo-600/30 border-indigo-400 text-white"
                      : "bg-slate-950/60 border-white/10 text-white hover:bg-slate-800/60"
                  }`}
              >
                <span className="text-lg">{type.icon}</span>
                {type.label}
              </button>
            ))}
          </div>

          {contentType && (
            <div className="mt-6 space-y-3">
              <input
                placeholder="Tema"
                className="w-full rounded-lg bg-slate-950/60 border border-white/10 px-4 py-2 text-white"
                value={topic}
                onChange={(e) => setTopic(e.target.value)}
              />

              <input
                placeholder="Audiencia"
                className="w-full rounded-lg bg-slate-950/60 border border-white/10 px-4 py-2 text-white"
                value={audience}
                onChange={(e) => setAudience(e.target.value)}
              />

              <input
                placeholder="Tono"
                className="w-full rounded-lg bg-slate-950/60 border border-white/10 px-4 py-2 text-white"
                value={tone}
                onChange={(e) => setTone(e.target.value)}
              />

              <button
                onClick={handleGenerate}
                disabled={loading}
                className="w-full py-3 rounded-xl bg-indigo-600 text-white"
              >
                {loading ? "Generando..." : "✨ Generar contenido"}
              </button>
            </div>
          )}
        </div>

        {/* PANEL DERECHO */}
        <div className="col-span-8 bg-slate-900/80 backdrop-blur-xl rounded-2xl 
          border border-indigo-500/20 p-8 relative overflow-hidden">

          {!result && (
            <div className="relative z-10 text-center">
              <div className="w-20 h-20 mx-auto mb-6 rounded-2xl 
                bg-indigo-600/30 flex items-center justify-center">
                <FiEdit3 className="text-indigo-300 w-10 h-10" />
              </div>

              <h3 className="text-white text-2xl font-semibold mb-2">
                Comienza a crear
              </h3>

              <p className="text-white/60 max-w-md mx-auto mb-6">
                Selecciona un tipo de contenido y rellena los campos
              </p>

              {/* 👇 LOS 4 CUADRADITOS */}
              <div className="grid grid-cols-2 gap-3 max-w-md mx-auto text-sm">
                <span className="bg-indigo-600/30 text-white py-2 rounded-lg">✓ Multi-plataforma</span>
                <span className="bg-violet-600/30 text-white py-2 rounded-lg">✓ Personalizable</span>
                <span className="bg-blue-600/30 text-white py-2 rounded-lg">✓ Varios modelos</span>
                <span className="bg-cyan-600/30 text-white py-2 rounded-lg">✓ IA Avanzada</span>
              </div>
            </div>
          )}

          {result && (
            <div className="relative z-10 h-full overflow-y-auto pr-2">
              <div className="bg-slate-950/60 rounded-xl p-6 text-white mb-4 max-w-full markdown-body">
                <ReactMarkdown remarkPlugins={[remarkGfm]} className="prose break-words">
                  {result.content}
                </ReactMarkdown>
              </div>

              {!result.image_url && (
                <button
                  onClick={handleCheckImage}
                  disabled={checkingImage}
                  className="px-4 py-2 rounded-lg bg-indigo-600 text-white"
                >
                  {checkingImage ? "Buscando imagen..." : "🖼️ Ver imagen"}
                </button>
              )}

              {result.image_url && (
                <img
                  src={`http://localhost:8000${result.image_url}`}
                  className="rounded-xl mt-4 border border-white/10 max-w-full"
                  alt="Imagen generada"
                />
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Home;
