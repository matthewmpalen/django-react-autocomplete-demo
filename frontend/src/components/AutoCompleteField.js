import React, { Component } from "react";
import PropTypes from "prop-types";
import Autocomplete from "react-autocomplete"

class AutoCompleteField extends Component {
    constructor (props) {
        super(props)
        this.state = {
            locations: [],
            loaded: false,
            value: ''
        }
    }

    static propTypes = {
        endpoint: PropTypes.string.isRequired
    };

    componentDidMount() {
        fetch(this.props.endpoint)
            .then(response => {
                if (response.status !== 200) {
                    return this.setState({ placeholder: "Something went wrong" });
                }
                return response.json();
            })
            .then(data => this.setState({ locations: data, loaded: true }));
    }

    render() {
        return (
            <React.Fragment>
                <label htmlFor="location-autocomplete">Search for Location</label><br/>
                <Autocomplete
                    inputProps={{ id: 'location-autocomplete' }}
                    wrapperStyle={{ position: 'relative', display: 'inline-block' }}
                    value={this.state.value}
                    items={this.state.locations}
                    getItemValue={(item) => item.full_name}
                    shouldItemRender={(item, value) => item.full_name.toLowerCase().indexOf(value.toLowerCase()) > -1}
                    onSelect={(value, item) => {
                        this.setState({ value });
                    }}
                    onChange={(event, value) => {
                        this.setState({ value });
                    }}
                    renderMenu={children => (
                        <div className="menu">
                            {children}
                        </div>
                    )}
                    renderItem={(item, isHighlighted) => (
                        <div className={`item ${isHighlighted ? 'item-highlighted' : ''}`} key={item.id}>
                            {item.full_name}
                        </div>
                    )}
                />
            </React.Fragment>
        )
    }
}

export default AutoCompleteField;
