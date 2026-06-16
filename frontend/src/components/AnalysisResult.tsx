import type { WorkflowResponse } from "../types/workflow";

import Timeline from "./Timeline";

interface Props {
  result: WorkflowResponse;
}

/**
 * Returns CSS class based on priority.
 */
function getPriorityClass(priority: string): string {
  switch (priority.toLowerCase()) {
    case "critical":
      return "priority-critical";

    case "high":
      return "priority-high";

    case "medium":
      return "priority-medium";

    case "low":
      return "priority-low";

    default:
      return "";
  }
}

export default function AnalysisResult(props: Props) {
  const result = props.result;

  return (
    <div>
      <h2 className="section-title">Analysis Result</h2>

      <p>
        <strong>Request Type:</strong> {result.request_type}
      </p>

      {/* <p>
        <strong>Priority:</strong> {result.priority}
      </p> */}

      <p>
        <strong>Priority:</strong>{" "}
        <span className={getPriorityClass(result.priority)}>
          {result.priority}
        </span>
      </p>

      <p>
        <strong>Decision:</strong> {result.decision}
      </p>

      <p>
        <strong>Department:</strong> {result.department}
      </p>
      <p>
        <strong>Queue Name:</strong> {result.queue_name}
      </p>

      <p>
        <strong>Ticket ID:</strong> {result.ticket_id}
      </p>

      <p>
        <strong>Ticket Summary:</strong> {result.ticket_summary}
      </p>

      <p>
        <strong>Explanation:</strong> {result.explanation}
      </p>

      <hr />

      <h3>Extracted Information</h3>

      <p>
        <strong>Symptoms:</strong>
      </p>

      <ul>
        {result.entities.symptoms.length > 0 ? (
          result.entities.symptoms.map((symptom, index) => (
            <li key={index}>{symptom}</li>
          ))
        ) : (
          <li>None</li>
        )}
      </ul>

      <p>
        <strong>Medications:</strong>
      </p>

      <ul>
        {result.entities.medications.length > 0 ? (
          result.entities.medications.map((medication, index) => (
            <li key={index}>{medication}</li>
          ))
        ) : (
          <li>None</li>
        )}
      </ul>

      <p>
        <strong>Specialty:</strong> {result.entities.specialty ?? "None"}
      </p>

      <p>
        <strong>Issue Type:</strong> {result.entities.issue_type ?? "None"}
      </p>

      <hr />

      <Timeline steps={result.timeline} />
    </div>
  );
}
