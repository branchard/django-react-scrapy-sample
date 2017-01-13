import React from 'react';
import Item from './Item';

const ITEM_TYPES = [
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
        apiName: "graphiquecard"
    }
];

class ItemList extends React.Component {

    constructor(props) {
        super(props);
    }

    handleItemChange = (event) => {
        console.log("item changed");
    };

    render() {
        let itemsComponents = [];
        ITEM_TYPES.forEach(function(item, id) {
            console.log(item.displayedName);
            itemsComponents.push(
                <Item key={id} itemObj={item} />
            );
        });


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
