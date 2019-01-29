---
title: DataSet Grid Control | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 356561d0-a36b-4b93-8b76-3e1abf9414e9
---

This sample shows how to change the user experience of interacting with dataset. For example, by default you only see the home page grid on an entity homepage as a table. You can build your own custom control that can display the data as per your choice. This sample show the records as tiles instead of the regular tabular grid.

> [!div class="mx-imgBorder"]
> ![Data Set Grid Control](../media/data-set-grid.png "Data Set Grid Control")

## Manifest 

```xml

<?xml version="1.0" encoding="utf-8" ?>
<manifest>
  <control namespace="SampleNamespace" constructor="TSDataSetGrid" version="1.0.0" display-name-key="TS_DataSetGrid">
    <data-set name="dataSetGrid" display-name-key="DataSetGridProperty">
	  </data-set>
    <resources>
      <code path="TS_DataSetGrid.js" order="1" />
	    <css path="css/TS_DataSetGrid.css" order="1" />
      <resx path="strings/TSDataSetGrid.1033.resx" version="1.0.0" />
    </resources>
  </control>
</manifest>
```

## Code 

```TypeScript

import DataSetInterfaces = ControlFramework.PropertyHelper.DataSetApi;
type DataSet = ControlFramework.PropertyTypes.DataSet;

module SampleNamespace
{
'use strict';

// Define const here
const RowRecordId:string = "rowRecId";

// Style name of Load More Button
const DataSetControl_LoadMoreButton_Hidden_Style = "DataSetControl_LoadMoreButton_Hidden_Style";

export class TSDataSetGrid implements ControlFramework.StandardControl<InputsOutputs.IInputs, InputsOutputs.IOutputs> {

// Cached context object for the latest updateView
private contextObj: ControlFramework.Context<InputsOutputs.IInputs>;

// Div element created as part of this control's main container
private mainContainer: HTMLDivElement;

// Table element created as part of this control's table
private gridContainer: HTMLDivElement;

// Button element created as part of this control
private loadPageButton: HTMLButtonElement;

/**
* Empty constructor.
*/
constructor()
{

}

/**
* Used to initialize the control instance. Controls can kick off remote server calls and other initialization actions here.
* Data-set values are not initialized here, use updateView.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to property names defined in the manifest, as well as utility functions.
* @param notifyOutputChanged A callback method to alert the framework that the control has new outputs ready to be retrieved asynchronously.
* @param state A piece of data that persists in one session for a single user. Can be set at any point in a controls life cycle by calling 'setControlState' in the Mode interface.
* @param container If a control is marked control-type='starndard', it will receive an empty div element within which it can render its content.
*/
public init(context: ControlFramework.Context<InputsOutputs.IInputs>, notifyOutputChanged: () => void, state: ControlFramework.Dictionary, container:HTMLDivElement)
{
// Need to track container resize so that control could get the available width. The available height won't be provided even this is true
context.mode.trackContainerResize(true);

// Create main table container div.
this.mainContainer = document.createElement("div");

// Create data table container div.
this.gridContainer = document.createElement("div");
this.gridContainer.classList.add("DataSetControl_grid-container");

// Create data table container div.
this.loadPageButton = document.createElement("button");
this.loadPageButton.setAttribute("type", "button");
this.loadPageButton.innerText = context.resources.getString("PCF_DataSetControl_LoadMore_ButtonLabel");
this.loadPageButton.classList.add(DataSetControl_LoadMoreButton_Hidden_Style);
this.loadPageButton.classList.add("DataSetControl_LoadMoreButton_Style");
this.loadPageButton.addEventListener("click", this.onLoadMoreButtonClick.bind(this));

// Adding the main table and loadNextPage button created to the container DIV.
this.mainContainer.appendChild(this.gridContainer);
this.mainContainer.appendChild(this.loadPageButton);
this.mainContainer.classList.add("DataSetControl_main-container");
container.appendChild(this.mainContainer);
}


/**
* Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
*/
public updateView(context: ControlFramework.Context<InputsOutputs.IInputs>): void
{
this.contextObj = context;
this.toggleLoadMoreButtonWhenNeeded(context.parameters.dataSetGrid);

if(!context.parameters.dataSetGrid.loading){

// Get sorted columns on View
let columnsOnView = this.getSortedColumnsOnView(context);

if (!columnsOnView || columnsOnView.length === 0) {
return;
}

while(this.gridContainer.firstChild)
{
this.gridContainer.removeChild(this.gridContainer.firstChild);
}

this.gridContainer.appendChild(this.createGridBody(columnsOnView, context.parameters.dataSetGrid));
}
// this is needed to ensure the scroll bar appears automatically when the grid resize happens and all the tiles are not visible on the screen.
this.mainContainer.style.maxHeight = window.innerHeight - this.gridContainer.offsetTop - 75 + "px";
}

/**
* It is called by the framework prior to a control receiving new data.
* @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
*/
public getOutputs(): InputsOutputs.IOutputs
{
return {};
}

/**
* Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
* i.e. cancelling any pending remote calls, removing listeners, etc.
*/
public destroy(): void
{
}

/**
* Get sorted columns on view
* @param context
* @return sorted columns object on View
*/
private getSortedColumnsOnView(context: ControlFramework.Context<InputsOutputs.IInputs>): DataSetInterfaces.Column[]
{
if (!context.parameters.dataSetGrid.columns) {
return [];
}

let columns =context.parameters.dataSetGrid.columns
.filter(function (columnItem:DataSetInterfaces.Column) {
// some column are supplementary and their order is not > 0
return columnItem.order >= 0 }
);

// Sort those columns so that they will be rendered in order
columns.sort(function (a:DataSetInterfaces.Column, b: DataSetInterfaces.Column) {
return a.order - b.order;
});

return columns;
}

/**
* funtion that creates the body of the grid and embeds the content onto the tiles.
* @param columnsOnView columns on the view whose value needs to be shown on the UI
* @param gridParam data of the Grid
*/
private createGridBody(columnsOnView: DataSetInterfaces.Column[], gridParam: DataSet):HTMLDivElement{

let gridBody:HTMLDivElement = document.createElement("div");

if(gridParam.sortedRecordIds.length > 0)
{
for(let currentRecordId of gridParam.sortedRecordIds){

let gridRecord: HTMLDivElement = document.createElement("div");
gridRecord.classList.add("DataSetControl_grid-item");
gridRecord.addEventListener("click", this.onRowClick.bind(this));

// Set the recordId on the row dom
gridRecord.setAttribute(RowRecordId, gridParam.records[currentRecordId].getRecordId());

columnsOnView.forEach(function(columnItem, index){
let labelPara = document.createElement("p");
labelPara.classList.add("DataSetControl_grid-text-label");

let valuePara = document.createElement("p");
valuePara.classList.add("DataSetControl_grid-text-value");

labelPara.textContent = columnItem.displayName+" : ";
gridRecord.appendChild(labelPara);
if(gridParam.records[currentRecordId].getFormattedValue(columnItem.name) != null && gridParam.records[currentRecordId].getFormattedValue(columnItem.name) != "")
{
valuePara.textContent = gridParam.records[currentRecordId].getFormattedValue(columnItem.name);
gridRecord.appendChild(valuePara);
}
else
{
valuePara.textContent = "-";
gridRecord.appendChild(valuePara);
}

});

gridBody.appendChild(gridRecord);
}
}
else
{
let noRecordLabel: HTMLDivElement = document.createElement("div");
noRecordLabel.classList.add("DataSetControl_grid-norecords");
noRecordLabel.style.width = this.contextObj.mode.allocatedWidth - 25 + "px";
noRecordLabel.innerHTML = this.contextObj.resources.getString("PCF_DataSetControl_No_Record_Found");
gridBody.appendChild(noRecordLabel);
}

return gridBody;
}


/**
* Row Click Event handler for the associated row when being clicked
* @param event
*/
private onRowClick(event: Event): void {
let rowRecordId = (event.currentTarget as HTMLTableRowElement).getAttribute(RowRecordId);

if(rowRecordId)
{
let entityReference = this.contextObj.parameters.dataSetGrid.records[rowRecordId].getNamedReference();
let entityFormOptions = {
entityName: entityReference.entityType,
entityId: entityReference.id,
}
this.contextObj.navigation.openForm(entityFormOptions);
}
}

/**
* Toggle 'LoadMore' button when needed
*/
private toggleLoadMoreButtonWhenNeeded(gridParam: DataSet): void{

if(gridParam.paging.hasNextPage && this.loadPageButton.classList.contains(DataSetControl_LoadMoreButton_Hidden_Style))
{
this.loadPageButton.classList.remove(DataSetControl_LoadMoreButton_Hidden_Style);
}
else if(!gridParam.paging.hasNextPage && !this.loadPageButton.classList.contains(DataSetControl_LoadMoreButton_Hidden_Style))
{
this.loadPageButton.classList.add(DataSetControl_LoadMoreButton_Hidden_Style);
}

}

/**
* 'LoadMore' Button Event handler when load more button clicks
* @param event
*/
private onLoadMoreButtonClick(event: Event): void {
this.contextObj.parameters.dataSetGrid.paging.loadNextPage();
this.toggleLoadMoreButtonWhenNeeded(this.contextObj.parameters.dataSetGrid);
}
}
}
```

