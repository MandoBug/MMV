import { useEffect, useState } from 'react'
import Plot from 'react-plotly.js'

function App() {
  const [bins, setBins] = useState<number[]>([])
  const [edges, setEdges] = useState<number[]>([])

  useEffect(() => {
    const go = async () => {
      const res = await fetch('/api/histogram', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({ n: 800 })
      })
      const data = await res.json()
      setBins(data.bins)
      setEdges(data.edges)
    }
    go()
  }, [])

  const centers = edges.length > 1
    ? edges.slice(0, -1).map((e, i) => (e + edges[i+1]) / 2)
    : []

  return (
    <div style={{padding: 24}}>
      <h1>Molecular Motion Visualizer (MMV) — Scaffold</h1>
      <p>Backend health should be <code>/api/health</code> = ok.</p>
      <Plot
        data={[{ x: centers, y: bins, type: 'bar' }]}
        layout={{ title: 'Demo Speed Histogram' }}
        style={{width: '100%', height: 500}}
      />
    </div>
  )
}

export default App
