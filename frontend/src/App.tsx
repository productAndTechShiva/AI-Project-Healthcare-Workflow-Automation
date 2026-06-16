import { useState } from "react";

import RequestForm from "./components/RequestForm";
import AnalysisResult from "./components/AnalysisResult";

import { analyzeWorkflow } from "./api/workflowApi";

import type { WorkflowResponse } from "./types/workflow";
import SampleRequests from "./components/SampleRequests";

function App() {
  const [message, setMessage] = useState("");

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const [result, setResult] = useState<WorkflowResponse | null>(null);

  /**
   * Submit request to backend
   */
  const handleAnalyze = async () => {
    if (!message.trim()) {
      setError("Please enter a request.");

      return;
    }

    try {
      setLoading(true);

      setError("");

      setResult(null);

      const response = await analyzeWorkflow({
        message,
      });

      setResult(response);
    } catch (_error) {
      setError("Failed to analyze request.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1 className="page-title">
        AI Healthcare Workflow Automation Assistant
      </h1>

      <div className="card">
        <SampleRequests onSelect={setMessage} />

        <hr />

        <RequestForm
          value={message}
          onChange={setMessage}
          onSubmit={handleAnalyze}
          loading={loading}
        />

        {error && <p className="error-message">{error}</p>}
      </div>

      {result && (
        <div className="card">
          <AnalysisResult result={result} />
        </div>
      )}
    </div>
  );
}

export default App;
