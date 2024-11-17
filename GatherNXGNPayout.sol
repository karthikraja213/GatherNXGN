// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GatherNXGNPayout {
    address public owner;
    uint256 public payoutAmount;

    
    constructor() {
        owner = msg.sender;
        payoutAmount = 0.002 ether; // Define the payout amount (in wei)
    }

    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this function");
        _;
    }

    
    function setPayoutAmount(uint256 _amount) external onlyOwner {
        payoutAmount = _amount;
    }

        
    function submitAccessToken(address payable _userAddress) external payable {
        require(address(this).balance >= payoutAmount, "Insufficient contract balance");
        require(_userAddress != address(0), "Invalid address");

        // Transfer the payout amount to the user address using transfer
        _userAddress.transfer(payoutAmount);
    }

    
    receive() external payable {}
}

