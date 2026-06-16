interface Props {
  steps: string[];
}

export default function Timeline(
  props: Props
) {
  return (
    <div>

      <h3>
        Workflow Timeline
      </h3>

      <ul className="timeline-list">

        {props.steps.map(
          (
            step,
            index
          ) => (
            <li key={index}>
              {step}
            </li>
          )
        )}

      </ul>

    </div>
  );
}