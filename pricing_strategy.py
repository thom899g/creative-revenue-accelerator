from typing import Dict, Any
import logging

class DynamicPricingStrategy:
    def __init__(self):
        self.prices = {}

    def set_price(self, asset_id: str, price: float) -> Dict[str, Any]:
        """Set the price for a specific asset."""
        try:
            self.prices[asset_id] = price
            logging.info(f"Price updated for asset {asset_id} to ${price}")
            return {"status": "success", "message": f"Price set to ${price}"}
        except Exception as e:
            logging.error(f"Failed to set price for asset {asset_id}: {str(e)}")
            return {"status": "error", "error": str(e)}

    def get_price(self, asset_id: str) -> Dict[str, Any]:
        """Get the current price of an asset."""
        try:
            if asset_id in self.prices:
                return {"status": "success", "price": self.prices[asset_id]}
            else:
                logging.warning(f"Asset {asset_id} not found")
                return {"status": "warning", "message": f"Asset {asset_id} not found"}
        except Exception as e:
            logging.error(f"Failed to get price for asset {asset_id}: {str(e)}")
            return {"status": "error", "error": str(e)}