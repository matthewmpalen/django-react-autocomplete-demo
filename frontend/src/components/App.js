import React from "react";
import DOM from "react-dom";
import AutoCompleteField from "./AutoCompleteField";

const App = () => (
    <AutoCompleteField endpoint="/api/locations/" />
);

DOM.render(<App />, document.getElementById("app"));