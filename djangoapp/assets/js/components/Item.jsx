import React from 'react';

import Spinner from "./Spinner";

const ITEMS_COLUMNS = {
    "processor": {
        rows: [
            "Article",

        ]
    }
}

class ItemList extends React.Component {
    constructor(props) {
        super(props);
        this.openingToogleHandler = this.openingToogleHandler.bind(this);
        this.renderProductsTable = this.renderProductsTable.bind(this);
    }

    openingToogleHandler(event) {
        event.preventDefault();
        this.props.onOpeningToogle(this.props.id, this.props.open);
    }

    renderProductsTable(products) {
        return(
            <table>

            </table>
        );
    }

    render() {
        const open = this.props.open;
        let selectMenu = null;
        if(open){
            let productsDiv = null;
            if(this.props.products){
                let productsList = []
                this.props.products.forEach(function(product, key){
                    productsList.push(
                        <li key={key} >{product.name}</li>
                    );
                }.bind(this));
                productsDiv = (
                    <ul>
                        {productsList}
                    </ul>
                );
            }else{
                productsDiv = (
                    <Spinner />
                );
            }
            selectMenu = (
                <div className="frame row item-menu">
                    {productsDiv}
                </div>
            )
        }
        return (
            <article className={"item" + (open ? " item-opened" : "")}>
                <div className="frame item-top row" onClick={this.openingToogleHandler}>
                    <div className="item-type col-sm-3">
                        <h3 className="item-type-name">
                            <span className="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>{this.props.name}</h3>
                    </div>
                    <div className="right-countainer">
                        <div className="item-description">
                            <span className="item-label">Intel Core i5-6600K (3.5 GHz)</span>
                            <span className="item-descr">Processeur Socket 1151 - Quad Core - Cache 6 Mo - Skylake - Ventirad non inclus</span>
                            <span className="item-price">
                                <span className="label label-danger">259.90 €</span>
                            </span>
                        </div>
                        <div className="item-preview">
                            <img src="http://lorempicsum.com/simpsons/300/300/5"/>
                        </div>
                    </div>
                </div>
                {selectMenu}
            </article>
        );
    }
}

export default ItemList;
