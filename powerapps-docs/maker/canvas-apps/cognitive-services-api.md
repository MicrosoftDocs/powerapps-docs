---
title: Use Cognitive Services in Power Apps | Microsoft Docs
description: Build a basic canvas app that uses the Azure Cognitive Services Text Analytics API to analyze text.
author: lancedMicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 01/27/2021
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Use Cognitive Services in Power Apps

This article shows you how to build a basic canvas app that uses the [Azure Cognitive Services Text Analytics API](https://docs.microsoft.com/azure/cognitive-services/text-analytics/overview) to analyze text. We'll show you how to set up the Text Analytics API, and connect to it with the [Text Analytics connector](https://docs.microsoft.com/connectors/cognitiveservicestextanalytics/). Then we'll show you how to create a canvas app that calls the API.

> [!NOTE]
> If you are new to building apps in Power Apps, we recommend reading [Create an app from scratch](get-started-create-from-blank.md) before diving into this article.

## Introduction to Azure Cognitive Services

Azure Cognitive Services are a set of APIs, SDKs, and services available to make your applications more intelligent, engaging, and discoverable. These services enable you to easily add intelligent features – such as emotion and video detection; facial, speech and vision recognition; and speech and language understanding – into your applications.

We'll focus on "language understanding" for this article, working with the Text Analytics API. This API enables you to detect sentiment, key phrases, topics, and language from your text. Let's get started by trying out a demo of the API, then signing up for a preview version.

## Prerequisites

Before you begin building a canvas app using the Text Analytics API, you must prepare the Text Analytics resource. For more details, go to [Text Analytics API prerequisites](https://docs.microsoft.com/azure/cognitive-services/text-analytics/quickstarts/client-libraries-rest-api#prerequisites).

## Build the app

Now that you have the Text Analytics API up and running, you connect to it from Power Apps, and build an app that calls the API. This is a single screen app that demonstrates the Text Analytics API in action with a canvas app. Let's get started on building this!

> [!TIP]
> In this tutorial, you'll learn about creating a demo app with a few properties and values from the output using the Text Analytics API operations. You can use similar method to create your own app to show more or all such properties and values for the Text Analytics API operations.

## Step 1. Create the app and add a connection

Create a blank phone app and add a connection with the **Text Analytics** connector.

1. Go to [Power Apps](https://make.powerapps.com).

1. Select **Canvas app from blank**.

    ![Create an app from blank](./media/cognitive-services-api/app-from-blank.png "Create an app from blank")

1. Enter app name.

1. Choose a layout for the app. For this demo, we'll use **Tablet** layout.

    ![Name the app, choose the layout, and select Create](./media/cognitive-services-api/app-name-create.png "Name the app, choose the layout, and select Create")

1. Select **Data** from the left pane.

1. Search for **Text Analytics** connection.

    ![Add Text Analytics connection](./media/cognitive-services-api/text-analytics-data-source.png "Add Text Analytics connection")

1. Enter **Account Key**, and **Site URL** values.

    ![Account Key and Site URL for Text Analytics API in Power Apps](./media/cognitive-services-api/text-analytics-power-apps.png "Account Key and Site URL for Text Analytics API in Power Apps")

    You can find the **Account Key** and **Site URL** from the **KEY** and **Endpoint** values respectively using the Azure portal.

    ![KEY and Endpoint in Azure portal](./media/cognitive-services-api/account-key-endpoint-azure.png "KEY and Endpoint in Azure portal")

1. Select **Connect**.

Your app is now connected to the Cognitive Services resource of Text Analytics API type in Azure.

## Step 2. Design the app

In this section, you'll design the app controls, and the formulas required to work with the Text Analytics API. After you've completed the app design, this is how it'll look:

![Finished app](./media/cognitive-services-api/finished-app-no-data.png)

> [!NOTE]
> - Values for component properties such as alignment, size, color, position (X, Y) in this tutorial as suggested. Actual values may vary depending on the app layout you select. You can also change these suggested values to design the app as per your requirements.
> - To learn more about how to add controls and formulas to the controls in detail, see [Add and configure controls](add-configure-controls.md).

1. Select ![Insert](./media/cognitive-services-api/insert-icon.png "Insert") from the left pane.

1. Select **Text label**.

1. Change the label properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Text | "Text Analytics" |
    | Size | 36 |
    | Color | RGBA(255, 255, 255, 1) |
    | Fill | RGBA(56, 96, 178, 1)|
    | Align | Align.Center |
    | X | 0 |
    | Y | 0 |

1. Insert **Text label**.

1. Change the label properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Text | "Enter your text, select your options, then select 'Analyze text'" |
    | Size | 16 |
    | Align | Align.Center |
    | X | 24 |
    | Y | 135 |

1. Insert **Checkbox**.

1. Change the checkbox properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Name | chkLanguage |
    | Text | "Language" |
    | Size | 16 |
    | X | 24 |
    | Y | 228 |

1. Insert **Checkbox**.

1. Change the checkbox properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Name | chkSentiment |
    | Text | "Sentiment" |
    | Size | 16 |
    | X | 230 |
    | Y | 228 |

1. Insert **Checkbox**.

1. Change the checkbox properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Name | chkEL |
    | Text | "Entity Linking" |
    | Size | 16 |
    | X | 403 |
    | Y | 228 |

1. Insert **Checkbox**.

1. Change the checkbox properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Name | chkPhrases |
    | Text | "Key Phrases" |
    | Size | 16 |
    | X | 24 |
    | Y | 286 |

1. Insert **Checkbox**.

1. Change the checkbox properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Name | chkNER |
    | Text | "Named Entity Recognition" |
    | Size | 16 |
    | X | 230 |
    | Y | 286 |

1. Insert **Text input**.

1. Change the text input properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Name | tiTextToAnalyze |
    | Text | "Enter text" |
    | Size | 14 |
    | Height | 256 |
    | Mode | MultiLine |
    | Width | 557 |
    | X | 24 |
    | Y | 390 |

1. Insert **Button**.

1. Change the button properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Name | analyzeText |
    | Text | "Analyze Text" |
    | X | 189 |
    | Y | 684 |
    | Width | 196 |
    | Height | 53 |

1. Insert **Text label**.

1. Change the label properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Name | dLanguage |
    | Text | "Detected language:" |
    | Size | 16 |
    | X | 633 |
    | Y | 135 |
    | Width | 665 |
    | Height | 48 |

1. Insert **Text label**.

1. Change the label properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Name | sScore |
    | Text | "Sentiment score:" |
    | Size | 16 |
    | X | 633 |
    | Y | 196 |
    | Width | 656 |
    | Height | 48 |

1. Insert **Text label**.

1. Change the label properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Text | "Linked entities:" |
    | Size | 16 |
    | X | 633 |
    | Y | 258 |
    | Width | 206 |
    | Height | 48 |

1. Select **Insert** -> **Gallery** -> **Blank vertical**.

1. Change the gallery properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Name | galleryLE |
    | Layout | Title and subtitle |
    | X | 633 |
    | Y | 318 |
    | Width | 696 |
    | Height | 87 |

1. Select the arrow icon inside the gallery and delete it.

1. Insert **Text label**.

1. Change the label properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Text | "Key Phrases:" |
    | Size | 16 |
    | X | 633 |
    | Y | 429 |
    | Width | 150 |
    | Height | 48 |

1. Select **Insert** -> **Gallery** -> **Blank vertical**.

1. Change the gallery properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Name | galleryKP |
    | Layout | Title |
    | X | 633 |
    | Y | 489 |
    | Width | 696 |
    | Height | 87 |

1. Select the arrow icon inside the gallery and delete it.

1. Change the following properties for the first row inside the gallery.

    | Property Name | Value |
    | - | - |
    | X | 16 |
    | Height | 87 |

1. Insert **Text label**.

1. Change the label properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Text | "Named entities:" |
    | Size | 16 |
    | X | 633 |
    | Y | 589 |
    | Width | 193 |
    | Height | 48 |

1. Select **Insert** -> **Gallery** -> **Blank vertical**.

1. Change the gallery properties with the following configuration.

    | Property Name | Value |
    | - | - |
    | Name | galleryNER |
    | Layout | Title |
    | X | 633 |
    | Y | 670 |
    | Width | 696 |
    | Height | 87 |

1. Select the arrow icon inside the gallery and delete it.

1. Change the following properties for the first row inside the gallery.

    | Property Name | Value |
    | - | - |
    | X | 16 |
    | Height | 87 |

Here's how the app should look like after following the above steps.

![App design](./media/cognitive-services-api/app-design.png "App design")

## Step 3. Add logic

1. Copy and paste the following formula as the **OnSelect** property value for the button **analyzeText**.

    ```powerapps-dot
    ClearCollect( languageInfo, { id: "E393CEB2-56A8-4668-A5EB-A1254E9758F0", countryHint: "US", text: tiTextToAnalyze.Text } );
    TextAnalytics.LanguagesV3(languageInfo);
    If( chkLanguage.Value=true,
        ClearCollect( languageCollect,
            TextAnalytics.LanguagesV3(languageInfo).documents.detectedLanguage
        )
    );
    ClearCollect( phrasesInfo, { id: "E393CEB2-56A8-4668-A5EB-A1254E9758F0", language: "en", text: tiTextToAnalyze.Text } );
    If( chkPhrases.Value = true,
        ClearCollect( phrasesCollect,
            TextAnalytics.KeyPhraseV3(phrasesInfo).documents.keyPhrases
        )
    );
    ClearCollect( sentimentInfo, { id: "E393CEB2-56A8-4668-A5EB-A1254E9758F0", language: "en", text: tiTextToAnalyze.Text } );
    If( chkSentiment.Value = true,
        ClearCollect( sentimentCollect,
            TextAnalytics.SentimentV3(sentimentInfo).documents.confidenceScores
        )
    );      
    ClearCollect( nerinfo, { id: "E393CEB2-56A8-4668-A5EB-A1254E9758F0", language: "en", text: tiTextToAnalyze.Text } );
    If( chkNER.Value = true,
        ClearCollect( nerCollect,
            TextAnalytics.EntitiesRecognitionGeneralV3(nerinfo).documents.entities
        )
    );
    ClearCollect( elinfo, { id: "E393CEB2-56A8-4668-A5EB-A1254E9758F0", language: "en", text: tiTextToAnalyze.Text } );
    If( chkEL.Value = true,
        ClearCollect( elCollect,
            TextAnalytics.EntitiesLinkingV3(elinfo).documents.entities
        )
    ); 
    ```
1. Copy and paste the following formula as the value of the **Text** property for the **dLanguage** label.

    ```powerapps-dot
    "Detected language: " & First(languageCollect.detectedLanguage).detectedLanguage.name
    ```

1. Select the first row inside the **galleryKP** gallery. And then, copy and paste following formula for the **Text** property.

    ```powerapps-dot
    Concat(ThisItem.keyPhrases.Value, Value, ",")
    ```

1. Copy and paste the following formula as the value of the **Text** property for the **sScore** label. 

    ```powerapps-dot
    "Positive: " & ThisItem.confidenceScores.positive &" Neutral: " & ThisItem.confidenceScores.neutral & " Negative: " & ThisItem.confidenceScores.negative
    ```

1. Select the first row inside the **galleryNER** gallery. And then, copy and paste following formula for the **Text** property.

    ```powerapps-dot
    Concat(ThisItem.entities.text,text,",")
    ```

1. Select the first row inside the **galleryLE** gallery. And then, copy and paste following formula for the **Text** property.

    ```powerapps-dot
    Concat(ThisItem.entities.name,name,",")
    ```

1. Select the second row inside the **galleryLE** gallery. And then, copy and paste following formula for the **Text** property.

    ```powerapps-dot
    Concat(ThisItem.entities.url,url,",")
    ```

1. [Save and publish](save-publish-app.md) the app.

<!--

1. Resize the label as below.

    ![App banner](./media/cognitive-services-api/app-banner.png "App banner")

1. Add 

1. Change **Text** for this label to *Text Analytics*.


Follow the steps below to create this screen. If a control name is specified, that name is used in a formula in the next section.

1. On the **Home** tab, click or tap **New Screen**, then **Scrollable screen**. 

2. On **Screen2**, select **[Title]** and change it to **Text Analysis**.

3. Add a **Label** control for the introductory text.

4. Add a **Text input** control, so you can enter text to analyze. Name the control **tiTextToAnalyze**. The app should now look like the following image.
   
    ![App with title, subtitle, and text input](./media/cognitive-services-api/partial-app-step1.png)

5. Add three **Check box** controls, so you can choose which API operations to perform. Name the controls **chkLanguage**, **chkPhrases**, and **chkSentiment**.

6. Add a button, so you can call the API after selecting which operations to perform. The app should now look like the following image.
   
    ![App with check boxes and button](./media/cognitive-services-api/partial-app-step2.png)

7. Add three **Label** controls. The first two hold results from the language and sentiment API calls; the third is just an introduction for the gallery at the bottom of the screen.

8. Add a **Blank vertical gallery** control, then add a **Label** control to the gallery. The gallery holds results from the key phrases API call. The app should now look like the following image.
   
    ![App with labels and gallery](./media/cognitive-services-api/partial-app-step3.png)

9. In the left pane, select **Screen1** > ellipsis (**. . .**) > **Delete** (you don't need this screen for the app).

We're keeping this app simple to focus on calling the Text Analytics API, but you could add things - like logic to show and hide controls based on the check boxes selected, error handling if the user doesn't select any options, and so on.

### Add logic to make the right API calls
OK, you have a nice-looking app, but it doesn't do anything yet. You'll fix that in a moment. But before we dive into the details, let's understand the pattern that the app follows:

1. The app makes specific API calls based on the check boxes selected in the app. When you click or tap **Analyze text**, the app makes 1, 2, or 3 API calls.

2. The app stores data that the API returns in three different [collections](working-with-variables.md#use-a-collection): **languageCollect**, **sentimentCollect**, and **phrasesCollect**.

3. The app updates the **Text** property for two of the labels, and the **Items** property for the gallery, based on what's in the three collections.

With that background, let's add the formula for the **OnSelect** property of the button. This is where all the magic happens.

```powerapps-dot
If( chkLanguage.Value = true,
    ClearCollect( languageCollect, 
        TextAnalytics.DetectLanguageV2(
            {
                text: tiTextToAnalyze.Text
            }
        ).detectedLanguages.name
    )
);

If( chkPhrases.Value = true,
    ClearCollect( phrasesCollect, 
        TextAnalytics.KeyPhrasesV2(
            {
                language: "en", 
                text: tiTextToAnalyze.Text
            }
        ).keyPhrases
    )
);

If( chkSentiment.Value = true,
    ClearCollect( sentimentCollect, 
        TextAnalytics.DetectSentimentV2(
            {
                language: "en", 
                text: tiTextToAnalyze.Text
            }
        ).score
    )
)
```

There's a bit going on here, so let's break it down:

* The **If** statements are straightforward – if a specific check box is selected, make the API call for that operation.

* Within each call, specify the appropriate parameters:

  * In all three calls, you specify **tiTextToAnalyze.Text** as the input text.

  * In **DetectLanguage()**, **numberOfLanguagesToDetect** is hard-coded as 1, but you could pass this parameter based on some logic in the app.

  * In **KeyPhrases()** and **DetectSentiment()**, **language** is hard-coded as "en", but you could pass this parameter based on some logic in the app. For example, you could detect the language first, then set this parameter based on what **DetectLanguage()** returns.

* For each call that is made, add the results to the appropriate collection:

    * For **languageCollect**, add the **name** of the language that was identified in the text.

    * For **phrasesCollect**, add the **keyPhrases** that were identified in the text.

    * For **sentimentCollect**, add the sentiment **score** for the text, which is a value of 0-1, with 1 being 100% positive.

### Display the results of the API calls
To display the results of the API calls, reference the appropriate collection in each control:

1. Set the **Text** property of the language label to: `"The language detected is " & First(languageCollect).name`.
   
    The **First()** function returns the first (and in this case only) record in **languageCollect**, and the app displays the **name** (the only field) associated with that record.

2. Set the **Text** property of the sentiment label to: `"The sentiment score is " & Round(First(sentimentCollect.Value).Value, 3)*100 & "% positive."`.
   
    This formula also uses the **First()** function, gets the **Value** (0-1) from the first and only record, then formats it as a percentage.

3. Set the **Items** property of the key phrases gallery to: `phrasesCollect`.
   
    You're now working with a gallery so you don't need the **First()** function to extract a single value. You reference the collection, and the gallery displays the key phrases as a list.

## Run the app

Now that the app is finished, run it to see how it works: click or tap the run button in the upper right corner ![Run the app](./media/cognitive-services-api/icon-run-app.png). In the following image, all three options are selected, and the text is the same as the default text on the Text Analytics API page.

![Finished app with data](./media/cognitive-services-api/finished-app.png)

If you compare the output of this app to the Text Analytics API page at the beginning of this article, you see that the results are the same.

We hope you now understand a little more about the Text Analytics API, and you've enjoyed seeing how to incorporate it into an app. Let us know if there are other Cognitive Services (or other services in general) that you would like us to focus on in our articles. As always, please leave feedback and any questions in the comments.



[!INCLUDE[footer-include](../../includes/footer-banner.md)]