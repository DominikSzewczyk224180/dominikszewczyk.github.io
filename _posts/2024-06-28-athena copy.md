---
layout: post
title: AI-Powered 3D Digital Twin & Object Removal Research
subtitle: A Collaborative Project with Antea Group & Kavel 10
gh-repo: DominikSzewczyk224180/Projects-2023-2024
gh-badge: [star, fork, follow]
tags: [Machine Learning, Data Science, Computer Vision, 3D Reconstruction, NeRF, Urban Digital Twins]
thumbnail-img: /assets/img/antea_project_thumbnail.png
comments: true
mathjax: false
author: Dominik Szewczyk
categories: projects
---

{: .box-success}
This project, in collaboration with Antea Group and Kavel 10, focused on AI-driven automation for 3D urban modeling. We explored semantic segmentation, generative AI for object removal, and Neural Radiance Fields (NeRF) to enhance digital twin generation.

**Project Duration:** September 2025 - February 2025 

## 💡 Project Summary  

Our team researched AI methods to automate the reconstruction of urban environments. The project involved developing custom machine learning pipelines for object removal, leveraging semantic segmentation to detect and isolate structures, and utilizing NeRF for high-fidelity 3D visualization. The ultimate goal was to improve 3D mesh quality from aerial imagery, supporting urban planning and infrastructure projects.

## 🖼️ Image Inpainting & Semantic Segmentation  

- Tested and compared DeepFill v2, LaMa, and PowerPaint for object removal on client data.  
- Developed a custom ML pipeline allowing users to preprocess data, adjust model parameters, and train segmentation models through a CLI interface.  
- Trained a semantic segmentation model to detect and isolate trees, preparing for future AI-powered object removal.  
- Evaluated models like U-Net, DeepLabV3, and FCN on key metrics such as accuracy and IoU, selecting FCN as the most effective model. (Full process and technical aspects detailed in the report.)  

## 🌍 3D Reconstruction & NeRF Exploration  

- Implemented Instant NeRF to generate high-quality 3D visualizations from short drone video sequences.  
- Used NeRF Studio to create, refine, and optimize point clouds for 3D mesh generation.  
- Cleaned point clouds and generated detailed 3D meshes, improving visual fidelity for urban reconstruction.  
- Developed a VR environment in Unreal Engine, allowing immersive exploration of reconstructed urban areas.  

## 📑 Final Deliverables & Presentation  

- Delivered reports covering data quality, project lifecycle, and AI model recommendations. (Includes a NeRF recommendation document detailing implementation steps, data preparation, and potential applications.)  
- Created a CLI interface for data preparation and model training.  
- Presented findings to mentors, peers, and clients in a final conference, demonstrating AI’s impact on urban digital twin advancements.  

## 📸 Project Snapshots  

![3D Reconstruction]({{ '/assets/img/antea_3d_mesh.png' | relative_url }})  
![NeRF Point Cloud]({{ '/assets/img/antea_nerf_pointcloud.png' | relative_url }})  
![Semantic Segmentation]({{ '/assets/img/antea_segmentation.png' | relative_url }})  

## 🔗 Links  

- [View the Project on GitHub](https://github.com/DominikSzewczyk224180/Projects-2023-2024)  

## 🛠 Skills  

- Machine Learning  
- Data Science  
- Image Inpainting  
- Computer Vision  
- Neural Radiance Fields (NeRF)  
- 3D Reconstruction  
- Unreal Engine  
- Python  
- Machine Learning Pipelines  
- CLI Development  
