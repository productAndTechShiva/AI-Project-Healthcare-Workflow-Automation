/**
 * API request
 */
export interface WorkflowRequest {
  message: string;
}

/**
 * Extracted entities
 */
export interface ExtractedEntities {
  symptoms: string[];
  medications: string[];
  specialty: string | null;
  issue_type: string | null;
}

/**
 * API response
 */
export interface WorkflowResponse {
  request_type: string;

  entities: ExtractedEntities;

  priority: string;

  decision: string;

  department: string;

  queue_name: string;

  ticket_id: string;

  ticket_summary: string;

  explanation: string;

  timeline: string[];
}