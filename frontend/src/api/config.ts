// central place to build backend API URLs
// reads VITE_API_BASE from .env files (Vite injects it at build/dev time)

export const API_BASE =
  import.meta.env.VITE_API_BASE || "http://127.0.0.1:5000";

export const url = (p: string) => `${API_BASE}${p}`;

/*
purpose: API base configuration
- exposes API_BASE from env and a url() helper to build endpoints

this file is just the API URL builder.
inside we read VITE_API_BASE and concatenate paths like /api/snapshot.
*/
