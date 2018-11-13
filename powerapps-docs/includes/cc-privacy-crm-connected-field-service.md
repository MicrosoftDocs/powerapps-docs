By installing [!INCLUDE[pn_connected_field_service_msdyn365](pn-connected-field-service-msdyn365.md)], when you provide your [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] subscription information, the required [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] resources (listed below) will be deployed and your [!INCLUDE[pn_dynamics_crm_online](pn-dynamics-crm-online.md)] instance will send data (such as commands and registrations) to [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] to enable IoT–enabled scenarios that register devices and then send and receive commands to the registered devices. An administrator can uninstall Connected Field Service to remove the functionality and then navigate to the [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] portal to manage any related [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] services that are no longer needed.  
  
 [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] components and services that are involved with Connected Field Service functionality are detailed in the following sections.  
  
 [!INCLUDE[cc_privacy_note_azure_trust_center](cc-privacy-note-azure-trust-center.md)]  
  
 [Service bus queue](https://azure.microsoft.com/documentation/articles/service-bus-dotnet-get-started-with-queues/)  
  
 This provides a queue for both inbound and outbound messages (commands) flowing between [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] and [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)]. When an IoT alert is sent to [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)], or a command is sent from [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] to the IoT hub, it will be queued here.  
  
 [Logic Apps](https://azure.microsoft.com/services/logic-apps/)  
  
 This provides an orchestration service that uses a [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] connector and a Queue connector. [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] connectors are used to construct entities that are specific to [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)]and Queue connectors are used for polling the queue.  
  
 [Stream analytics](https://azure.microsoft.com/services/stream-analytics/)  
  
 This provides a fully managed, real-time event processing engine that helps to unlock deep insights from data. Stream Analytics makes it easy to set up real-time analytic computations on data streaming from devices, sensors, web sites, social media, applications, infrastructure systems, and more. It is functioning as a funnel to send selective IoT alerts to [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)].  
  
 [IoT Hub](https://azure.microsoft.com/services/iot-hub/)  
  
 Connected Field Services uses the IoT Hub to manage the state of registered devices and assets. In addition, the IoT Hub sends commands and notifications to connected devices—and tracks message delivery with acknowledgement receipts. Device messages are sent in a durable way to accommodate intermittently connected devices.  
  
 **Simulator**  
  
 This is a test web app to emulate the device that is sending commands or receiving commands from the IoT hub.  
  
 [Azure SQL Database](https://azure.microsoft.com/services/sql-database/)  
  
 Connected Field Service uses SQL [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] to store device heartbeat messages for later use by PowerBI to show the status of devices in [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)].  
  
 [Azure Blob Storage](https://azure.microsoft.com/services/storage/)  
  
 Queries that Stream Analytics will use are stored to [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] Blob storage.