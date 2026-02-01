--- 
Source: Unity 6 Manual (android-asset-splitting.md)
---

# Introduction to asset splitting
Depending on which publishing format your application uses, there is a different solution for asset splitting.
The following table shows which asset splitting solution is for which publishing format:
| **Publishing format** | **Asset splitting solution** |
| --- | --- |
| ****APK**The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html) See in [Glossary](Glossary.html#APK)** | [APK expansion files](android-OBBsupport.html) |
| [Android App Bundle](https://developer.android.com/guide/app-bundle) (AAB) | [Play Asset Delivery](play-asset-delivery.html) |
**Note**: Some [digital distribution services](android-distribution.html) require applications to use a specific publishing format. For example, [Google Play](https://play.google.com/about/howplayworks/) requires new applications to use the AAB format which means your application must use [Play Asset Delivery](play-asset-delivery.html) if you want to distribute your application through Google Play.
## Additional resources
* [APK expansion files](android-OBBsupport.html)
* [Play Asset Delivery](play-asset-delivery.html)