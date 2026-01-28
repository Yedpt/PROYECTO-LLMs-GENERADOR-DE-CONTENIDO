export default function Nav() {
  return (
    <nav className="w-full px-8 py-4 flex items-center justify-between bg-black/20 backdrop-blur border-b border-white/10">
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 rounded-xl bg-linear-to-r from-purple-500 to-pink-500 flex items-center justify-center text-white text-xl shadow-lg">
          ✨
        </div>
        <div>
          <h1 className="text-lg font-bold text-white">
            Generador de Contenido IA
          </h1>
          <p className="text-xs text-white/60">
            Crea contenido increíble con IA
          </p>
        </div>
      </div>
    </nav>
  );
}
