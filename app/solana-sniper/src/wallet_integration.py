import os
import logging
from dotenv import load_dotenv
from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction

# Load environment variables
load_dotenv()

class Wallet:
    def __init__(self):
        self.client = Client(os.getenv("SOLANA_RPC_URL"))
        self.private_key = self._validate_private_key(os.getenv("PRIVATE_KEY"))

    def _validate_private_key(self, private_key):
        """Validate Solana private key."""
        if not private_key or len(private_key) != 88:  # Example length for Solana private key
            raise ValueError("Invalid private key")
        return private_key

    def execute_transaction(self, token_address, amount):
        """Execute a Solana transaction to buy tokens."""
        try:
            transaction = Transaction()
            transaction.add(
                transfer(
                    TransferParams(
                        from_pubkey=PublicKey(self.private_key),
                        to_pubkey=PublicKey(token_address),
                        lamports=amount,
                    )
                )
            )
            response = self.client.send_transaction(transaction)
            return response["result"]
        except Exception as e:
            logging.error(f"Transaction failed: {e}")
            raise