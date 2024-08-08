import "./confirmationModal.less";
import React from "react";
import "../../../css/theme.css";

/**
 * @component Comp1
 * Component for confirming changes to Bucket Sort decisions
 *
 * @param {object} props
 * @param {function} closeModal
 * @param {jsx} content
 */
function ConfirmationModal(props) {
  return (
    <React.Fragment>
      <div className="confirmation-background" onClick={props.closeModal} />
      <div className="confirmation-modal">{props.content}</div>
    </React.Fragment>
  );
}

export default ConfirmationModal;
