By enabling the embedding of Power BI tiles and dashboards, when a user embeds a Power BI tile or dashboard, that user’s [!INCLUDE[pn_azure_active_directory](pn-azure-active-directory.md)] authorization token for Microsoft Dataverse is used to authenticate with the Power BI service with an implicit grant, providing a seamless “single-sign on” experience for the end user.  
  
 An administrator can disable embedding of Power BI tiles and dashboards at any time to stop use of the [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] authorization token for authenticating with Power BI service. Any existing tiles or dashboards will stop rendering for the end user.  
  
 The [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] component or service that is involved with embedding of Power BI tiles is detailed in the following section.  
  
 [!INCLUDE[cc_privacy_note_azure_trust_center](cc-privacy-note-azure-trust-center.md)]  
  
 [Microsoft Entra ID](https://azure.microsoft.com/services/active-directory/)  
  
 This service provides the authentication token exchanged with Power BI service for API and UI authentication.