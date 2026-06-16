import type {
  WorkflowRequest,
  WorkflowResponse
} from "../types/workflow";

const API_URL =
  "http://localhost:8000/api/workflow/analyze";

/**
 * Call backend workflow endpoint
 */
export async function analyzeWorkflow(
  request: WorkflowRequest
): Promise<WorkflowResponse> {

  const response = await fetch(
    API_URL,
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify(request)
    }
  );

  if (!response.ok) {
    throw new Error(
      "Failed to analyze request."
    );
  }

  return response.json();
}