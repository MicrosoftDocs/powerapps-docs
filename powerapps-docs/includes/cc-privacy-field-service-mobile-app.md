By installing and using the [!INCLUDE[pn_fieldservice_mobile_app_long](pn-fieldservice-mobile-app-long.md)] mobile app on a mobile device, users consent to transmission of user organization's assigned ID and assigned end user ID, and device ID to Microsoft and Resco.net, Inc. for purposes of providing the services and verifying that the software is properly licensed.  
&nbsp;<br />
If users use the [!INCLUDE[pn_fieldservice_mobile_app_long](pn-fieldservice-mobile-app-long.md)] mobile app to connect [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] with [!include[](../includes/tn-glympse.md)] Services, by installing or using the software, users consent to transmission of Customer Data to [!include[](../includes/tn-glympse.md)] for purposes of enabling real-time location based services. This feature requires that an authorized user or administrator integrate and configure organization's existing [!include[](../includes/tn-glympse.md)] account to work with [!include[](../includes/pn-dynamics-crm.md)]. Use of [!include[](../includes/tn-glympse.md)] Services is subject to the terms and privacy statement that apply to your [!include[](../includes/tn-glympse.md)] account.  
&nbsp;<br />
If users use the App to connect to [!include[](../includes/pn-microsoft-dynamics.md)] CRM (online) or [!include[](../includes/pn-crm-online.md)], by installing the App, users consent to transmission of their organization's assigned ID and assigned end user ID, and device ID to Microsoft for purposes of enabling connections across multiple devices, or improving [!include[](../includes/pn-microsoft-dynamics.md)] CRM (online), [!include[](../includes/pn-crm-online.md)] or the App.  
&nbsp;<br />
**Location data.** If users request and enable location-based services or features in the App, the App may collect and use precise data about their location. Precise location data can be Global Position System (GPS) data, as well as data identifying nearby cell towers and Wi-Fi hotspots. The App may send location data to [!include[](../includes/pn-microsoft-dynamics.md)] CRM or [!include[](../includes/pn-dynamics-crm.md)]. The App may send the location data to [!include[](../includes/pn-bing-maps.md)] and other third party mapping services, such as Google Maps and [!include[](../includes/tn-apple.md)] Maps, a user designated in the user's phone to process the user's location data within the App. Users may disable location-based services or features or disable the App's access to user's location by turning off the location service or turning off the App's access to the location service. Users' use of [!include[](../includes/pn-bing-maps.md)] is governed by the [!include[](../includes/pn-bing-maps.md)] End User Terms of Use available at [https://go.microsoft.com/?linkid=9710837](https://go.microsoft.com/?linkid=9710837) and the [!include[](../includes/pn-bing-maps.md)] Privacy Statement available at [https://go.microsoft.com/fwlink/?LinkID=248686](https://go.microsoft.com/fwlink/?LinkID=248686). Users' use of third party mapping services, and any information users provide to them, is governed by their service specific end user terms and privacy statements. Users should carefully review these other end user terms and privacy statements.  
&nbsp;<br />
The App may include links to other Microsoft services and third party services whose privacy and security practices may differ from those of [!include[](../includes/pn-microsoft-dynamics.md)] CRM or [!include[](../includes/pn-dynamics-crm.md)].  IF USERS SUBMIT DATA TO OTHER MICROSOFT SERVICES OR THIRD PARTY SERVICES, SUCH DATA IS GOVERNED BY THEIR RESPECTIVE PRIVACY STATEMENTS. For the avoidance of doubt, data shared outside of [!include[](../includes/pn-microsoft-dynamics.md)] CRM or [!include[](../includes/pn-dynamics-crm.md)] is not covered by users' [!include[](../includes/pn-microsoft-dynamics.md)]s CRM or [!include[](../includes/pn-dynamics-crm.md)] agreement(s) or the applicable [!include[](../includes/pn-microsoft-dynamics.md)] Trust Center. Microsoft encourages users to review these other privacy statements.  
&nbsp;<br />
By enabling the [!INCLUDE[pn_fieldservice_mobile_app_long](pn-fieldservice-mobile-app-long.md)] mobile app on a mobile device with location features enabled, real-time location data will be sent to [!INCLUDE[pn_bing_maps](pn-bing-maps.md)] and stored in [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)]. Users are prompted to provide permission for the flow of real-time location data during installation or use of the field service mobile app. To disable the flow of real-time location data from the device, the user must disable the device's location features or uninstall the application.  
&nbsp;<br />
The real-time location data sent by the field service mobile app is used to support the following scenarios:  

 -  To show the location of a user's customers. Data about the user's current location is passed to the mapping provider as context for the map rendered by the provider and displayed within field service mobile app.  

 -  To create and update a user's schedule. Data about the user's current location is passed to the field service capabilities in [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] to create and update a user's schedule. For example, to assign a task to the nearest technician.  
  
In addition, by enabling the field service mobile app on a mobile device, mobile app usage information, such as application errors, will be sent to Microsoft through a secure connection to Organization Insights and stored in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Table Storage.  
  
**Note:** Organization Insights provides the system administrator of a [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] organization with a quick overview of how the org is being used. The system administrator can view most active users, the number of SDK requests being initiated, and the number of being viewed by SDK users.  
  
A list of the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] components and services that are involved with Help Improve [!INCLUDE[pn_unified_service_desk](pn-unified-service-desk.md)] functionality is provided below.  
  
[!INCLUDE[cc_privacy_note_azure_trust_center](cc-privacy-note-azure-trust-center.md)]  
  
[Cloud Services](https://azure.microsoft.com/services/cloud-services/)  
  
**OrgInsights Data REST API (Web Role)**  
  
This web role accepts requests from the charts that display data in Organization Insights. The API reads aggregated data from the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Tables and returns it.  
  
[Azure Blob Storage](https://azure.microsoft.com/services/storage/blobs/)  
  
The Monitoring Agent (which runs on every scale group computer) collects the [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] organization's raw telemetry data and uploads it in Bond Format (Binary format) to [!INCLUDE[pn_azure_blob_storage](pn-azure-blob-storage.md)].  
  
[Azure Table Storage](https://azure.microsoft.com/services/storage/tables/)  
  
Raw telemetry data in [!INCLUDE[pn_azure_blob_storage](pn-azure-blob-storage.md)] is aggregated and stored in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Table Storage, which is read by the Cloud Service.  
  
[Microsoft Entra ID](https://azure.microsoft.com/services/active-directory/)  
  
Organization Insights uses [!INCLUDE[pn_azure_active_directory](pn-azure-active-directory.md)] Service to authenticate web services.  
  
[Azure Service Bus](https://azure.microsoft.com/services/service-bus/)  
  
The Monitoring Agent creates and queues messages whenever it uploads data to [!INCLUDE[pn_azure_blob_storage](pn-azure-blob-storage.md)]. The CMA pipe picks up these messages to aggregate the uploaded data.