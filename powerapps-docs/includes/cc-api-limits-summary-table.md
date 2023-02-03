|Service Protection limits |Power Platform Request (API Entitlement) limits|
|---------|---------|
|Immediately return [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) when limits are exceeded. | Enforced for Power Automate flows but will have provisions for occasional overages on Dataverse, when enforced|
|Evaluated in a 5-minute sliding window.|Evaluated in a 24-hour period.|
|Applies to all external requests to Dataverse web services.|Applies to all compute operations and analytics originating from internal or external requests.|
|Developer is responsible for avoiding conditions that can cause errors and managing retry when they occur.|Administrator is responsible to manage assigned capacity. They can purchase capacity add-ons to increase limits.|
|Enforced today within the product.|- Will be enforced after preview report, available today for administrators to track and estimate usage, is made generally available.<br />-Preview reports are available now.|
|More information: [https://aka.ms/serviceprotectionlimits ](https://aka.ms/serviceprotectionlimits )|More information: [https://aka.ms/PlatformLimits](https://aka.ms/PlatformLimits)|
