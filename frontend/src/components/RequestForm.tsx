interface Props {
  value: string;

  onChange: (
    value: string
  ) => void;

  onSubmit: () => void;

  loading: boolean;
}

export default function RequestForm(
  props: Props
) {
  return (
    <div>

      <h2>
        Healthcare Request
      </h2>

      <textarea
        rows={6}
        value={props.value}
        onChange={(e) =>
          props.onChange(
            e.target.value
          )
        }
        placeholder="Describe your healthcare request..."
      />

      <br />

      <button
        onClick={props.onSubmit}
        disabled={props.loading}
      >
        {
          props.loading
            ? "Analyzing..."
            : "Analyze Request"
        }
      </button>

    </div>
  );
}