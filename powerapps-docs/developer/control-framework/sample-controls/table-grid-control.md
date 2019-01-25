---
title: " Table grid Control| Microsoft Docs" 
description: "Implementing table grid control" 
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "NavaKiran" 
ms.author: "nkrb" 
manager: "" 
---

# Implementing Table Grid control

This sample showcases how to create a simple dataset control, view’s column metadata binding, record binding, more records from paging and record navigation to form.
The control header columns and internal record values are bound to the existing views.

> [!div class="mx-imgBorder"]
> ![Table Grid Control](../media/table_grid_control.png "Table Grid Control")

## Manifest 

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
  <control namespace="SampleNamespace" constructor="TSTableGrid" version="1.0.0" display-name-key="TS_TableGrid">
    <data-set name="simpleTableGrid" display-name-key="SimpleTableGridProperty">
	  </data-set>
    <resources>
      <code path="TS_TableGrid.js" order="1" />
	    <css path="css/TS_TableGrid.css" order="1" />
      <resx path="strings/TSTableGrid.1033.resx" version="1.0.0" />
    </resources>
  </control>
</manifest>
```

## Code

```TypeScript
/*
	This file is part of the Microsoft PowerApps code samples. 
	Copyright (C) Microsoft Corporation.  All rights reserved. 
	This source code is intended only as a supplement to Microsoft Development Tools and/or  
	on-line documentation.  See these other materials for detailed information regarding  
	Microsoft code samples. 

	THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER  
	EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF  
	MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE. 
 */

/// <reference path="./private_typing/inputsOutputs.d.ts"/>
/// <reference path="../../typing/ControlFramework.d.ts"/>

import DataSetInterfaces = ControlFramework.PropertyHelper.DataSetApi;
type DataSet = ControlFramework.PropertyTypes.DataSet;

module SampleNamespace
{
	'use strict';

	// Define const here
	const RowRecordId:string = "rowRecId";

	// Style name of Load More Button
	const LoadMoreButton_Hidden_Style = "LoadMoreButton_Hidden_Style";

export class TSTableGrid implements ControlFramework.StandardControl<InputsOutputs.IInputs, InputsOutputs.IOutputs> 
 {

	// Cached context object for the latest updateView
	private contextObj: ControlFramework.Context<InputsOutputs.IInputs>;
		
	// Div element created as part of this control's main container
	private mainContainer: HTMLDivElement;

	// Table element created as part of this control's table
	private dataTable: HTMLTableElement;

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
	this.mainContainer.classList.add("SimpleTable_MainContainer_Style");

	// Create data table container div. 
	this.dataTable = document.createElement("table");
	this.dataTable.classList.add("SimpleTable_Table_Style");

	// Create data table container div. 
	this.loadPageButton = document.createElement("button");
	this.loadPageButton.setAttribute("type", "button");
	this.loadPageButton.innerText = context.resources.getString("PCF_TSTableGrid_LoadMore_ButtonLabel");
	this.loadPageButton.classList.add(LoadMoreButton_Hidden_Style);
	this.loadPageButton.classList.add("LoadMoreButton_Style");
	this.loadPageButton.addEventListener("click", this.onLoadMoreButtonClick.bind(this));

