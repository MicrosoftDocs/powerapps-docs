<properties
	pageTitle="Common issues and resolutions | Microsoft PowerApps"
	description="Read about PowerApps issues and resolutions"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="MandiOhlinger"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="06/01/2016"
   ms.author="mandia"/>

# Common issues and resolutions

## Create any app

1.  **When PowerApps generates an app from data, the field used for sorting and searching isn't automatically configured.**

	To configure this field, edit the **[Items](controls/properties-core.md)** formula for the gallery, as the sections for filtering and sorting in [Add a gallery](add-gallery.md) describe.

1. **For apps that are created from data, only the first 500 records of a data source can be accessed.**

	In general, PowerApps works with any size data source by delegating operations to the data source. For operations that can't be delegated, PowerApps will give a warning at authoring time and operate on only the first 500 records of the data source.  See the [Filter function](functions/function-filter-lookup.md) article for more details about delegation.  

	In this release, delegation doesn't support **[Filter](functions/function-filter-lookup.md)** and **[Sort](functions/function-sort.md)** functions used together, nor does it support the **[In](functions/operators.md#in-and-exactin-operators)** operator.  These features are used by apps that are created from data, so these apps are limited to the first 500 records. To partially work around this issue, you can remove one or both of the Filter and Sort functions from the gallery's **[Items](controls/properties-core.md)** property.

## Create an app automatically from Excel

1. **Excel data must be formatted as a table.**

	If **Data type unsupported** or **Not formatted as a table** appears when you try to use an Excel connection in your app, [format the data as a table](https://support.office.com/article/Format-an-Excel-table-6789619F-C889-495C-99C2-2F971C0E2370) by following these steps:

	1. Open the Excel file, and then select any cell in the data that you want to use.
	1. On the **Insert** tab, select **Table**.
	1. In the **Save as Table** dialog box, select the **My table has headers** checkbox, and then select **OK**.
	1. Save your changes.

## Create an app automatically from SharePoint

1. **You can create an app from a SharePoint Online custom list but not a document library.**

	Support for document libraries is expected soon.

1. **Not all column types are supported.**

	| Column type | Support |
|---|---|
| Boolean (Yes/No) | Yes |
| Single line of text | Yes |
| Number | Yes |
| Hyperlink | Yes |
| Multiple lines of text | Yes |
| Date and Time | Yes |
| Currency | Yes |
| Picture | Yes (read-only) |
| Lookup | Yes (read-only) |
| Person or Group | Yes (read-only) |
| Managed Metadata | Yes (read-only) |
| Choice | Yes (read-only) |
| Calculated | Yes (read-only) |
| Task Outcome | No |
| External data | No |

> [AZURE.NOTE] For the column types marked as *Yes (read-only)*, full support is coming soon.

1. **Not all types of columns support all types of cards.**  

	| Column type | Supported card/s |
|---|---|
| Yes/No | View text <br/>View toggle |
| Number | View percentage <br/>View rating <br/>View text |
| Hyperlink | View URL <br/>View text |
| Single line of text | View text |
| Multiple lines of text | View text |
| Date and Time | View text |
| Currency | View percentage <br/>View rating <br/>View text |
| Picture | View image <br/>View text |
| Lookup | View lookup |
| Person or Group | View lookup |
| Managed Metadata | View lookup |
| Choice | View lookup |

## Customize an app

1. **It can sometimes take a moment before a newly shared app can be used.**

	In some cases, a newly shared app won't be immediately available.  Wait a few moments, and it should become available.

1. **Sharing an app for editing doesn't also share the flows.**

	You must share the flows separately so that others can edit them, not just run them.

## Use controls

1. **In the [Form control](controls/control-form-detail.md), you can't change data by using a custom card.**

	The stock custom card is missing the **[Update](controls/control-card.md)** property, which is required to write back changes. To work around this:
	- Select the form control, and insert a card by using the right-hand pane based on the field that you want the card to show.  
	- Unlock the card, as described in [Understanding data cards](working-with-cards.md#unlock-a-card).
	- Remove or rearrange controls within the card as you see fit, just as you would with the custom card.   

1. **Card gallery is deprecated.**

	Existing apps that use this feature will continue to run for the time being, but you can't add a card gallery. Please replace card galleries with the new **[Edit form](controls/control-form-detail.md)** and **[Display form](controls/control-form-detail.md)** controls.

## Other areas

1. **Co-authoring isn't supported. One author at a time, please.**

	You can corrupt an app or over-write others’ changes if more than one person modifies the same app at the same time. Close the app before someone else edits it.

1. **An app that's running on Android 5.0, Nexus 6 with Webview versions v48 or v49 may crash.**

	Users can fix this problem by updating to a lower version of Webview (3x) or update to Android 6.0.

1. **Camera usage may be temporarily disabled if memory is low.**

	If your mobile device is low on memory, the camera is temporarily disabled to avoid crashing the device.
