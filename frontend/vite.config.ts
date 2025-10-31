import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    // Optional proxy — makes frontend API calls go to Flask in dev
    proxy: {
      "/api": "http://127.0.0.1:5000"
    }
  }
});

/*
purpose: Vite configuration
- enables the React plugin
- sets up a dev proxy so requests to /api hit Flask automatically

this file is just Vite’s build + dev server config.
inside we define the React plugin and optionally route /api calls to Flask.
*/
