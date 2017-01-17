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

        fetch('https://baconipsum.com/api/?type=meat-and-filler', {
        	method: 'get'
        }).then(function(response) {
            response.json().then(function(data){
                //console.log(data);
                setTimeout(function(){
                    that.setState({
                        products: data
                    })
                }, 4000);
            });
        }).catch(function(err) {
        	console.log(err);
        });
    }

    render() {
        return (
            <Item id={this.props.id} itemObj={this.props.itemObj} onOpeningToogle={this.props.onOpeningToogle} open={this.props.open} products={this.state.products} />
        );
    }
}

export default ItemContainer;
