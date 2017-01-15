import React from 'react';
import Item from './Item';

const ITEM_TYPES = [
    {
        displayedName: "Boitier",
        apiName: "case"
    },
    {
        displayedName: "Processeur",
        apiName: "processor"
    },
    {
        displayedName: "Carte mère",
        apiName: "motherboard"
    },
    {
        displayedName: "Mémoire",
        apiName: "ram"
    },
    {
        displayedName: "Carte graphique",
        apiName: "graphique_card"
    },
    {
        displayedName: "Disque Dur",
        apiName: "storage"
    },
    {
        displayedName: "Alimentation",
        apiName: "power_supply"
    }
];

class ItemList extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            openItemId: null
        };
        this.handleItemOpeningToogle = this.handleItemOpeningToogle.bind(this);
    }

    handleItemOpeningToogle(id, alreadyOpen) {
        this.setState({
            openItemId: alreadyOpen ? null : id
        });
    }

    render() {
        let itemsComponents = [];
        ITEM_TYPES.forEach(function(item, id) {
            itemsComponents.push(
                <Item key={id} id={id} itemObj={item} onOpeningToogle={this.handleItemOpeningToogle} open={id == this.state.openItemId} />
            );
        }.bind(this));


        return (
            <div>
                <div className="container-fluid">
                    <h2>Les composants</h2>
                    <hr/>
                    <div className="item-list">
                        {itemsComponents}
                    </div>
                </div>
                <footer className="total">
                    <div className="container-fluid">
                        <span className="price-label">Prix total:</span><span className="price label label-danger">600.00 €</span>
                    </div>
                </footer>
            </div>
        );
    }
}

export default ItemList;
