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
        this.state = {
            openItemId: null
        };
        this.handleItemOpening = this.handleItemOpening.bind(this);
    }

    handleItemOpening(id) {
        this.setState({
            openItemId: id
        });
    }

    render() {
        let itemsComponents = [];
        let that = this;
        console.log("rendering");
        ITEM_TYPES.forEach(function(item, id) {
            itemsComponents.push(
                <Item key={id} id={id} itemObj={item} onOpening={that.handleItemOpening} open={id == that.state.openItemId} />
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
