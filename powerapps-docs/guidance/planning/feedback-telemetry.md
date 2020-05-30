# Collecting feedback and analyzing telemetry

To help you refine and improve your app, collecting feedback and analyzing the
telemetry is an important part of the refining process. Look
back at the goals you set in the planning phase to reflect
on how much the app has contributed.

## Collecting feedback

Providing a place to give feedback ensures your apps will continue to meet user
needs. You can leverage Microsoft Forms and Power Automate to automatically
collect valuable feedback. Microsoft Forms have Net Promoter Score built in.

## Analyzing telemetry

To ensure healthy app usage, you should leverage the analytics features of the
app. The Power Apps analytics provides you information such as:

-   Number of active users

-   Devices / Browsers used

-   Locations

-   App diagnostics

-   Service performance

As an app maker, you can access your analytics by accessing the App usage
report at [https://make.powerapps.com](https://make.powerapps.com). This report is available if you are the owner or co-owner of the Canvas
app. Data is available for 30 days to view usage information such as app launch
counts, unique users by day etc.

![A screenshot of App Usage Report](media/telemetry.png)

If you are an administrator, you can access analytics at overall tenant level.
For more information for administrators, see [Admin Analytics for Power
Apps](https://docs.microsoft.com/power-platform/admin/analytics-powerapps).

### Adding manual telemetry using Azure Application Insights

You can gain additional insights/telemetry about the app by setting up
connection to Azure Application Insights - a feature that is part of [Azure
Monitor](https://docs.microsoft.com/azure/azure-monitor/overview) Some of the
telemetry you can gain from setting this up are as follows:

-   Number of active users using the app

-   Location of where the app is used

-   What screens are used the most

-   User flow from one screen to another

![A screenshot of Azure Application Insights](media/app-insights.png)

You can also set up custom telemetry by using the [trace
function](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/functions/function-trace).
