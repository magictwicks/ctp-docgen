import React, { useRef } from "react";
import { AiOutlineMail, AiOutlinePaperClip } from "react-icons/ai";
import "./errorButton.less";

/**
 * @component Comp2
 * Generate error button with options to send or copy error messages.
 */
function ErrorButton({ errors: errors }) {
  const errorForm = useRef();

  let errorsString = JSON.stringify(
    errors.map((error) => {
      if (error.response) {
        return {
          response: {
            data: error.response.data,
            status: error.response.status,
            headers: error.response.headers,
          },
          config: error.config,
        };
      } else if (error.request) {
        return {
          request: error.request,
          config: error.config,
        };
      } else {
        return {
          message: error.message,
          config: error.config,
        };
      }
    }),
  );

  return (
    <div className="error-notification">
      <p>{`Errors (${errors.length}) occured.`}</p>
      <p>Please refresh the page.</p>
      <p>Send an error report:</p>
      <form ref={errorForm} action="mailto:roman@kalaam.org" method="GET">
        <input
          name="subject"
          type="hidden"
          value="CTP - Contemporary Evaluations error report"
        />
        <input name="body" type="hidden" value={errorsString} />

        <a onClick={() => errorForm.current.submit()}>
          <AiOutlineMail />
        </a>
        <a onClick={() => navigator.clipboard.writeText(errorsString)}>
          <AiOutlinePaperClip />
        </a>
      </form>
    </div>
  );
}

export default ErrorButton;
