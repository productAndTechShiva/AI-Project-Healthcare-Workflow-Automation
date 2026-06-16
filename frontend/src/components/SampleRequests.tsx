/**
 * Sample requests for quick testing.
 */

interface Props {
  onSelect: (request: string) => void;
}

const SAMPLE_REQUESTS = [
  "I have severe chest pain and difficulty breathing.",

  "I need an appointment with a cardiologist.",

  "I need a refill for my diabetes medication.",

  "Why was I charged twice for my recent visit?",

  "I need copies of my medical records."
];

export default function SampleRequests(
  props: Props
) {
  return (
    <div>

      <h3>
        Try Sample Requests
      </h3>

      <ul>

        {SAMPLE_REQUESTS.map(
          (request, index) => (
            <li
              key={index}
              className="sample-item"
              onClick={() =>
                props.onSelect(
                  request
                )
              }
            >
              {request}
            </li>
          )
        )}

      </ul>

    </div>
  );
}