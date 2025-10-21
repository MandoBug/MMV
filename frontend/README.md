# Molecular Motion Visualizer (MMV)

**Real-time visualization of gas molecules** obeying kinetic theory with live speed histograms and a Maxwell–Boltzmann overlay.  
Built by **Mando & Isaac** — Python (Flask + NumPy) backend, React + Plotly frontend.

## ✨ Features (MVP)
- 2D box with N particles (positions/velocities in NumPy)
- Wall bounces (specular)
- Live speed histogram (+ MB overlay)
- Temperature/energy readouts
- Start/Pause/Reset controls

## 🧠 Roadmap
- Particle–particle elastic collisions (equal mass)
- Spatial hashing (cell lists) for O(N) neighbor checks
- Equilibrium detector (KS/EMD distance badge)
- Exports (PNG/GIF/CSV), “hot corner” heater

## 🛠 Tech
- **Frontend:** React (Vite) + TypeScript + Plotly
- **Backend:** Flask + NumPy
- **Dev:** Node 18+, Python 3.10+


