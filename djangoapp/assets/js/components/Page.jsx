import React from 'react';

import Navbar from './Navbar';
import Header from './Header';
import ItemList from './ItemList';
import Footer from './Footer';

class Page extends React.Component {
    render() {
        return (
            <div className="">
                <Navbar />
                <main className="">
                    <section className="container-fluid">
                        <Header />
                    </section>
                    <section className="hardware-list">
                        <ItemList />
                    </section>
                </main>
                <Footer />
            </div>
        );
    }
}

export default Page;
