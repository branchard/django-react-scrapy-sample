import React from 'react';
import Item from './Item';



class ItemContainer extends React.Component {
    render() {
        return (
            <Item id={this.props.id} itemObj={this.props.itemObj} onOpeningToogle={this.props.onOpeningToogle} open={this.props.open} />
        );
    }
}

export default ItemContainer;
