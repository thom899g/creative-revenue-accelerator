from typing import Dict, Any
import logging
import requests

class MarketplaceConnector:
    def __init__(self):
        self.base_url = "https://api.marketplace.com"

    def upload_asset(self, asset_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Upload an asset to the marketplace."""
        try:
            response = requests.post(f"{self.base_url}/assets/{asset_id}", json=data)
            if response.status_code == 200:
                logging.info(f"Asset {asset_id} uploaded successfully")
                return {"status": "success", "message": "Asset uploaded"}
            else:
                logging.error(f"Failed to upload asset {asset_id}: {response.text}")
                return {"status": "error", "error": response.text}
        except Exception as e:
            logging.error(f"Connection error while uploading asset {asset_id}: {str(e)}")
            return {"status": "error", "error": str(e)}

    def get_asset_sales(self, asset_id: str) -> Dict[str, Any]:
        """Get sales data for an asset."""
        try:
            response = requests.get(f"{self.base_url}/assets/{asset_id}/sales")
            if response.status_code == 200:
                return {"status": "success", "data": response.json()}
            else:
                logging.error(f"Failed to get sales data for {asset_id}: {response.text}")
                return {"status": "error", "error": response.text}
        except Exception as e:
            logging.error(f"Connection error while fetching sales data: {str(e)}")
            return {"status": "error", "error": str(e)}