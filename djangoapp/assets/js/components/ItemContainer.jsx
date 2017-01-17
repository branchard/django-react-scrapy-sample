import React from 'react';

import Item from './Item';



class ItemContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            products: null
        };
    }

    componentDidMount() {
        let that = this;

        fetch('/api/0.1/components/' + this.props.itemObj.apiName, {
        	method: 'get'
        }).then(function(response) {
            response.json().then(function(data){
                //console.log(data);
                setTimeout(function(){
                    that.setState({
                        products: data.results
                    })
                }, 900);
            });
        }).catch(function(err) {
        	console.log(err);
        });
    }

    render() {
        return (
            <Item id={this.props.id} name={this.props.itemObj.displayedName} collumns={this.props.itemObj.collumns} onOpeningToogle={this.props.onOpeningToogle} open={this.props.open} products={this.state.products} />
        );
    }
}

export default ItemContainer;
