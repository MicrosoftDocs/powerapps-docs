By enabling [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] you agree to allow flow of the data from [!INCLUDE[pn-microsoftcrm](../includes/pn-microsoftcrm.md)] to certain [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] services in order to perform some of the marketing processes. These services are collectively referred to as "[!INCLUDE[pn-marketing-app-module](../includes/pn-marketing-app-module.md)] services."

To do customer journeys, [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] needs to send customer journey, email, submission form, and marketing page definitions to these [!INCLUDE[pn-marketing-app-module](../includes/pn-marketing-app-module.md)] services, running on [!INCLUDE[pn_azure_service_fabric](../includes/pn_azure_service_fabric.md)]. Marketing Pages are further sent to a customer's own instance of Portal capabilities for [!INCLUDE[pn-microsoftcrm](../includes/pn-microsoftcrm.md)].

To personalize sent emails [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] needs to enable data flow to and from [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)]. Please see below for more information about the [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)] service. Data flow to [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)] includes synchronization of contacts and accounts to [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)]. [!INCLUDE[pn-marketing-app-module](../includes/pn-marketing-app-module.md)] services uses this data to personalize email content. The data that is included depends exclusively on the email definition.

To recalculate lead score models and marketing segments, [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] needs to send lead score model definitions and segment definitions to [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)] and to leverage profiles and interactions in [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)] within these calculations.

To provide insights into the email and Internet interactions captured by [!INCLUDE[pn-marketing-app-module](../includes/pn-marketing-app-module.md)] services, the collected data flows from [!INCLUDE[pn-marketing-app-module](../includes/pn-marketing-app-module.md)] services to both [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] and [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)].

If additionally, [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] Event Management integration is enabled, [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] is synchronizing events to [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)] (directly via the connector for [!INCLUDE[pn-crm-online-shortest](../includes/pn-crm-online-shortest.md)]) and event registrations and check-ins (via [!INCLUDE[pn-marketing-app-module](../includes/pn-marketing-app-module.md)] services, as interactions).

Data flow involving [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)] is the following:
- Entity data from [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] to [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)], using the regular inbound connector of [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)], in order to provide content for email personalization, lead scoring, and segmentation (mainly contacts and accounts, eventually also leads and events)
- Entity data from [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] via [!INCLUDE[pn-marketing-app-module](../includes/pn-marketing-app-module.md)] services to [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)], in order to provide identifiers for interactions and insights (customer journey, marketing emails, marketing pages)
- Interactions from [!INCLUDE[pn-marketing-app-module](../includes/pn-marketing-app-module.md)] services to [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)] (email tracking, website tracking, customer journey progress)
- Interactions from [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] via [!INCLUDE[pn-marketing-app-module](../includes/pn-marketing-app-module.md)] services to [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)] (event registrations and check-ins)
- [!INCLUDE[pn-insights](../includes/pn-insights.md)] (interactions and KPIs) from [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)] via [!INCLUDE[pn-marketing-app-module](../includes/pn-marketing-app-module.md)] services to [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] (mainly customer journey and email send progress, and lead scoring results)
- [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)] apps (segmentation and widgets) from [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)] directly into dedicated and sandboxed UI elements in forms of [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)]

### Marketing services

[!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] uses these [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] services:

- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Data Lake Store
- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Data Lake Analytics
- [!INCLUDE[pn-azure-key-vault](../includes/pn-azure-key-vault.md)]
- [!INCLUDE[pn_azure_service_fabric](../includes/pn_azure_service_fabric.md)]
- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] DocumentDB
- [!INCLUDE[pn-microsoft-azure-active-directory](../includes/pn-microsoft-azure-active-directory.md)]
- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Storage

> [!NOTE]
> For more information about additional [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] service offerings, see the [!INCLUDE[cc_privacy_note_azure_trust_center](../includes/cc_privacy_note_azure_trust_center.md)] (<https://azure.microsoft.com/support/trust-center/>).

### [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)]

By using [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)], you are activating the transfer of customer data into [!INCLUDE[pn-customer-insights-full](../includes/pn-customer-insights-full.md)] for further processing. Your use of [!INCLUDE[pn-customer-insights-short](../includes/pn-customer-insights-short.md)] for [!INCLUDE[pn-microsoftcrm](../includes/pn-microsoftcrm.md)] might require compliance with specific privacy laws. Please direct any questions to the appropriate representative in your organization.

At present, [!INCLUDE[pn-customer-insights-short](../includes/pn-customer-insights-short.md)] is in public preview and does not offer the same level of privacy and security commitments as [!INCLUDE[pn-marketing-business-app-module-name](../includes/pn-marketing-business-app-module-name.md)] or [!INCLUDE[pn-microsoftcrm](../includes/pn-microsoftcrm.md)] Customer Engagement. [!INCLUDE[pn-customer-insights-short](../includes/pn-customer-insights-short.md)] is natively built on [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] services, and respective compliance and security standards for each applicable [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] service apply. For more information, go to the [!INCLUDE[cc-microsoft](../includes/cc-microsoft.md)] Trust Center: [https://azure.microsoft.com/support/trust-center/](https://azure.microsoft.com/support/trust-center/)

[!INCLUDE[pn-customer-insights-short](../includes/pn-customer-insights-short.md)] uses these [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] services:

- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Data Lake Store
- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Data Lake Analytics
- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] HDInsight (Spark, Phoenix, HBase)
- [!INCLUDE[pn-ms-azure-sql-database](../includes/pn-ms-azure-sql-database.md)]
- [!INCLUDE[pn-azure-key-vault](../includes/pn-azure-key-vault.md)]
- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Secret Store
- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Event Hub
- [!INCLUDE[pn-azure-stream-analytics](../includes/pn-azure-stream-analytics.md)]
- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Redis Cache
- [!INCLUDE[pn_azure_service_fabric](../includes/pn_azure_service_fabric.md)]
- [!INCLUDE[pn-microsoft-azure-active-directory](../includes/pn-microsoft-azure-active-directory.md)]
- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Monitoring
- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Metrics
- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Websites
- [!INCLUDE[pn_azure_service_bus](../includes/pn_azure_service_bus.md)]
- [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Storage
