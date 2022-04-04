---
title: List map view
description: Learn how to enable a list to  render as a map on a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 04/04/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - ProfessorKendrick
---

# List Map view

On the **Map View** tab, you can enable the list to render as a map view of the data.

The map view is powered by [!INCLUDE[pn-bing](../../../includes/pn-bing.md)] maps with search functionality to find locations near an address. By populating your records with latitude and longitude coordinate values and specifying the necessary configuration options listed in this section, your records can be rendered as pushpins on a map. Any record that doesn't have a latitude or longitude value will be excluded from the search. The initial load of the page will display all records within the initial value of the Distance Values field (in miles or km, depending on the Distance Units specified) from the Default Center Latitude and Default Center Longitude coordinates. The view specified is ignored when Map view is used, and a distance query is applied to the dataset to return the mappable results.

> [!NOTE] 
> - This option is not supported in the German Sovereign Cloud environment. The Map view section will not be visible in this environment.
> - Only Bing maps are supported as the **Map type**.

## List Calendar view

On the **Calendar View** tab, you can enable the list to render as a calendar view, with each individual record configured to act as a single event.

The following field mappings can be configured to display list records as dated events on the calendar. The records need to include at minimum a date field.

> [!Tip]
> See [date and time](behavior-format-date-time-field.md#date-and-time) field behaviors for information on formatting date and time fields on portals.

| Entity Field Mappings | Details |
| - | - |
| Start Date Field Name | A datetime column representing the start date of a calendar event. |
| End Date Field Name | A datetime column representing the end date of a calendar event. |
| Summary Field Name | A text column that will show the summary of a calendar event. |
| Description Field Name | A text column that will display a description of the calendar event. |
| Organizer Field Name | A text or lookup column that will display the organizer of the calendar event. |
| Location Field Name | A text column describing the location of the calendar event.|
| Is All Day Field Name | A yes/no column indicating if the calendar event is all day. |

| Setting | Details |
| - | - |
| Initial View | Initial view of the calendar; year, month, week, or day. Default value is month. |
| Initial Date | The initial start date when the calendar is rendered. Default (blank) will be the current date. |
| Time Zone Display Mode | The time zone the calendar will be displayed in. No option selected will display the events based on how the date column was configured in Dataverse. The *User Local Time Zone* displays events in the calendar using the time zone of the user viewing the portal. *Specific Time Zone* will display the calendar events with a specified time zone. |
| Display Time Zone | If the **Time Zone Display Mode** is set to *Specific Time Zone* this value will determine the time zone the calendar events are displayed. |
| Style | The setting displays the calendar in either a *Full Calendar* format or as an *Event List* |

Once the specific fields are configured, a list calendar view will appear on the portal page.

:::image type="content" source="media/lists/calendar-list.png" alt-text="List displayed as a calendar on a web page.":::

### See also

- [Microsoft Learn: Display multiple Dataverse records using lists](/learn/modules/portals-access-data-platform/2-entity-lists)
- [Configure a portal](configure-portal.md)  
- [Redirect to a new URL on a portal](add-redirect-url.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
