/* Import styles */
import "bootstrap-webpack";
import "./../less/base.less";

import React from 'react';
import ReactDOM from 'react-dom';

/* Components */
import App from "./App";

ReactDOM.render(<App />, document.getElementById('container'))
