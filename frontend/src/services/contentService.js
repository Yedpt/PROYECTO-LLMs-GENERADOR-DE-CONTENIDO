import api from "./api";

/**
 * Genera contenido usando el backend IA
 */
export const generateContent = async ({
  topic,
  platform,
  audience,
  tone,
}) => {
  const response = await api.post("/api/generate", {
    tema: topic,
    plataforma: platform,
    audiencia: audience,
    tono: tone,
  });

  return response.data;
};