## Overview

In this sample we have the input parameter defined in the control Manifest with the data-set tag. This is the input property that gets bound to the control.  
 
This control has two important containers that are added onto a main div that is added onto the div that is passed onto the control.  The first container holds the tiles that shows the record data from the view and the second container is for the Load More button that shows when there are records that needs more area that can fit in one page. 
 
Both the containers are generated and refreshed whenever the [updateView](../reference/control/updateview.md) method is called. For the first container, we generate the tiles based on the information in the columns and the number of records. This ensures we display a tile for each record along with its information on it.  
 
If there exists a following page for the records, the load more button is displayed i.e., the second container is visible and is hidden if there are no more pages in the result set.  
 
On click of the load more button, we load the next page of records and append it to the existing result set and the logic to hide/show the button remains same as earlier as shown in the code. This is taken care by the ***onLoadMoreButtonClick*** method which is bound to the button. 
 
The ***toggleLoadMoreButtonWhenNeeded*** function takes the input as the data set and checks if the data set has next page and if the button is hidden/visible and respectively hides/shows the button.  
 
The ***onRowClick*** function attaches the context of the record using its GUID and invokes the [openForm](../reference/navigation/openform.md) method of the NavigationAPI to open that respective record. This method is bound to each tile that gets generated as part of the ***createGridBody*** method. 
 
The ***getSortedColumnsOnView*** method returns the list of columns based on the defined order on the view. 

### Related topics

[PowerApps Control Framework API Reference](../reference/index.md)<br />
[PowerApps Control Framework Manifest Schema Reference](../manifest-schema-reference/index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
