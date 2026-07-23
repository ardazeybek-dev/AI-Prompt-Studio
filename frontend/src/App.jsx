import { useState } from "react"

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000"

export default function App() {
  const [text, setText] = useState("")
  const [result, setResult] = useState("")
  const [loading, setLoading] = useState(false)

  const handleGenerate = async () => {
    if (!text) return
    setLoading(true)
    try {
      const response = await fetch(`${API_URL}/api/generate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
      })
      const data = await response.json()
      setResult(data.prompt || "An error occurred")
    } catch (error) {
      setResult("Server connection error")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{ backgroundColor: "#121212", color: "#ffffff", minHeight: "100vh", padding: "40px", fontFamily: "sans-serif" }}>
      <div style={{ maxWidth: "800px", margin: "0 auto" }}>
        <h1 style={{ color: "#e67e22", textAlign: "center" }}>AI Prompt Studio 🚀</h1>
        <p style={{ textAlign: "center", color: "#aaa" }}>Turn your simple ideas into professional cinematic prompts</p>
        
        <div style={{ marginTop: "40px" }}>
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="e.g. A documentary scene about the history of Bergama..."
            style={{ width: "100%", height: "120px", padding: "15px", borderRadius: "8px", border: "1px solid #333", backgroundColor: "#1e1e1e", color: "#fff", fontSize: "16px", resize: "none", boxSizing: "border-box" }}
          />
          <button
            onClick={handleGenerate}
            disabled={loading}
            style={{ width: "100%", padding: "15px", marginTop: "15px", backgroundColor: "#e67e22", color: "#fff", border: "none", borderRadius: "8px", fontSize: "16px", fontWeight: "bold", cursor: "pointer" }}
          >
            {loading ? "AI is working..." : "✨ Generate Professional Prompt"}
          </button>
        </div>

        {result && (
          <div style={{ marginTop: "40px", padding: "20px", backgroundColor: "#1e1e1e", borderRadius: "8px", border: "1px solid #333" }}>
            <h3 style={{ color: "#e67e22", marginTop: 0 }}>Generated Prompt:</h3>
            <pre style={{ whiteSpace: "pre-wrap", wordBreak: "break-word", color: "#fff", fontFamily: "monospace", fontSize: "15px" }}>{result}</pre>
          </div>
        )}
      </div>
    </div>
  )
}
