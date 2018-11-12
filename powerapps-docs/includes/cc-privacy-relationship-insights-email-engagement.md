By enabling Email Engagement, a Embedded intelligence feature, when an email marked with the **Follow** setting is sent from [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)], information about interactions with the email by recipients will be collected and stored in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] for the purposes of computing recipient activity KPIs and interactions on “followed” emails.  
  
 A system administrator enables Email Engagement by provisioning the feature from the **Email Engagement** tab within Embedded intelligence. Administrators can subsequently disable Email Engagement in the organization from the **Intelligence Configuration** node, under **Settings**.  
  
 When the feature has been disabled, emails sent from [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] cannot be followed, either from the user interface or programmatically. Also, recipient interaction data will no longer be collected on sent emails that were marked with the **Follow** setting. Any data previously collected will remain in [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] and will be available again if the feature is re-enabled in the organization. Data is retained for 90 days after customers terminate their subscription with Microsoft. [!INCLUDE[pn_dynamics_crm](pn-dynamics-crm.md)] users can also disable the Embedded intelligence - Email Engagement functionality on a per Contact or per Lead basis by changing the **Follow Email** setting under **Contact Preferences**.  
  
 [!INCLUDE[pn_azure_shortest](pn-azure-shortest.md)] components and services that are involved with Email Engagement functionality are detailed below.  
  
 [!INCLUDE[cc_privacy_note_azure_trust_center](cc-privacy-note-azure-trust-center.md)]  
  
 **[!INCLUDE[pn_azure_storage_account](pn-azure-storage-account.md)]**  
  
 The Email Engagement feature uses [!INCLUDE[pn_azure_storage_account](pn-azure-storage-account.md)] to temporarily store email interaction blobs.