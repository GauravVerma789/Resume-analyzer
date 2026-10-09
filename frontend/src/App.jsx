import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const API_URL = "http://127.0.0.1:8000";

  async function handleSubmit(e) {
    e.preventDefault();

    if (!file || !jobDescription.trim()) {
      alert("Please upload a PDF and enter a job description.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    try {
      const response = await fetch(`${API_URL}/upload-resume`, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("API request failed:", error);
    }
  }

  return (
    <main className="app">
      <h1>AI Resume Analyzer</h1>
      <p>Compare your resume with a job description.</p>

      <form onSubmit={handleSubmit}>
        <label htmlFor="resume">Upload Resume (PDF)</label>
        <input
          id="resume"
          type="file"
          accept=".pdf,application/pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <label htmlFor="jobDescription">Job Description</label>
        <textarea
          id="jobDescription"
          rows="8"
          placeholder="Paste the job description here..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        />

        <button type="submit">Analyze Resume</button>
      </form>

      {result && (
        <section className="results">
          <h2>Analysis Results</h2>

          <div className="score-card">
            <p className="score-label">RESUME MATCH SCORE</p>
            <div className="score-value">{result.match_percentage}%</div>
            <p className="score-caption">Match based on detected skills</p>
          </div>

          <h3>Matched Skills</h3>
          <ul>
            {result.matched_skills.map((skill) => (
              <li key={skill}>{skill}</li>
            ))}
          </ul>

          <h3>Missing Skills</h3>
          <ul>
            {result.missing_skills.map((skill) => (
              <li key={skill}>{skill}</li>
            ))}
          </ul>
        </section>
      )}
    </main>
  );
}

export default App;
