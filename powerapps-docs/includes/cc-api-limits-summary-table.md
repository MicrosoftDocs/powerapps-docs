|Service Protection limits |Power Platform Request (API Entitlement) limits|
|---------|---------|
|Immediately return [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) when limits are exceeded. |Will have allowances/tolerance for occasional and reasonable overages when enforcement begins.|
|Evaluated in a 5-minute sliding window.|Evaluated in a 24-hour period.|
|Applies to all external requests to Dataverse web services.|Applies to data operations on table rows originating from internal or external requests.|
|Developer is responsible for avoiding conditions that can cause errors and managing re-try when they occur.|Administrator is responsible to manage assigned capacity. They can purchase capacity add-ons to increase limits.|
|Enforced today within the product.|- Will be enforced after reports are available for administrators to track and estimate use are generally available.<br />-Preview reports are available now.|
|More information: [https://aka.ms/serviceprotectionlimits ](https://aka.ms/serviceprotectionlimits )|More information: [https://aka.ms/PlatformLimits ](https://aka.ms/PlatformLimits)|
