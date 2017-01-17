import React from 'react';

import Spinner from "./Spinner";

class ItemList extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            currentSelectedItem: null, // must contain product
            currentHoveredItem: null // must contain product
        };

        this.onItemClick = this.onItemClick.bind(this);
        this.onItemHover = this.onItemHover.bind(this);
        this.onItemHoverLeave = this.onItemHoverLeave.bind(this);
        this.openingToogleHandler = this.openingToogleHandler.bind(this);
        this.renderProductsTable = this.renderProductsTable.bind(this);
    }

    onItemClick(product){
        this.setState({
            currentSelectedItem: product
        });
    }

    onItemHover(product){
        this.setState({
            currentHoveredItem: product
        });
    }

    onItemHoverLeave(){
        this.setState({
            currentHoveredItem: null
        });
    }

    openingToogleHandler(event) {
        event.preventDefault();
        this.props.onOpeningToogle(this.props.id, this.props.open);
    }

    renderProductsTable() {
        const that = this;

        let theadCollumns = [];
        this.props.collumns.forEach(function(collumn, key){
            theadCollumns.push(
                <th key={key} >
                    {collumn.displayedName}
                </th>
            )
        });

        let productsRows = [];
        this.props.products.forEach(function(row, key){
            let productCollumns = [];
            that.props.collumns.forEach(function(collumn, key){
                let _row;
                let regexExec = /^(.*)\.(.*)$/.exec(collumn.apiName);
                if(regexExec)
                {
                    _row = row[regexExec[1]][regexExec[2]];
                }else{
                    _row = row[collumn.apiName];
                }

                productCollumns.push(
                    <td key={key} onClick={() => that.onItemClick(row)} onMouseEnter={() => that.onItemHover(row)} onMouseLeave={that.onItemHoverLeave} >
                        {_row}
                    </td>
                );
            });
            productsRows.push(
                <tr key={key} className={row == that.state.currentSelectedItem ? "actived" : ""} >
                    {productCollumns}
                </tr>
            );
        });

        return(
            <div className="table-responsive">
                <table className="table table-bordered" >
                    <thead>
                        <tr>
                            {theadCollumns}
                        </tr>
                    </thead>
                    <tbody>
                        {productsRows}
                    </tbody>
                </table>
            </div>
        );
    }

    render() {
        const open = this.props.open;
        let selectMenu = null;
        if(open){
            let productsDiv = null;
            if(this.props.products){
                productsDiv = this.renderProductsTable();
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

        let currentSelectedItemDiv;
        if(this.state.currentSelectedItem || this.state.currentHoveredItem){
            let currentProduct = this.state.currentHoveredItem || this.state.currentSelectedItem;

            let img = null;

            if(currentProduct.img){
                img = <img src="http://lorempicsum.com/simpsons/300/300/5"/>;
            }

            currentSelectedItemDiv = (
                <div className="right-countainer">
                    <div className="item-description">
                        <span className="item-label">{currentProduct.name}</span>
                        <span className="item-descr">Processeur Socket 1151 - Quad Core - Cache 6 Mo - Skylake - Ventirad non inclus</span>
                        <span className="item-price">
                            <span className="label label-danger">259.90 €</span>
                        </span>
                    </div>
                    <div className={"item-preview " + (img ? "" : "no-img")}>
                        {img}
                    </div>
                </div>
            );
        }else{
            /* No Description */
            currentSelectedItemDiv = (
                <div className="right-countainer">
                    <div className="item-description">

                    </div>
                    <div className="item-preview">
                    </div>
                </div>
            );
        }

        return (
            <article className={"item" + (open ? " item-opened" : "")}>
                <div className="frame item-top row" onClick={this.openingToogleHandler}>
                    <div className="item-type col-sm-3">
                        <h3 className="item-type-name">
                            <span className="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>{this.props.name}</h3>
                    </div>
                    {currentSelectedItemDiv}
                </div>
                {selectMenu}
            </article>
        );
    }
}

export default ItemList;