	// Adding the main table and loadNextPage button created to the container DIV.
	this.mainContainer.appendChild(this.dataTable);
	this.mainContainer.appendChild(this.loadPageButton);
	container.appendChild(this.mainContainer);
		}

/**
* Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
*/
public updateView(context: ControlFramework.Context<InputsOutputs.IInputs>): void
 {
	this.contextObj = context;
	this.toggleLoadMoreButtonWhenNeeded(context.parameters.simpleTableGrid);

	if(!context.parameters.simpleTableGrid.loading){
				
		// Get sorted columns on View
		let columnsOnView = this.getSortedColumnsOnView(context);

if (!columnsOnView || columnsOnView.length === 0) {
            return;
		}

	let columnWidthDistribution = this.getColumnWidthDistribution(context, columnsOnView);


while(this.dataTable.firstChild)
	{
		this.dataTable.removeChild(this.dataTable.firstChild);
	  }

		this.dataTable.appendChild(this.createTableHeader(columnsOnView, columnWidthDistribution));		
		this.dataTable.appendChild(this.createTableBody(columnsOnView, columnWidthDistribution, context.parameters.simpleTableGrid));

		this.dataTable.parentElement.style.height = window.innerHeight - this.dataTable.offsetTop - 70 + "px";
			}
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
	if (!context.parameters.simpleTableGrid.columns) {
	return [];
			}
			
	let columns =context.parameters.simpleTableGrid.columns
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
 * Get column width distribution
* @param context context object of this cycle
* @param columnsOnView columns array on the configured view
* @returns column width distribution
*/
private getColumnWidthDistribution(context: ControlFramework.Context<InputsOutputs.IInputs>, columnsOnView: DataSetInterfaces.Column[]): string[]
 {

	let widthDistribution: string[] = [];
			
	// Considering need to remove border & padding length
	let totalWidth:number = context.mode.allocatedWidth - 250;
	let widthSum = 0;
			
	columnsOnView.forEach(function (columnItem) {
	widthSum += columnItem.visualSizeFactor;
			});

	let remainWidth:number = totalWidth;
			
	columnsOnView.forEach(function (item, index) {
	let widthPerCell = "";
	if (index !== columnsOnView.length - 1) {
		let cellWidth = Math.round((item.visualSizeFactor / widthSum) * totalWidth);
		remainWidth = remainWidth - cellWidth;
		widthPerCell = cellWidth + "px";
			}
	else {
		  widthPerCell = remainWidth + "px";
				}
			widthDistribution.push(widthPerCell);
			});

		return widthDistribution;

		}

private createTableHeader(columnsOnView: DataSetInterfaces.Column[], widthDistribution: string[]):HTMLTableSectionElement
 {

	let tableHeader:HTMLTableSectionElement = document.createElement("thead");
	let tableHeaderRow: HTMLTableRowElement = document.createElement("tr");
	tableHeaderRow.classList.add("SimpleTable_TableRow_Style");

	columnsOnView.forEach(function(columnItem, index){
	let tableHeaderCell = document.createElement("th");
	tableHeaderCell.classList.add("SimpleTable_TableHeader_Style");
	let innerDiv = document.createElement("div");
	innerDiv.classList.add("SimpleTable_TableCellInnerDiv_Style");
	innerDiv.style.maxWidth = widthDistribution[index];
	innerDiv.innerText = columnItem.displayName;
	tableHeaderCell.appendChild(innerDiv);
	tableHeaderRow.appendChild(tableHeaderCell);
			});

	tableHeader.appendChild(tableHeaderRow);
	return tableHeader;
		}

		
private createTableBody(columnsOnView: DataSetInterfaces.Column[], widthDistribution: string[], gridParam: DataSet):HTMLTableSectionElement
{

	let tableBody:HTMLTableSectionElement = document.createElement("tbody");

	if(gridParam.sortedRecordIds.length > 0)
	 {
		for(let currentRecordId of gridParam.sortedRecordIds){
					
		let tableRecordRow: HTMLTableRowElement = document.createElement("tr");
		tableRecordRow.classList.add("SimpleTable_TableRow_Style");
		tableRecordRow.addEventListener("click", this.onRowClick.bind(this));

		// Set the recordId on the row dom
		tableRecordRow.setAttribute(RowRecordId, gridParam.records[currentRecordId].getRecordId());
					

		columnsOnView.forEach(function(columnItem, index){
		let tableRecordCell = document.createElement("td");
		tableRecordCell.classList.add("SimpleTable_TableCell_Style");
		let innerDiv = document.createElement("div");
		innerDiv.classList.add("SimpleTable_TableCellInnerDiv_Style");
		innerDiv.style.maxWidth = widthDistribution[index];
		innerDiv.innerText = gridParam.records[currentRecordId].getFormattedValue(columnItem.name);
		tableRecordCell.appendChild(innerDiv);
		tableRecordRow.appendChild(tableRecordCell);
					});

		tableBody.appendChild(tableRecordRow);
				}
			}
	else
	 {
		let tableRecordRow: HTMLTableRowElement = document.createElement("tr");
		let tableRecordCell: HTMLTableCellElement = document.createElement("td");
		tableRecordCell.classList.add("No_Record_Style");
		tableRecordCell.colSpan = columnsOnView.length;
		tableRecordCell.innerText = this.contextObj.resources.getString("PCF_TSTableGrid_No_Record_Found");
		tableRecordRow.appendChild(tableRecordCell)
		tableBody.appendChild(tableRecordRow);
			}

		return tableBody;
		}


/**
* Row Click Event handler for the associated row when being clicked
* @param event
*/
private onRowClick(event: Event): void 
 {
	let rowRecordId = (event.currentTarget as HTMLTableRowElement).getAttribute(RowRecordId);

	if(rowRecordId)
	 {
		let entityReference = this.contextObj.parameters.simpleTableGrid.records[rowRecordId].getNamedReference();
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
			
if(gridParam.paging.hasNextPage && this.loadPageButton.classList.contains(LoadMoreButton_Hidden_Style))
 {
	this.loadPageButton.classList.remove(LoadMoreButton_Hidden_Style);
			}
else if(!gridParam.paging.hasNextPage && !this.loadPageButton.classList.contains(LoadMoreButton_Hidden_Style))
 {
	this.loadPageButton.classList.add(LoadMoreButton_Hidden_Style);
			}

		}

/**
* 'LoadMore' Button Event handler when load more button clicks
* @param event
*/
private onLoadMoreButtonClick(event: Event): void {
this.contextObj.parameters.simpleTableGrid.paging.loadNextPage();
this.toggleLoadMoreButtonWhenNeeded(this.contextObj.parameters.simpleTableGrid);
		}
	}
}
```

## Overview

Column Header bind to the View :

View column info lies at `context.parameters.[dataset_property_name].columns`. It’s an array type. 

Record binding :

- The sorted record Ids are at `context.parameters.[dataset_property_name].sortedRecordIds`
- All records info is at `context.parameters.[dataset_property_name].records` 
- For each record object, `context.parameters.[dataset_property_name].records[record_Id]` 
- Formatted value could be retrieved at `getFormattedValue` 

Load more page of data if needed :

`context.parameters.[dataset_property_name].paging` will provide paging functionality like `hasNextPage` and `loadNextPage` data. The `Load More` button is shown if it has next page data.

This sample also showcases how the control listens to the container resize. 

The `trackContainerResize` method should be called within [init](../reference/control/init.md) method so that the `mode.allocatedWidth` and `mode.allocatedHeight` will be provided each time [updateView](../reference/control/updateview.md) being called. If this method is not being called initially, then they don't have `allocatedWidth` and `allocatedHeight` provided.

If the allocatedHeight is –1, that means there is no limit on height. The control should adjust its height based on the provided width.

### Related topics

[PowerApps Control Framework Manifest Schema Reference](../manifest-schema-reference/index.md)<br />
[PowerApps Control Framework API Reference](../index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
