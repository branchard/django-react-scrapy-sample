import React from 'react';

class Navbar extends React.Component {
    render() {
        return (
            <nav className="navbar navbar-default ">
                <div className="container-fluid">
                    <div className="navbar-header">

                        <a className="navbar-brand" href="#">
                            <span className="glyphicon glyphicon-tasks" aria-hidden="true"></span>
                            Django-react-scrapy-sample
                        </a>
                    </div>
                </div>
            </nav>
        );
    }
}

export default Navbar;
