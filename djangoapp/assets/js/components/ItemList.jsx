import React from 'react';
import ItemContainer from './ItemContainer';

const ITEM_TYPES = [
    {
        displayedName: "Boitier",
        apiName: "cases",
        collumns: [
            {
                displayedName: "Article",
                apiName: "name"
            },
            {
                displayedName: "Poids (Kg)",
                apiName: "weight"
            },
            {
                displayedName: "Type d'alimentation",
                apiName: "powerSupplyFormFactor.name"
            },
            {
                displayedName: "Marque",
                apiName: "brand.name"
            }

        ]
    },
    {
        displayedName: "Processeur",
        apiName: "processors",
        collumns: [
            {
                displayedName: "Article",
                apiName: "name"
            },
            {
                displayedName: "Nombre de coeurs",
                apiName: "cores"
            },
            {
                displayedName: "Socket",
                apiName: "socket.name"
            },
            {
                displayedName: "Marque",
                apiName: "brand.name"
            }

        ]
    },
    {
        displayedName: "Carte mère",
        apiName: "motherboards",
        collumns: [
            {
                displayedName: "Article",
                apiName: "name"
            },
            {
                displayedName: "Socket",
                apiName: "socket.name"
            },
            {
                displayedName: "Marque",
                apiName: "brand.name"
            }

        ]
    },
    {
        displayedName: "Mémoire",
        apiName: "rams",
        collumns: [
            {
                displayedName: "Article",
                apiName: "name"
            },
            {
                displayedName: "Type",
                apiName: "ramtype.typeName"
            },
            {
                displayedName: "Capacité (Go)",
                apiName: "capacity"
            },
            {
                displayedName: "Marque",
                apiName: "brand.name"
            }

        ]
    },
    {
        displayedName: "Carte graphique",
        apiName: "graphiccards",
        collumns: [
            {
                displayedName: "Article",
                apiName: "name"
            },
            {
                displayedName: "Memoire (Mo)",
                apiName: "memory"
            },
            {
                displayedName: "Type",
                apiName: "pcitype.name"
            },
            {
                displayedName: "Marque",
                apiName: "brand.name"
            }

        ]
    },
    {
        displayedName: "Disque Dur",
        apiName: "harddrives",
        collumns: [
            {
                displayedName: "Article",
                apiName: "name"
            },
            {
                displayedName: "Capacité (Go)",
                apiName: "capacity"
            },
            {
                displayedName: "Type",
                apiName: "hardDriveType.name"
            },
            {
                displayedName: "Marque",
                apiName: "brand.name"
            }

        ]
    },
    {
        displayedName: "Alimentation",
        apiName: "powersupplies",
        collumns: [
            {
                displayedName: "Article",
                apiName: "name"
            },
            {
                displayedName: "Puissance",
                apiName: "watts"
            },
            {
                displayedName: "Format",
                apiName: "factorForm.name"
            },
            {
                displayedName: "Marque",
                apiName: "brand.name"
            }

        ]
    }
];

class ItemList extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            openItemId: null,
            prices: {}
        };
        this.handleItemOpeningToogle = this.handleItemOpeningToogle.bind(this);
        this.handlePriceChanging = this.handlePriceChanging.bind(this);
    }

    handleItemOpeningToogle(id, alreadyOpen) {
        this.setState({
            openItemId: alreadyOpen ? null : id
        });
    }

    handlePriceChanging(id, price) {
        this.setState({
            prices: {id: price}
        });
    }

    render() {
        let itemsComponents = [];
        ITEM_TYPES.forEach(function(item, id) {
            itemsComponents.push(
                <ItemContainer key={id} id={id} itemObj={item} onPriceChanging={this.handlePriceChanging} onOpeningToogle={this.handleItemOpeningToogle} open={id == this.state.openItemId} />
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
