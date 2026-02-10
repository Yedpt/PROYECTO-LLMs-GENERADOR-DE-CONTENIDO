import React, { useEffect } from "react";

export default function ImageModal({ src, alt, open, onClose }) {
  useEffect(() => {
    if (!open) return;

    function onKey(e) {
      if (e.key === "Escape") onClose();
    }

    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open, onClose]);

  if (!open) return null;

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm"
      onClick={onClose}
      aria-modal="true"
      role="dialog"
    >
      <div
        className="relative max-w-4xl w-[90%] max-h-[90%] bg-transparent"
        onClick={(e) => e.stopPropagation()}
      >
        <button
          onClick={onClose}
          className="absolute -top-4 -right-4 bg-white/10 hover:bg-white/20 text-white rounded-full p-2 shadow-lg"
          aria-label="Cerrar imagen"
        >
          ✕
        </button>

        <div className="w-full h-full flex items-center justify-center">
          <img
            src={src}
            alt={alt || "Imagen generada"}
            className="max-h-[82vh] w-auto rounded-xl border border-white/10 shadow-2xl object-contain"
          />
        </div>

        <div className="mt-4 text-center text-sm text-white/80">
          <div>{alt}</div>
          <a
            href={src}
            download
            className="inline-block mt-2 px-3 py-2 bg-indigo-600 text-white rounded-lg shadow-md hover:opacity-90"
          >
            Descargar imagen
          </a>
        </div>
      </div>
    </div>
  );
}
