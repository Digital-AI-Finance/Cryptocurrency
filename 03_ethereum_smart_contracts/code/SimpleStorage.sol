// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SimpleStorage {
    uint256 private storedValue;

    event ValueChanged(uint256 indexed oldValue, uint256 indexed newValue, address indexed setter);
    event ValueRetrieved(uint256 value, address indexed retriever);

    constructor() {
        storedValue = 0;
    }

    function setValue(uint256 newValue) public {
        uint256 oldValue = storedValue;
        storedValue = newValue;
        emit ValueChanged(oldValue, newValue, msg.sender);
    }

    function getValue() public returns (uint256) {
        emit ValueRetrieved(storedValue, msg.sender);
        return storedValue;
    }

    function getValueView() public view returns (uint256) {
        return storedValue;
    }
}
