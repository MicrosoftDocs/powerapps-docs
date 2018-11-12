## Mapping functions for Dynamics 365 Customer Engagement Plan 
 Field Service and Project Service Automation have key functions that rely on location. For example, the location of Service Accounts (which define where services or tasks take place) or the starting/ending location of Resources (people performing services or tasks).  In order for the system to show these on a map - or to calculate distances between points - it's necessary to use a mapping service (in this case Bing Maps).  
  
 Following is the workflow to and from the Bing Maps service:  
  
|From Dynamics 365|Bing Maps returns|Note|  
|-----------------------|-----------------------|----------|  
|Address (account or resource)|Latitude and longitude of the address (location)|This is referred to as "geo-coding" of an address.|  
|Set of locations (latitude/longitude)|Distance between locations|This can be used to find optimal routes for resources or to calculate travel times.|  
|Set of locations (latitude/longitude)|Map view with the locations as pins on the map|This is used to view the accounts and resources in a map view.|  
  
> [!NOTE]
>  Aside from the data referenced above, no other data is sent to the Bing Maps service.
