Title: Misc
Slug: misc

Not everything I work on fits neatly into the digital storytelling world. Sometimes the story lives in a software tool that solves a particular problem, or in a presentation where you're reading the room instead of designing for a screen. This is where I've collected the projects that live outside the purely digital storytelling realm but still capture that same drive to make complex ideas accessible and engaging.

## **Software**

Most of my days are spent deep in code, building tools that bridge the messy reality of academic R&D with the polished expectations of industry delivery. I'm also a huge believer in open-source scientific programming.

### *NASA Surface, Terrain, and Vegetation (STV)*

A large majority of my time at grad school was supporting the STV mission and understanding the bias of different spaceborne altimetry measurements--you'd be surprised at just how much radar vs lasers vs photogrammetry disagree on tree heights. Below is a Python package built on Pixi and Ruff for grabbing and analyzing these alitmetry measurements from the various disconnected APIs and cloud storage endpoints (prioritizing STAC-compliant data). This feeds into larger NASA efforts with [computer vision approaches for multimodal sensor fusion](https://github.com/uw-cryo/DeepDEM) and [custom lidar processing algorithms](https://github.com/uw-cryo/lidar_tools/tree/main/notebooks).

[https://coincident.readthedocs.io/en/latest/](https://coincident.readthedocs.io/en/latest/)

### *Open-Source Software*

A small toolkit that pulls together commerical synthetic aperture radar organizations' open-source data inventories (Capella, ICEYE, Umbra) into a single, tidy table. Great if you want to quickly see what imagery exists over a place without hunting three different websites with three different data storage structures. It automatically updates every week too!

[https://github.com/Jack-Hayes/commerical-sar-stac](https://github.com/Jack-Hayes/commerical-sar-stac)

Want to see where there's forest and where there's not? A tiny command-line helper that grabs Meta’s 1-meter tree-height maps and returns a clipped TIFF plus a simple "forest or not" mask for any area you care about.

[https://github.com/Jack-Hayes/fetch_meta_chm](https://github.com/Jack-Hayes/fetch_meta_chm)

Draw a box on a map and instantly preview cloud-free satellite RGB, synthetic aperture radar, and contextual layers (shaded relief and land cover classification) in just a few seconds. A playful, browser-ready explorer for Earth imagery--no coding experience needed!

[https://github.com/Jack-Hayes/planetquery](https://github.com/Jack-Hayes/planetquery)

## **Presentations**

Face-to-face storytelling is truly irreplaceable--the real-time feedback, the shared energy when an idea finally lands. I've had the privilege of speaking with wildly different audiences about various topics I'm excited about, whether that's pitching Microsoft partners on why campus needs more high-performance computing support, sitting on a panel with climate scientists at the American Geophysical Union, or explaining what gravitational waves are to families and how machine learning algorithms help with detecting them.

[*Oral presentation on community-based water resource management in Nepal + a panel on climate science*](https://ui.adsabs.harvard.edu/abs/2023AGUFMSY22A..04H/abstract)

[*A night spent explaining gravitational waves and computer vision to families and students in Williamsburg, VA*](https://events.wm.edu/event/view/appliedscience/353443)

[*Technical presentation on geospatial data software infrastructure development*](https://sdl.gis.harvard.edu/event/symposium-spatiotemporal-data-science-geoai-social-sciences)

## **Side Projects**

### *What even is a Photon-Counting Satellite?*

Here is an incomplete GitHub repository of a final project from grad school focused on what 'elevation' actually means from a photon-counting satellite.

[https://github.com/Jack-Hayes/ATL06-Archive?tab=readme-ov-file#project-overview](https://github.com/Jack-Hayes/ATL06-Archive?tab=readme-ov-file#project-overview)