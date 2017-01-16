import React from 'react';

class ItemList extends React.Component {
    constructor(props) {
        super(props);
        this.openingToogleHandler = this.openingToogleHandler.bind(this);
    }

    openingToogleHandler(event) {
        event.preventDefault();
        this.props.onOpeningToogle(this.props.id, this.props.open);
    }

    render() {
        const open = this.props.open;
        let selectMenu = null;
        if(open){
            selectMenu = (
                <div className="frame row item-menu">
                    <p>Ouvert !!!!</p>
                </div>
            )
        }
        return (
            <article className={"item" + (open ? " item-opened" : "")}>
                <div className="frame item-top row" onClick={this.openingToogleHandler}>
                    <div className="item-type col-sm-3">
                        <h3 className="item-type-name">
                            <span className="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>{this.props.itemObj.displayedName}</h3>
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
